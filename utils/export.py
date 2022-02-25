import os
import comtypes.client
from openpyxl import Workbook
from models import query_as_dict, Region, City, User
from settings import ROOT_DIR
from PyPDF2 import PdfFileMerger
from docxtpl import DocxTemplate


def generate_users_resume():
    """
    Формирует .pdf файл на основании данных таблицы users.
    Генерация файлов выполняется функциями
    generate_docx_resume и generate_pdf_resume
    :return: str Путь к сгенерированному .pdf файлу
    """
    pdf_files = []
    outfile = os.path.join(ROOT_DIR, 'media', 'users_resume.pdf')

    for user in query_as_dict(User.get_users()):
        # Генерируем .pdf файл и присваиваем переменной путь к файлу
        pdf = generate_pdf_resume(user)
        pdf_files.append(pdf)

    # Объединяем все сгенерированные pdf файлы
    merger = PdfFileMerger()
    for file in pdf_files:
        merger.append(file)
    merger.write(outfile)
    merger.close()
    # Удаляем все файлы кроме итогового
    for file in pdf_files:
        os.remove(file)
    return outfile


def generate_pdf_resume(user_data: dict):
    """
    Формирует .docx файл резюме сделанный по .docx шаблону
    на основании данных user_data и конвертирует в pdf.
    Работает только для Windows, должен быть установлен Microsoft Office!
    :param user_data: dict Словарь с данными пользователя,
    где ключами являются название столбца БД
    :return: str Путь к сгенерированному .pdf файлу
    """
    # Генерируем .docx файл и присваиваем переменной путь к файлу
    in_file = generate_docx_resume(user_data)
    out_file = os.path.splitext(in_file)[0] + '.pdf'

    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=17)
    doc.Close()
    word.Quit()
    os.remove(in_file)  # Удаляем не нужный .docx файл
    return out_file


def generate_docx_resume(user_data: dict):
    """
    Формирует .docx файл резюме сделанный по .docx шаблону
    на основании данных user_data
    :param user_data: dict Словарь с данными пользователя
    :return: str Путь к сгенерированному .docx файлу
    """
    second_name = user_data['second_name']
    first_name = user_data['first_name']
    patronymic = user_data['patronymic']
    city_id = user_data['city']
    phone = user_data['phone']
    email = user_data['email']
    city = City.get_city_name_by_id(city_id)

    template_name = 'resume_template.docx'
    doc = DocxTemplate(os.path.join(ROOT_DIR, 'media', 'templates', template_name))
    context = {
        'second_name': second_name,
        'first_name': first_name,
        'patronymic': patronymic,
        'city': city,
        'phone': phone,
        'email': email
    }
    doc.render(context)
    out_file = os.path.join(ROOT_DIR, 'media', f"user-{user_data['id']}.docx")
    doc.save(out_file)
    return out_file


def collect_users_data():
    """
    Собирает данные о пользователях из БД.
    :return: [{user1}, {user2}...]
    """
    result = []
    users_data = query_as_dict(User.get_users())

    for user in users_data:
        user_data = []
        # Заменяем id на названия
        region_id = user['region']
        city_id = user['city']
        try:  # В БД может отсутствовать город/регион пользователя
            user['region'] = Region.get_region_name_by_id(region_id)
        except AttributeError:
            user['region'] = None
        try:
            user['city'] = City.get_city_name_by_id(city_id)
        except AttributeError:
            user['city'] = None

        for key, value in user.items():
            user_data.append(value)
        result.append(user_data)

    return result


def generate_xlsx(data):
    """
    Генерирует .xlsx файл на основании переданных в data данных.
    :param data: Список, где каждый элемент - вложенный список.
    Каждый список записывается в новой строке.
    Каждый элемент списка записывается в отдельный столбец.
    :return: None
    """
    workbook = Workbook()
    worksheet = workbook.active

    headers = User.get_headers()
    worksheet.append(headers)

    for el in data:
        worksheet.append(el)

    file_name = 'export_users.xlsx'
    file_path = os.path.join(ROOT_DIR, 'media', file_name)
    workbook.save(file_path)

    return file_path


def download_users_xlsx():
    pass


if __name__ == '__main__':
    pass
    # generate_users_resume()  # Генерирует .xlsx файл по таблице users
    # generate_xlsx(collect_users_data())  # Генерирует .pdf файл с резюме по таблице users
