from django.contrib import admin
from .models import Car
# Register your models here.

class CarAdmin(admin.ModelAdmin):
	list_display =('car_tittle','color','year','body_style','fuel_type','is_featured')
	list_editable = ('is_featured',)
	search_fields = ('car_tittle','color','year','body_style','body_style',)


admin.site.register(Car, CarAdmin)
