from collections import defaultdict

class Request:
    """
    HTTP requests
    """

    def __init__(self, scope):
        self.scope = defaultdict(lambda: None, scope)
        self.type = scope["type"]
        self.http_version = scope["http_version"]
        self.method = scope["method"]
        self.path = scope["path"]
        self.headers = scope["headers"]
        self.client = scope["client"]

class Response:
    """
    HTTP response
    """

    def __init__(self, code, headers, body):
        self.code = code
        self.headers = headers
        self.body = body
