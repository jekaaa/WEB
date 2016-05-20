from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.wsgi import wsgiapp


def index(request):
    file = open('index.html', 'r')
    data = file.read()
    file.close()

    return Response(data)


def aboutme(request):
    file = open('about/aboutme.html', 'r')
    data = file.read()
    file.close()

    return Response(data)


class middleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        page = self.app(environ, start_response)[0].decode()
        top = '<div class=''top''>Middleware TOP</div>'
        bot = '<div class=''bottom''>Middleware BOTTOM</div>'
        head, body = page.split('<body>')
        data, end = bodyHtml.split('</body>')
        data = '<body>' + top + data + bot + '</body>'
        return head.encode() + data.encode() + end.encode()


if __name__ == '__main__':
    config = Configurator()
    config.add_route('default', '/')
    config.add_view(index, route_name='default')
    config.add_route('index', '/index.html')
    config.add_view(index, route_name='index')
    config.add_route('aboutme', '/about/aboutme.html')
    config.add_view(aboutme, route_name='aboutme')

    app = config.make_wsgi_app()
    wsgi_app = middleware(app)

    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()
