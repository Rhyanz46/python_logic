import http.server

PORT = 8000

server = http.server


class S(server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _set_headers_not_found(self):
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if self.path == "/a":
            self._set_headers()
            self.wfile.write(b"<html><body><h1>hay aaa</h1></body></html>")
        else:
            self._set_headers_not_found()
            self.wfile.write(b"<html><body><h1>tidak ada</h1></body></html>")


httpd = server.HTTPServer(('', 8000), S)
print("Serving on port 8000...")
httpd.serve_forever()