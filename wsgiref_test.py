from wsgiref.util import setup_testing_defaults, shift_path_info
from wsgiref.simple_server import make_server
import json

def simple_app(environ, start_response):
    setup_testing_defaults(environ)
    url = shift_path_info(environ)

    print(environ['REQUEST_METHOD'])

    status = '200 OK'
    headers = [('Content-type', 'text/html')]

    start_response(status, headers)
    if url == "":
        return [b"<html><body><h1>Hello</h1></body></html>"]
    else:
        return [b"<html><body><h1>Halaman Tidak ada</h1></body></html>"]

httpd = make_server('', 8000, simple_app)
print("Serving on port 8000...")
httpd.serve_forever()
