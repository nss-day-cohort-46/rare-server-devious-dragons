from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from posts.request import get_all_posts, get_single_post
from users.request import register_user


class HandleRequests(BaseHTTPRequestHandler):
    def parse_url(self, path):
        path_params = path.split("/")
        resource = path_params[1]

        if "?" in resource:
            resource, param = resource.split("?")
            key, value = param.split("=")

            return (resource, key, value)
            
        else:
            id = None

            try:
                id = int(path_params[2])
            except IndexError:
                pass
            except ValueError:
                pass

            return (resource, id)

    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        response = {}
        parsed = self.parse_url(self.path)

        if len(parsed) == 2:
            resource, id = parsed
            if resource == "posts":
                if id is not None:
                    response = f"{get_single_post(id)}"
                else:
                    response = f"{get_all_posts()}"

        self.wfile.write(f"{response}".encode())

    def do_POST(self):
        # Set response code to 'Created'
        self._set_headers(201)

        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)

        post_body = json.loads(post_body)

        resource, id = self.parse_url(self.path)

        new_item = None

        if resource == "login":
            # This will be replaced with validate_user(post_body)
            #####################################################
            #####################################################
            #####################################################

            #
            new_item = {
                "valid": True,
                "token": 1
            }
            new_item = json.dumps(new_item)

        if resource == "register":
            new_item = register_user(post_body)

        self.wfile.write(f"{new_item}".encode())

def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
