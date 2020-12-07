import os
import http.server
import socketserver

from http import HTTPStatus


from urllib.parse import urlparse, parse_qs


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        query_components = parse_qs(urlparse(self.path).query)
        print(query_components)
        challenge = query_components["hub.challenge"] 
        msg = '%s' % (challenge)
        self.wfile.write(challenge)
        print(self.request)


port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)
httpd.serve_forever()
