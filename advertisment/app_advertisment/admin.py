from django.contrib import admin
from .models import Advertisment
# Register your models here.

class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','auction','created_at','update_at']
    list_filter = ['auction','created_at']


admin.site.register(Advertisment, AdvertismentAdmin)