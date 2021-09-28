from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8080


def run():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()


run()
