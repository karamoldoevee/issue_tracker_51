from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')

    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')

    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')

    about_yourself = models.TextField(max_length=1000, null=True, blank=True, verbose_name='О себе')

    github_profile = models.URLField(max_length=250, null=True, blank=True, verbose_name='Профиль ГитХаб')

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'

        verbose_name_plural = 'Профили'
