from pyramid.config import Configurator
from pyramid.response import Response


def hello_world(request):
    return Response("Hello world form Pyramid!\n", content_type="text/plain")


config = Configurator()
config.add_route("hello", "/hellp")
config.add_view(hello_world, route_name="hello")
app = config.make_wsgi_app()
