from django.contrib import admin
from .models import Category, Blog, Comment, Tag

admin.site.register(Comment)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'created', 'views')
    prepopulated_fields = {'slug': ('title', )}