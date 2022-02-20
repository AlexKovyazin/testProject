import quopri
import os
from my_framework.requests import GetRequests, PostRequests
from utils.content_types import CONTENT_TYPES
from settings import STATIC_URL, STATIC_FILES_DIR


class PageNotFound:
    def __call__(self, request):
        return '404 Page not found', '404 Page not found :('


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
        if path.startswith(STATIC_URL):
            # Получаем путь к файлу из директории статики
            file_path = path[len(STATIC_URL):len(path) - 1]
            # Получаем content type из файла
            content_type = self.get_content_type(file_path)
            code, body = self.get_static(STATIC_FILES_DIR, file_path)
        else:
            if path in self.routes_lst:
                view = self.routes_lst[path]
            else:
                view = PageNotFound()

            code, body = view(request)
            body = body.encode('UTF-8')
            content_type = self.get_content_type(path)

        start_response(
            code,
            [('Content-Type', content_type)]
        )
        return [body]

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

    @staticmethod
    def get_content_type(file_path, content_types=CONTENT_TYPES):
        file_name = os.path.basename(file_path)
        extension = os.path.splitext(file_name)[1]
        return content_types.get(extension, 'text/html')

    @staticmethod
    def get_static(static_dir, file_path):
        path_to_file = os.path.join(static_dir, file_path)
        with open(path_to_file, 'rb') as file:
            file_content = file.read()
        code = '200 OK'
        return code, file_content

