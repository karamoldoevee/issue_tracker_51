# Generated by Django 2.2.6 on 2019-11-03 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0005_auto_20191008_2025'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_started', models.DateTimeField(auto_now_add=True, verbose_name='Начало работы')),
                ('work_finished', models.DateTimeField(auto_now_add=True, verbose_name='Окончание работы')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='team', to='webapp.Project', verbose_name='Проект')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Команда',
                'verbose_name_plural': 'Команда',
            },
        ),
    ]