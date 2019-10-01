from django.db import models
import datetime
from django.db import models

class Issue(models.Model):

    summary = models.CharField(max_length=100, blank=False, verbose_name='Краткое описание')

    description = models.TextField(max_length=2000, blank=True, verbose_name='Описание')

    status = models.ForeignKey('Status', on_delete=models.PROTECT, verbose_name='Категория', related_name='articles')

    type = models.ForeignKey('Type', on_delete=models.PROTECT, verbose_name='Тип', related_name='articles')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.summary

class Status(models.Model):

    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name

class Type(models.Model):

    name = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.name
