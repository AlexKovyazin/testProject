from openpyxl import Workbook
from models import query_as_dict, Region, City, User
from settings import ROOT_DIR
import os


def collect_users_data():
    """
    Собирает данные о пользователях из БД.
    :return: [{headers}, {user1}, {user2}...]
    """
    result = []
    users_data = query_as_dict(User.get_users())
    headers = [key for key in users_data[0].keys()]
    # Записываем названия столбцов первым элементом
    result.append(headers)

    for user in users_data:
        user_data = []
        # Заменяем id на названия
        region_id = user['region']
        city_id = user['city']
        user['region'] = Region.get_region_name_by_id(region_id)
        user['city'] = City.get_city_name_by_id(city_id)
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

    for el in data:
        worksheet.append(el)

    file_name = 'export_users.xlsx'
    file_path = os.path.join(ROOT_DIR, 'media', file_name)
    workbook.save(file_path)


def download_users_xlsx():
    pass
