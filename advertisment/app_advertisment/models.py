
from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

User = get_user_model()

class Advertisment(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    text = models.TextField('Текст')
    price = models.FloatField('Цена')
    #user = models.CharField('Пользователь', max_length=126)
    auction_test = models.BooleanField('торг', help_text='Возможен торг или нет', default=False)
    description = models.TextField('Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField('изображение', upload_to='advertisment/media')
    


    def __str__(self):
        return f'Advertisment(id = {self.user}, title = {self.title}, price = {self.price})'
    
    
    def get_absolute_urls(self):
        return reverse('adv-detail', kwargs= {'pk' : self.pk })


    @admin.display(description="дата создания")
    def created_date(self):
        from django.utils import timezone
        from django.utils.html import format_html

        if self.created_at.date() == timezone.now().date():
            create_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:green">Сегодня в {}</span>',create_time
            )
        return self.created_at.strftime('%d.%m.%Y in %H:%M:%S')

    @admin.display(description="дата обновления")
    def updated_date(self):
        from django.utils import timezone
        from django.utils.html import format_html

        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:purple">Сегодня в {}</span>',update_time
            )
        return self.update_at.strftime('%d.%m.%Y in %H:%M:%S')
    
    @admin.display(description='фото')
    def photo(self):
        from django.utils.html import format_html
        if self.image:
            return format_html(
                " <img src='{}' width = '100px' heigth = '100px' > ",
                self.image.url
            )
        return format_html(
            "<img src = 'http://127.0.0.1:8000/media/adv.png' width = '100px'> heigth = '100px' ",
            
        )



    class Meta:
        db_table = 'advertisment'