from wsgiref.simple_server import make_server
from my_framework.main import Framework
from urls import routes

application = Framework(routes)

with make_server('', 8000, application) as httpd:
    print('Сервер запущен на порту 8000')
    httpd.serve_forever()

