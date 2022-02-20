from wsgiref.simple_server import make_server
from my_framework.main import Framework
from urls import routes

application = Framework(routes)

with make_server('', 8000, application) as httpd:
    print('Запуск сервера на порту 8000...')
    print('http://127.0.0.1:8000/')
    httpd.serve_forever()

