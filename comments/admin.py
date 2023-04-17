from django.contrib import admin
from comments.models import Comment


@admin.register(Comment)
class Category(admin.ModelAdmin):
    list_display = ['content', 'user','post', 'created_at']
