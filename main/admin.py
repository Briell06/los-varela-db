from django.contrib import admin
from .models import Categoria, Item, Combo


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    list_display = ("nombre", "precio", "categoria")
    list_filter = ("categoria",)
    search_fields = ("nombre", "descripcion")
    list_per_page = 10


@admin.register(Combo)
class ComboAdmin(admin.ModelAdmin):

    list_display = ("nombre", "precio")
    list_filter = ("items",)
    search_fields = ("nombre",)
    list_per_page = 10
