# Generated by Django 4.2.4 on 2023-08-29 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=50, verbose_name='Имя пользователя'),
        ),
    ]