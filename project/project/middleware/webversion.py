from django.conf import settings
from django.shortcuts import redirect
from urllib.parse import urlsplit, urlunsplit

class WebVersionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if getattr(settings, 'WEB_VERSION', None) == "NEW":
            url_parts = urlsplit(request.get_full_path())
            path = url_parts.path
            query = url_parts.query
            if self.should_redirect(path):
                new_path = self.insert_new_before_last_slash(path)
                new_url = urlunsplit((url_parts.scheme, url_parts.netloc, new_path, query, url_parts.fragment))
                return redirect(new_url)
        return response

    def should_redirect(self, path):
        return not path.endswith('new/') and (path.startswith(("/story/", "/user/")) or path in ("/aboutus/", "/home/"))

    def insert_new_before_last_slash(self, path):
        segments = path.rstrip('/').split('/')
        segments[-1] = segments[-1] + 'new'
        return '/'.join(segments) + '/'
