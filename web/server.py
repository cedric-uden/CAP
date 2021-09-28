from http.server import HTTPServer, SimpleHTTPRequestHandler

PORT = 8080


class HttpRequestHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        '': 'application/octet-stream',
        '.manifest': 'text/cache-manifest',
        '.html': 'text/html',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg':	'image/svg+xml',
        '.css':	'text/css',
        '.js': 'application/x-javascript',
        '.wasm': 'application/wasm',
        '.json': 'application/json',
        '.xml': 'application/xml',
    }


def run():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, HttpRequestHandler)
    httpd.serve_forever()


run()
