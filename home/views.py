from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Point, News
from .forms import MessageForm


def uslugi(request):
    data = {'points': Point.objects.all(), 'title':'Услуги', 'topic':'Страница с услугами'}
    return render(request, 'home/uslugi.html', data)

def about(request):
    return render(request, 'home/about.html', {'title':'О нас', 'topic':'Немного поговорим о нас'})


# Отправка сообщения в админку
def inputMessage(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Сообщение отправлено')
            return redirect('contact')
    else:
        form = MessageForm()

    return render(
        request,
        'home/contact.html',
        {
            'title': 'Контакты',
            'form': form
        }
    )


# Получение новостей из БД
def home(request):
    data = {
        'news': News.objects.all(),
        'title': 'Главная страница!',
        'topic':'Простой и удобный сервис'
    }

    return render(request, 'home/home.html', data)
