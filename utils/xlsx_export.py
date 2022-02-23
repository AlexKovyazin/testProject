from openpyxl import Workbook
from models import query_as_dict, Region, City, User
from settings import ROOT_DIR
import os


def generate_users_xlsx():
    workbook = Workbook()
    worksheet = workbook.active

    users_data = query_as_dict(User.get_users())
    headers = [key for key in users_data[0].keys()]

    worksheet.append(headers)

    for user in users_data:
        user_data = []
        # Заменяем id на названия
        region_id = user['region']
        city_id = user['city']
        user['region'] = Region.get_region_name_by_id(region_id)
        user['city'] = City.get_city_name_by_id(city_id)
        for key, value in user.items():
            user_data.append(value)
        worksheet.append(user_data)

    file_name = 'export_users.xlsx'
    file_path = os.path.join(ROOT_DIR, 'media', file_name)
    workbook.save(file_path)


def download_users_xlsx():
    pass


if __name__ == '__main__':
    generate_users_xlsx()
