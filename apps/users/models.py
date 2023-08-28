from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(
        max_length=100,
        verbose_name='Имя пользователя'
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
        auto_now=True,
        verbose_name='Создано'
    )
    age = models.IntegerField(
        verbose_name='Возраст'
    )
    wallet_adress = models.CharField(
        max_length=12,
        verbose_name='Кошелек'
    )

    def __str__(self):
        return self.user_name
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"