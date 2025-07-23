from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    pass

if __name__ == "__main__":
    server = HTTPServer(("", PORT), Handler)
    print(f"Serving at http://localhost:{PORT}")
    server.serve_forever()
