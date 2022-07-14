from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Таблица качеств компании
class Point(models.Model):
    title = models.CharField('Заголовок', max_length=20)
    textfield = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пункт"
        verbose_name_plural = "Пункты"

# Таблица сообщений
class userMessage(models.Model):
    username = models.CharField('ФИО', max_length=50)
    email = models.EmailField('Email')
    phone = models.CharField('Номер телефона', max_length=20)
    textfield = models.TextField('Описание', max_length=500)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

# Таблица новостей
class News(models.Model):
    title = models.CharField('Название статьи', max_length=100, unique=True)
    text = models.TextField('Текст статьи')
    date = models.DateTimeField('Дата', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    views = models.IntegerField('Просмотры', default=1)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'