from rest_framework.serializers import ModelSerializer

from core.models import Book


class BookSeriazlizer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        depth = 1
