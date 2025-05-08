from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_tm', 'title_en', 'image', 'writer', 'file')
    list_editable = ('title_tm', 'title_en', 'image', 'writer', 'file')

admin.site.register(Book, BookAdmin)
