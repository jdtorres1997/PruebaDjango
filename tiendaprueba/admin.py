from django.contrib import admin
from .models import Product
from .models import Favorite
# Register your models here.

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
	list_display = ('nombre', 'categoria', 'descripcion', 'precio')

@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
	list_display = ('user', 'product')
	