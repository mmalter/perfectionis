class Resource:
   """
   A resource for an API.
   """

   def __init__(self,
                name,
                content_acceptors = None,
                content_providers = None,
               ):
       self.name = name
       self.content_acceptors = content_acceptors
       self.content_providers = content_providers

    @property
    def route(self):
        return "/" + self.name

    @property
    def children(self):
        return []

    def allow_missing_post(self, request):
        return False

    def charsets_provided(self, request):
        return "*"

    def is_allowed(self, request):
        """
        Specify wether the request is allowed wrt authentication.
        Sends 401 if the function returns False
        """
        return True

    def deletion_checker(self, request):
        return True

    def expires_at(self, request):
        return "never"

    def is_forbidden(self, request):
        return False

    def etag(self, request):
        return None

    def conflicts(self, request):
        """
        Returns true if a PUT request results in a conflict.
        Sends 409 if so.
        """
        return False

    def language_provided(self, request):
        return ["en"]

    def last_modified(self, request):
        return None

    def malformed_request(self, request):
        return False

    def moved_temporarily(self, request):
        return False

    def moved_permanently(self, request):
        return False

    def multiple_choices(self, request):
        return False

    def previously_existed(self, request):
        return False

    def rate_limited(self, request):
        return False

    def ressource_exists(self, request):
        return True

    def ressource_available(self, request):
        return True

    def uri_too_long(self, request):
        return False

    def valid_content_headers(self, request):
        return True

    def valid_entity_length(self, request):
        return True
