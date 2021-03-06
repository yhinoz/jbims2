# -*- coding: utf-8 -*-
"""
JBIMS 設定ファイル
"""

#-- URL設定
URL_TOP     = '/~club/jbims2/'
URL_SVG     = '/~club/jbims2/svg/'
URL_ERR_500 = URL_TOP + '/err.html'

#-- ディレクトリ
DIR_SYS     = '/Users/yhino/UHD/dev/jacla/src/'
DIR_LIB     = DIR_SYS + 'lib/'
DIR_DB      = DIR_SYS + 'db/'
DIR_TMPL    = DIR_SYS + 'tmpl/'
DIR_CONF    = DIR_SYS + 'conf/'
DIR_SVG_TMPL = DIR_SYS + 'svgtmpl/'
DIR_SVG     = DIR_SYS + 'svg/'

#-- ファイルパス
LOG_CONF    = DIR_CONF  + 'log.conf'
DB_BAND     = DIR_DB    + 'jbims.db'
LIVE_STATUS = DIR_DB    + '.on_live'

#-- テンプレート名
TMPL_HEADER             = 'header.tmpl'
TMPL_FOOTER             = 'footer.tmpl'
TMPL_INDEX              = 'index.tmpl'
TMPL_LOGIN              = 'login.tmpl'
TMPL_REG_PS1            = 'reg_ps1.tmpl'
TMPL_REG_PS2            = 'reg_ps2.tmpl'
TMPL_REG_PS3            = 'reg_ps3.tmpl'
TMPL_ENTRY_LIVE_PS1     = 'entry_live_ps1.tmpl'
TMPL_ENTRY_LIVE_PS2     = 'entry_live_ps2.tmpl'
TMPL_ENTRY_LIVE_PS3     = 'entry_live_ps3.tmpl'
TMPL_ENTRY_LIVE_PS4     = 'entry_live_ps4.tmpl'
TMPL_VIEW_ENTRY         = 'view_entry.tmpl'
TMPL_CANCEL_ENTRY_PS1   = 'cancel_entry_ps1.tmpl'
TMPL_CANCEL_ENTRY_PS2   = 'cancel_entry_ps2.tmpl'
TMPL_DEL_BAND_PS1       = 'del_band_ps1.tmpl'
TMPL_DEL_BAND_PS2       = 'del_band_ps2.tmpl'
TMPL_EDIT_BAND_PS1      = 'edit_band_ps1.tmpl'
TMPL_EDIT_BAND_PS2      = 'edit_band_ps2.tmpl'
TMPL_EDIT_BAND_PS3      = 'edit_band_ps3.tmpl'

#-- 各リスト
LST_BAND_PART   = ('--', 'Gt', 'Ba', 'Key', 'Piano', 'Dr', 'Perc', 'Cl', 'Fl', 'SSax', 'ASax', 'TSax', 'BSax', 'Tp', 'Tb', 'Violin', 'Syn', 'EWI', 'Other')

#-- 取得リクエストキー
REQ_GET_KEY_LOGIN   = ('id', '_done')
REQ_GET_KEY_PS1     = ('band_name', 'genre', 'leader_name', 'leader_mail', 'passwd', 're_passwd', 'member_num')
REQ_GET_KEY_PS2     = ('band_name', 'genre', 'leader_name', 'leader_mail', 'passwd', 're_passwd', 'member_num')
REQ_GET_KEY_PS3     = ('band_name', 'genre', 'leader_name', 'leader_mail', 'passwd', 're_passwd', 'member_num', 'member', 'music_name', 'comment')
REQ_GET_KEY_ENTRY_LIVE_PS1 = ('band_name', 'genre', 'part', 'member', 'comment', 'music_num')
REQ_GET_KEY_ENTRY_LIVE_PS2 = ('band_name', 'genre', 'part', 'member', 'comment', 'music_num')
REQ_GET_KEY_ENTRY_LIVE_PS3 = ('band_name', 'genre', 'part', 'member', 'comment', 'music_num', 'music_name', 'music_time')
REQ_GET_KEY_ENTRY_LIVE_PS4 = ('s_microphone', 's_amplifer', 's_keyboard', 's_other', 's_supplement', 's_useDrum', 's_usePercussion', 's_useLainy', 's_useJazzCorus', 's_useAmpeg')
REQ_GET_KEY_EDIT_BAND_PS1  = ('band_name', 'genre', 'leader_name', 'leader_mail', 'chg_passwd', 'passwd', 're_passwd', 'member_num')
REQ_GET_KEY_EDIT_BAND_PS2  = ('band_name', 'genre', 'leader_name', 'leader_mail', 'chg_passwd', 'passwd', 're_passwd', 'member_num')
REQ_GET_KEY_EDIT_BAND_PS3  = ('band_name', 'genre', 'leader_name', 'leader_mail', 'passwd', 'member_num', 'member', 'music_name', 'comment')

#-- エラーメッセージ
REQUIRE_KEY_REG = {
    'band_name'     : 'バンド名を入力して下さい',
    'genre'         : 'ジャンルを入力して下さい',
    'leader_name'   : '代表者を入力して下さい',
    'leader_mail'   : '代表者メールアドレスを入力して下さい',
    'passwd'        : 'パスワードを入力して下さい',
    're_passwd'     : 'パスワードを再入力して下さい',
    'member'        : 'メンバー%sを入力して下さい'
}
REQUIRE_KEY_LOGIN = {
    'id'    : 'not get id.',
    '_done' : 'not get done.'
}

#-- 各種設定
DATA_DELIMITER = ''
STAGE_DATA_DELIMITER = "\t"
