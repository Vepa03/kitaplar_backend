from django.contrib import admin

from .models import Writer
from books.models import Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 1

class WriterAdmin(admin.ModelAdmin):
    list_display = ('id', 'username_tm', 'username_en', 'image')
    list_editable = ('username_tm', 'username_en', 'image')
    inlines = (BookInline, )
admin.site.register(Writer, WriterAdmin)
