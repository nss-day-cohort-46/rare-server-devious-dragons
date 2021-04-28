from categories.request import update_category
from comments.request import create_comment, get_all_comments
from categories import create_category, get_all_categories, delete_category
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

from posts.request import create_post, get_all_posts, get_single_post
from users.request import register_user
from users.request import get_auth_user
from tags.request import get_all_tags
from tags.request import create_tag
from tags.tag_request import create_post_tag


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

                
            elif resource == "categories":
                response = f"{get_all_categories()}"

            elif resource == "comments":
                response = f"{get_all_comments()}"

            
            elif resource == "tags":
                response = f"{get_all_tags()}"



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
            new_item = get_auth_user(post_body)

        if resource == "register":
            new_item = register_user(post_body)


        if resource == "posts":
            new_item = create_post(post_body)
        
        if resource == "categories":
            new_item = create_category(post_body)

        if resource == "comments":
            new_item = create_comment(post_body)
  
        if resource == "tags":
            new_item = create_tag(post_body)
        
        if resource == "postTags":
            new_item = create_post_tag(post_body)


        self.wfile.write(f"{new_item}".encode())

    def do_PUT(self):
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        resource, id = self.parse_url(self.path)

        success = False

        if resource == "categories":
            success = update_category(id, post_body)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def do_DELETE(self):
        self._set_headers(204)
        resource, id = self.parse_url(self.path)

        if resource == "categories":
            delete_category(id)


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
