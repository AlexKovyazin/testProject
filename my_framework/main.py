import quopri
from my_framework.requests import GetRequests, PostRequests


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

        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequests().get_request_params(environ)
            request['data'] = data
        if method == 'GET':
            # Получаем параметры запроса и добавляем их в request
            request_params = GetRequests().get_request_params(environ)
            request['request_params'] = request_params

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

    @staticmethod
    def decode_value(data):
        """
        Заменяет quoted-printable символы запроса символами UTF-8
        :param data: dict
        :return: dict
        """
        decode_data = {}
        for key, value in data.items():
            replace_value = bytes(value.replace('%', '=').replace('+', ' '), 'UTF-8')
            decode_value = quopri.decodestring(replace_value).decode('UTF-8')
            decode_data[key] = decode_value
        return decode_data
