from collections import deque
from perfectionis.telecom import Request, Response

class RestApi:
    """
    An asgi application.
    """

    def __init__(self, resources):
        self.resources = resources
        self.routes = self.build_all_routes(resources)
        self.router = self.build_router(self.routes)


    async def __call__(self, scope, receive, send):
        request = Request(scope)
        (headers, body) = self.router(scope)
        await send(headers)
        await send(body)


        #Example from uvicorn
        #assert scope['type'] = 'http'
        #await send({
            #'type': 'http.response.start',
            #'status': 200,
            #'headers': [
                #[b'content-type', b'text/plain'],
            #],
        #})
        #await send({
            #'type': 'http.response.body',
            #'body': b'Hello, world!',
        #})

    @staticmethod
    def build_routes(resource)
        def acc_routes(resource):
            routes = deque([(resource.route, resource)])
            if resource.children is not []:
                children_routes = []
                for child in resource.children:
                    children_routes.append(acc_routes(child))
                # Make sure that children are evaluated first when pattern
                # matching. That's why we use a deque.
                routes.extendleft(children_routes)
            return routes
        return acc_routes(resource)

    @staticmethod
    def build_all_routes(resources):
        routes = []
        for resource in resources:
            routes.extend(build_routes(resource))
        return routes

    @staticmethod
    def build_router(routes):
        def router(request):
