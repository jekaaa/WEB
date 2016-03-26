import socket

HOST,PORT = '',8000
bufSize = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST,PORT))
s.listen(1)

while (True):
    connection,address = s.accept()
    request = str(connection.recv(bufSize))
    path = request.split('\n')[0].split(' ')[1]
    path = path[1:]
    if (path == '' or path == 'index.html'):
        path == 'index.html'
        file = open(path,'rb')
    if (path == 'about/aboutme.html'):
        file = open(path,'rb')
    response = """\
HTTP/1.1 200 OK
Content-Type: text/html



""" + str(file.read())
    connection.send(response.encode())
    
    connection.close()
s.close()


