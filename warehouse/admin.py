from django.contrib import admin
from .models import MainCategory, Category, Position, CategoryValue

# Register your models here.
admin.site.register(MainCategory)
admin.site.register(Category)
admin.site.register(Position)
admin.site.register(CategoryValue)