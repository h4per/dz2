from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    name = models.CharField(
        max_length=50,
        verbose_name='Имя пользователя',
        default=''
    )
    email = models.EmailField(
        max_length=100,
        verbose_name='Email'
    )
    phone_number = models.CharField(
        max_length=100,
        verbose_name='Номер телефона'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )
    age = models.PositiveIntegerField(
        verbose_name='Возраст',
        blank=True,
        null=True
    )
    wallet_adress = models.CharField(
        max_length=12,
        verbose_name='Кошелек'
    )

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
