class PageNotFound:
    def __call__(self):
        return '404 Page not found :('


class Framework:
    def __init__(self, routes_obj):
        self.routes_lst = routes_obj

    def __call__(self, environ, start_response):
        # Получаем адрес, по которому перешел пользователь
        path = environ['PATH_INFO']

        # Добавляем закрывающий слэш
        if not path.endswith('/'):
            path = path + '/'

        # Получаем нужный контроллер
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound()

        # Запускаем контроллер
        code, body = view(request)
        start_response(
            code,
            [('Content-Type', 'text/html')]
        )
        return [body.encode('utf-8')]
