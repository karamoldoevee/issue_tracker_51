# Generated by Django 2.2.5 on 2019-09-27 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(choices=[('other', 'Другое'), ('new', 'новая'), ('in_progress', 'в процессе'), ('done', 'выполнена')], default='other', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='webapp.Status', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='type',
            field=models.ForeignKey(choices=[('other', 'Другая'), ('task', 'Задача'), ('bug', 'ошибка'), ('enhancement', 'улучшение')], default='other', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='articles', to='webapp.Type', verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='status',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Название'),
        ),
    ]
