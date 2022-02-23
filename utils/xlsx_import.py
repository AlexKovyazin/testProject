import os
from openpyxl import load_workbook
from models import get_regions, get_cities, Region, City, User
from settings import ROOT_DIR


def import_from_xlsx(path_to_file):
    workbook = load_workbook(path_to_file)
    worksheet = workbook.active

    headers_list = worksheet[worksheet.min_row]
    # Необходим для сопоставления названия колонок
    headers = {i: cell.value for i, cell in enumerate(headers_list)}
    body = worksheet[worksheet.min_row + 1: worksheet.max_row]

    # Собираем данные из таблицы в словари и добавляем в users_data
    users_data = []
    for row in body:
        user_dict = {}
        for i, cell in enumerate(row):
            # Используем headers для правильного распределения значений по столбцам
            user_dict[headers[i]] = cell.value
        # Заменяем названия на id
        region_name = user_dict['region']
        city_name = user_dict['city']
        user_dict['region'] = Region.get_region_id_by_name(region_name)
        user_dict['city'] = City.get_city_id_by_name(city_name)
        users_data.append(user_dict)

    for user in users_data:
        new_user = User(**user)
        new_user.create_user()


if __name__ == '__main__':
    file = os.path.join(ROOT_DIR, 'media', 'users_for_import.xlsx')
    import_from_xlsx(file)
