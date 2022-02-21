from my_framework.templator import render
from models import Region, get_total, get_regions


class Index:
    def __call__(self, request):
        regions_list = get_regions()

        return '200 OK', render('index.html',
                                users_list=get_total(),
                                regions_list=regions_list)


class RegionCities:
    def __call__(self, request):
        pass
