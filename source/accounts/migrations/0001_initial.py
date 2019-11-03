# Generated by Django 2.2.6 on 2019-11-01 14:57

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='user_pics', verbose_name='Аватар')),
                ('about_yourself', models.TextField(blank=True, max_length=1000, null=True, verbose_name='О себе')),
                ('github_profile', models.URLField(blank=True, max_length=250, null=True, verbose_name='Профиль ГитХаб')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]