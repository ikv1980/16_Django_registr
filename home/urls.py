from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('uslugi', views.uslugi, name='uslugi'),
    # path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('contact', views.inputMessage, name="contact"),
]
