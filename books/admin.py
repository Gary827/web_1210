from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name']
    list_filter = ['price', 'name']

admin.site.register(Book, BookAdmin)