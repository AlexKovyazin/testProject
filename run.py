import os
import sqlite3
from sqlalchemy.exc import NoSuchTableError
from wsgiref.simple_server import make_server
from my_framework.main import Framework
from settings import ROOT_DIR

# При запуске run.py сначала происходит импортирование всех модулей.
# В urls.py импортируется класс Index,
# использующий функцию get_total(), которая обращается к БД.
# При отсутствии БД необходимо обработать событие отсутствия таблиц
try:
    from urls import routes
except NoSuchTableError:
    # Создаем БД скриптом
    connection = sqlite3.connect('testDB.sqlite3')
    cursor = connection.cursor()
    with open(os.path.join(ROOT_DIR, 'utils', 'create_DB_script.sql'), encoding='utf-8') as file:
        sql_script = file.read()
        cursor.executescript(sql_script)

finally:
    from urls import routes

# Запускаем сервер
application = Framework(routes)
with make_server('', 8000, application) as httpd:
    print('Запуск сервера на порту 8000...')
    print('http://127.0.0.1:8000/')
    httpd.serve_forever()
