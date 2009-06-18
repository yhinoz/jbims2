import sha

class Util:

    def getParam(self, cgi, key, default = ''):
        if cgi.has_key(key):
            if isinstance(cgi[key], list):
                return cgi.getlist(key)
            else:
                return cgi.getfirst(key)
        else:
            return default

    def getParams(self, req, keys, requires = {}, errors = {}):
        params = {}
        for key in keys:
            params[key] = self.getParam(req, key)
            # validate param
            if requires.has_key(key) and params[key] == '':
                errors[key] = requires[key]
        return params
    
    def redirect(self, url):
        print 'Status: 301 Moved Permanently'
        print "Location: %s\n" % (url)
        return True

    def cryptPasswd(self, raw):
        s = sha.new(raw)
        return s.hexdigest()
    
    def chkMailAddr(self, param):
        parts = param.split('@')
        if len(parts) != 2:
            return False
        for p in parts:
            if p == '':
                return False
        return True

    def writeFile(self, file, data, mode='w'):
        fp = open(file, mode)
        fp.write(data)
        fp.close()
