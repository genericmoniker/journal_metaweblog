#!/usr/bin/python

# Copyright (C) 2014 Eric Smith (http://esmithy.net)
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from SimpleXMLRPCServer import SimpleXMLRPCServer
import os.path

PORT = 8085
BLOG_URL = "http://localhost:{0}".format(PORT)
HTML = (u'<html><head><title>{0}</title><meta charset="utf-8"></head>'
        '<body><p>{0}</p>{1}</body></html>')


def get_user_blogs(key, username, password):
    return [{'url': BLOG_URL, 'blogid': '1', 'blogName': 'Save HTML'}]


def new_post(blogid, username, password, struct, publish):
    filename = _get_filename(struct['title'])
    _write_html(filename, struct['title'], struct['description'])
    return struct['title']


def get_post(postid, username, password):
    filename = _get_filename(postid)
    print 'Reading HTML from ' + filename
    struct = {'title': postid}
    with open(filename, 'r') as f:
        struct['description'] = f.read()
    return struct


def edit_post(postid, username, password, struct, publish):
    filename = _get_filename(postid)
    _write_html(filename, struct['title'], struct['description'])
    return True


def _get_filename(n):
    year = n.split('-')[0]
    return os.path.expanduser(
        '~/Documents/Journal/{0}/{1}.html'.format(year, n))


def _write_html(filename, title, body):
    print 'Saving HTML to ' + filename
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
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