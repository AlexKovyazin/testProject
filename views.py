from my_framework.templator import render
from models import get_total, get_regions, get_region_cities


class Index:

    def __call__(self, request):
        regions_list = get_regions()

        return '200 OK', render('index.html',
                                users_list=get_total(),
                                regions_list=regions_list)


class RegionCities:

    def __call__(self, request):
        # Получаем id региона из запроса
        region_id = request['data']['id']
        # Собираем города региона из БД
        cities_list = get_region_cities(region_id)

        # Готовим данные для загрузки в <select> методом .load в ajax.js
        options = '<option selected disabled>Выберите город</option>'
        for city in cities_list:
            options += f"<option value='{city.id}'>{city.city_name}</option>"

        return '200 OK', options
