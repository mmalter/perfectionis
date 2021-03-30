from perfectionis.resource import Resource

class StaticSingleResource(Resource):
    """
    A simple endpoint for static resources.
    """
    def __init__(self, name):
        super.__init__(name)
