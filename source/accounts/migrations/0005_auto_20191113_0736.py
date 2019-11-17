# Generated by Django 2.2.6 on 2019-11-13 07:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191113_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='work_finished',
            field=models.DateTimeField(default=None, verbose_name='Окончание работы'),
        ),
        migrations.AddField(
            model_name='team',
            name='work_started',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Начало работы'),
            preserve_default=False,
        ),
    ]