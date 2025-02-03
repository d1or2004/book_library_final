from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'isbn', 'subtitle', 'price')
        read_only_fields = ('id',)

    def validate(self, data):
        title = data.get('title')
        author = data.get('author')

        # Harflardan iboratligini tekshirish
        if title and not title.isalpha():
            raise serializers.ValidationError('Title must contain only alphabetic characters')

        # Bazada mavjud bo'lgan sarlavha va muallifni tekshirish
        if title and author and Book.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError('Book with this title and author already exists')

        return data

    def validate_price(self, price):
        if price < 0 or price > 99999999999999:
            raise ValidationError({
                'price': 'Price must be between 0 and 99999999999999',
                'status': False
            })

    #  HAvfsiz usuli
# class CashSerializer(serializers.Serializer):
#     input = serializers.CharField(max_length=120)
#     output = serializers.CharField(max_length=120)
