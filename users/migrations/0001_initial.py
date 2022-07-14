# Generated by Django 4.0.5 on 2022-07-06 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='default.png', upload_to='user_images', verbose_name='Фото пользователя')),
                ('gender', models.CharField(choices=[('N', 'Не указан'), ('M', 'Мужской'), ('F', 'Женский')], default='N', max_length=1, verbose_name='Пол пользователя')),
                ('agreement', models.BooleanField(default=True, verbose_name='Согласие пользователя')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профайл',
                'verbose_name_plural': 'Профайлы',
            },
        ),
    ]
