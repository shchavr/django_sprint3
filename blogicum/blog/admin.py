from django.contrib import admin
from .models import Category, Post, Location

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Post)
