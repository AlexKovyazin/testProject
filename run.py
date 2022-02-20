import os
import sqlite3
from wsgiref.simple_server import make_server
from my_framework.main import Framework
from urls import routes
from settings import DB_PATH, ROOT_DIR


# Проверяем наличие БД в проекте
if not os.path.exists(DB_PATH):
    # Создаем БД скриптом
    connection = sqlite3.connect('testDB.sqlite3')
    cursor = connection.cursor()
    with open(os.path.join(ROOT_DIR, 'utils', 'create_DB_script.sql'), encoding='utf-8') as file:
        sql_script = file.read()
        cursor.executescript(sql_script)

# Запускаем сервер
application = Framework(routes)
with make_server('', 8000, application) as httpd:
    print('Запуск сервера на порту 8000...')
    print('http://127.0.0.1:8000/')
    httpd.serve_forever()
