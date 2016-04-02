from waitress import serve

TOP =  "<div class='top'>Middleware TOP</div>"
BOTTOM = "<div class='botton'>Middleware BOTTOM</div>"


class Middleware(object):
 	def __init__(self, app):
 		self.app = app
 	def __call__(self, environ, start_responce):
 		response = self.app(environ, start_responce)[0].decode()

 		if (response.find('<body>') != -1):
 			head,body = response.split('<body>')
 			bodytext,end = body.split('</body>')
 			bodytext = '<body>' + TOP + bodytext + BOTTOM + '</body>'
 			return [head.encode() + bodytext.encode() + end.encode()]
 		else:
 			return [TOP + response.encode() + BOTTOM]
 		
def app(environ, start_responce):
        start_responce('200 OK', [('Content-Type', 'text/html')])
        path = environ['PATH_INFO']
        path = path[1:]
        if (path == ''):
                path = 'index.html'
        file = open(path,'r')
        return [file.read().encode()]

app = Middleware(app)
serve(app, host = '', port = 8000)
