#!/usr/bin/python
# journal.py - by Eric Smith - http://esmithy.net

from SimpleXMLRPCServer import SimpleXMLRPCServer
import os.path

PORT = 8085
BLOG_URL = "http://localhost:{0}".format(PORT)
HTML = u'<html><head><title>{0}</title><meta charset="utf-8"></head><body><p>{0}</p>{1}</body></html>'

def get_user_blogs(key, username, password):
    return [{'url':BLOG_URL, 'blogid':'1', 'blogName':'Save HTML'}]

def new_post(blogid, username, password, struct, publish):
    filename = _get_filename(struct['title'])
    _write_html(filename, struct['title'], struct['description'])
    return struct['title']

def get_post(postid, username, password):
    filename = _get_filename(postid)
    print 'Reading HTML from ' + filename
    struct = {'title':postid}
    with open(filename, 'r') as f:
        struct['description'] = f.read()
    return struct

def edit_post(postid, username, password, struct, publish):
    filename = _get_filename(postid)
    _write_html(filename, struct['title'], struct['description'])
    return True

def _get_filename(n):
    year = n.split('-')[0]
    return os.path.expanduser('~/Documents/Journal/{0}/{1}.html'.format(year, n))

def _write_html(filename, title, body):
    print 'Saving HTML to ' + filename
    with open(filename, 'w') as f:
        f.write(HTML.format(title, body).encode("utf-8"))

def main():
    server = SimpleXMLRPCServer(('localhost', PORT))
    server.register_introspection_functions()
    server.register_function(get_user_blogs, 'blogger.getUsersBlogs')
    server.register_function(new_post, 'metaWeblog.newPost')
    server.register_function(get_post, 'metaWeblog.getPost')
    server.register_function(edit_post, 'metaWeblog.editPost')
    print "===== Journal MetaWebLog Server ====="
    print "Listening on port {0}".format(PORT)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()