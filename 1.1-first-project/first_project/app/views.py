import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):

    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': '',
        'Показать содержимое рабочей директории': ''
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    # current_time = None
    msg = f'Текущее время: {datetime.datetime.now().time()}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    files = os.listdir()
    file_list = "\n".join(files)
    return HttpResponse(file_list)
    # raise NotImplemented
