Test Project for interview

Запуск сервера осуществляется через файл run.py.
При запуске автоматически генерируется база данных sqlite скриптом utils.create_DB_script.sql.
Сервер запускается на порте 8000

http://127.0.0.1:8000/

Сгенерированные файлы сохраняются в директории media.

Для тестирования импорта из .xlsx файла в папку media добавлен файл users_for_import.xlsx.

Импорт из .pdf согласно заданию реализован на основе резюме. В связи с этим в функцию import_from_pdf модуля import необходимо передать путь к файлу.
