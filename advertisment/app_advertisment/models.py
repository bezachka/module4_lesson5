from django.db import models

# Create your models here.

class Advertisment(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    text = models.TextField('Текст')
    price = models.FloatField('Цена')
    user = models.CharField('Пользователь', max_length=126)
    date = models.DateField('Дата', auto_now_add=True)


    def __str__(self):
        return f'Advertisment(id = {self.id}, title = {self.title}, price = {self.price})'
    

    class Meta:
        db_table = 'advertisment'