from my_framework.templator import render
from models import get_total


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', objects_list=get_total())
