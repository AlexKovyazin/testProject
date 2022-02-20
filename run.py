import os
import sqlite3
from wsgiref.simple_server import make_server
from my_framework.main import Framework
from urls import routes

db_path = os.path.join(os.getcwd(), 'testDB.sqlite3')
# Проверяем наличие БД в проекте
if not os.path.exists(db_path):
    # Создаем БД скриптом
    connection = sqlite3.connect('testDB.sqlite3')
    cursor = connection.cursor()
    with open(os.path.join(os.getcwd(), 'utils', 'create_DB_script.sql'), encoding='utf-8') as file:
        sql_script = file.read()
        cursor.executescript(sql_script)

# Запускаем сервер
application = Framework(routes)
with make_server('', 8000, application) as httpd:
    print('Запуск сервера на порту 8000...')
    print('http://127.0.0.1:8000/')
    httpd.serve_forever()
