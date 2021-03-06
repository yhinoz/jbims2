#!/usr/bin/env python
# coding: utf-8

def main():
    import os, sys
    import cgi
    import traceback
    import cgitb;
    import logging.config
    import config as cfg

    sys.path.append(cfg.DIR_LIB)
    logging.config.fileConfig(cfg.LOG_CONF)
    cgitb.enable()

    from mako.lookup import TemplateLookup
    from mako import exceptions
    from jcore.util import Util
    from jcore.jband import Dao
    from jcore.live import LiveManager
    from jcore.controller import Controller
    from jcore.logger import Logger

    log = Logger()

    try:
        ut  = Util()
        req = cgi.FieldStorage()
        ctrller = Controller(cfg.LIVE_STATUS)

        ps  = ut.getParam(req, 'ps')    # entry process no.
        id  = ut.getParam(req, 'id')    # band reg id.
        ver  = ut.getParam(req, 'ver')  # band reg version.
        params = {}                     # for request params.
        errors = {}                     # for error.

        if ctrller.is_start() == False:
            # redirect error page.
            log.error('live entry is not start. errors = [id]')
            return ut.redirect(cfg.URL_ERR_500)
            
        if id == '':
            # redirect error page.
            log.error('validate error. errors = [id]')
            return ut.redirect(cfg.URL_ERR_500)
        if ver == '':
            # redirect error page.
            log.error('validate error. errors = [ver]')
            return ut.redirect(cfg.URL_ERR_500)

        if req.has_key('goback'):
            ps = '1'

        dao = Dao(cfg.DB_BAND)
        band = dao.get_band_by_id(id)

        if ps == '1':
            tmpl_name_entry_live = cfg.TMPL_ENTRY_LIVE_PS1

            # get request.
            for key in cfg.REQ_GET_KEY_ENTRY_LIVE_PS1:
                tmp = ut.getParam(req, key)
                if tmp != '':
                    params[key] = tmp

        elif ps == '2':
            tmpl_name_entry_live = cfg.TMPL_ENTRY_LIVE_PS2

            # get request.
            for key in cfg.REQ_GET_KEY_ENTRY_LIVE_PS1:
                tmp = ut.getParam(req, key)
                if tmp != '':
                    params[key] = tmp

            #todo うまくないから関数化
            # get member.
            members = []
            parts   = []
            for i in range(int(band.member_num)):
                members.append(ut.getParam(req, 'member'+ str(i)))
                parts.append(ut.getParam(req, 'part'+ str(i)))
                if cfg.REQUIRE_KEY_REG.has_key('member') and members[i] == '':
                    errors['member'+ str(i)] = cfg.REQUIRE_KEY_REG['member'] % (i+1)
            params['member'] = cfg.DATA_DELIMITER.join(members)
            params['part'] = cfg.DATA_DELIMITER.join(parts)

            # convert comment
            params['comment'] = cfg.DATA_DELIMITER.join(params['comment'].split("\r\n"))

            if len(errors) > 0:
                tmpl_name_entry_live = cfg.TMPL_ENTRY_LIVE_PS1

        elif ps == '3':
            tmpl_name_entry_live = cfg.TMPL_ENTRY_LIVE_PS4

            # get request.
            for key in cfg.REQ_GET_KEY_ENTRY_LIVE_PS3:
                params[key] = ut.getParam(req, key)

            # TODO うまくないから関数化
            # list to scalar
            m_name = []
            m_time = []
            for i in range(int(params.get('music_num'))):
                m_name.append(ut.getParam(req, 'music_name'+ str(i)))
                m_time.append(ut.getParam(req, 'music_time'+ str(i)))
            params['music_name'] = cfg.DATA_DELIMITER.join(m_name)
            params['music_time'] = cfg.DATA_DELIMITER.join(m_time)
            params['music_genre'] = ''
            params['music_comp'] = ''

            # regist liveinfo.
            reg_res = dao.regist_liveinfo(id, ver, params)
            if reg_res == True:
                log.info('regist liveinfo. rec_id[%s], rec_version[%s], band_name[%s]' % (id, ver, band.band_name))
            else:
                log.error('regist liveinfo failed. rec_id[%s], rec_version[%s], band_name[%s]' % (id, ver, band.band_name))
                return ut.redirect(cfg.URL_ERR_500)

            # get new bandinfo.
            band = dao.get_band_by_id(id)
            ver = band.__version__

        #elif ps == '4':
        #    tmpl_name_entry_live = cfg.TMPL_ENTRY_LIVE_PS4
        #    # get request.
        #    upd_params = {}
        #    for key in cfg.REQ_GET_KEY_ENTRY_LIVE_PS4:
        #        params[key] = ut.conv_encoding(ut.getParam(req, key), 'sjis', 'utf-8')

        #    try:
        #        live_manager = LiveManager()
        #        live_manager.set_template_dir(cfg.DIR_SVG_TMPL)
        #        svg_data = live_manager.create_svg(params)
        #        svg_file = id+'.svg'
        #        ut.writeFile(cfg.DIR_SVG+svg_file, svg_data)
        #        params['stage_setting'] = svg_file
        #    except:
        #        log.error('create_svg failed.' + exceptions.text_error_template().render())
        #        return ut.redirect(cfg.URL_ERR_500)

        #    entry_res = dao.entry_live(id, ver, params)
        #    if entry_res == True:
        #        log.info('entry live. rec_id[%s], rec_version[%s]' % (id, ver))
        #    else:
        #        log.error('entry live failed. rec_id[%s], rec_version[%s]' % (id, ver))
        #        return ut.redirect(cfg.URL_ERR_500)

        #    # get new bandinfo.
        #    band = dao.get_band_by_id(id)

        else:
            # redirect error page.
            log.warn('unknown process code. ps[%s], remote_addr[%s]' % (ps, os.environ.get('REMOTE_ADDR','')))
            return ut.redirect(cfg.URL_ERR_500)

        # set template.
        tmpl_lookup = TemplateLookup(cfg.DIR_TMPL, output_encoding='utf-8', input_encoding='utf-8', default_filters=['decode.utf8'])
        tmpl_entry  = tmpl_lookup.get_template(tmpl_name_entry_live)

        print tmpl_entry.render(**locals())

        dao.close()

    except: 
        #TODO エラー画面リダイレクトできない
        log.error(exceptions.text_error_template().render())
        return ut.redirect(cfg.URL_ERR_500)

if __name__ == '__main__':
    main()
