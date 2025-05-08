from rest_framework import serializers

from .models import Book


class BooksListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title_tm', 'image', 'writer', 'file']


class BookForWriterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title_tm', 'image', 'writer', 'file']
