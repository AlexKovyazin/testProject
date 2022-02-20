def parse_input_data(data):
    result = {}
    if data:
        # Разделяем параметры
        params = data.split('&')
        for item in params:
            # Разделяем ключи и значения
            key, value = item.split('=')
            result[key] = value
    return result


class GetRequests:
    @staticmethod
    def get_request_params(environ):
        # Получаем параметры запроса
        query_string = environ['QUERY_STRING']
        # Преобразовываем в словарь
        request_params = parse_input_data(query_string)
        return request_params


class PostRequests:
    @staticmethod
    def get_wsgi_input_data(environ) -> bytes:
        content_length_data = environ['CONTENT_LENGTH']
        # Проверяем длину содержимого
        if content_length_data:
            content_length = int(content_length_data)
        else:
            content_length = 0
        # Считываем данные при наличии
        if content_length > 0:
            data = environ['wsgi.input'].read(content_length)
        else:
            data = b''
        return data

    @staticmethod
    def parse_wsgi_input_data(data):
        result = {}
        if data:
            data_str = data.decode(encoding='UTF-8')
            result = parse_input_data(data_str)
        return result

    def get_request_params(self, environ):
        data = self.get_wsgi_input_data(environ)
        data = self.parse_wsgi_input_data(data)
        return data
