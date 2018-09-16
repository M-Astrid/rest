from django.contrib import admin

# Register your models here.

from .models import Dish


class DishAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dish, DishAdmin)
