from django.contrib import admin
from .models import Advertisment

# Register your models here.

class AdvertismentAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','price','auction_test','created_date', 'updated_date', 'photo']
    list_filter = ['auction_test','created_at']
    auction = ['make_auction_as_false']
    # fieldsets = (
    #     (   
    #         'Общее',
    #         {
    #             'fields':('title',"description")
    #         }
    #     ),
    #     (   
    #         'Финансы',
    #         {
    #             'fields':('price','auction_test'),
    #             'classes':['collapse']
    #         }
    #     ),
    # )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_false(self, request, queryset): 
        queryset.update(auction = True)

    



admin.site.register(Advertisment, AdvertismentAdmin)