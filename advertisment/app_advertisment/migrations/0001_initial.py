# Generated by Django 4.2.3 on 2023-07-22 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('user', models.CharField(max_length=126, verbose_name='Пользователь')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
        ),
    ]
