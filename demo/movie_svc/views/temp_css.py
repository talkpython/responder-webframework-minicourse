import os

from app_instance import api


# This sucks. But at the moment I'm publishing this code / video
# Responder has developed a bug where it cannot serve static files
# See https://github.com/kennethreitz/responder/issues/337
#
# This is just a work around so you all can enjoy the course.

@api.route("/css/{file}")
def css(req, resp, file):
    resp.headers['Content-Type'] = 'text/css'
    full_file = os.path.join(
        os.path.dirname(__file__),
        '..',
        'css',
        file
    )
    with open(full_file, encoding='utf-8') as fin:
        resp.content = fin.read()
