from rest_framework import serializers

from .models import Writer
from books.serializers import BookForWriterSerializer


class WriterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Writer
        fields = ['id', 'username_tm', 'image']


class WriterRetrieveSerializer(serializers.ModelSerializer):
    books = BookForWriterSerializer(many=True)
    
    class Meta:
        model = Writer
        fields = ['id', 'username_tm', 'image', 'books']
