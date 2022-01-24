from http.server import HTTPServer, BaseHTTPRequestHandler


class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html/css/js')
        self.end_headers()
        self.wfile.write('Hello loklok!\n'.encode())
        self.wfile.write(self.path.encode())


def main():
    PORT = 6969
    server = HTTPServer(('', PORT), echoHandler)
    print("server is running on port %s" % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
