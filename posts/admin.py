from django.contrib import admin
from posts.models import Post


@admin.register(Post)
class Category(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at', 'published']
