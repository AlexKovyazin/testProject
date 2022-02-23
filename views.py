from my_framework.main import Framework
from my_framework.templator import render
from models import get_total, get_regions, get_region_cities, replace_none, User
from utils.xlsx_export import generate_xlsx, collect_users_data


class Index:

    def __call__(self, request):
        if request['method'] == 'POST':
            raw_user_data = Framework.decode_value(request['data'])
            user_data = {}

            for key, value in raw_user_data.items():
                if value == '':
                    user_data[key] = None
                else:
                    user_data[key] = value

            new_user = User(**user_data)
            new_user.create_user()

        regions_list = get_regions()

        return '200 OK', render('index.html',
                                users_list=replace_none(get_total()),
                                regions_list=regions_list)


class RegionCities:

    def __call__(self, request):
        # Получаем id региона из запроса
        region_id = request['data']['id']
        # Собираем города региона из БД
        cities_list = get_region_cities(region_id)

        # Готовим данные для загрузки в <select> методом .load в ajax
        options = '<option selected disabled>Выберите город</option>'
        for city in cities_list:
            options += f"<option value='{city.id}'>{city.city_name}</option>"

        return '200 OK', options


class DownloadUsersXlsx:

    def __call__(self, request):
        users_data = collect_users_data()
        generate_xlsx(users_data)
        return '200 OK', render('index.html',
                                users_list=replace_none(get_total()),
                                regions_list=get_regions())
