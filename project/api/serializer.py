from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['full_name', 'birth_year', 'address', 'course']
        # exclude = ['image']
        # depth = 1
        # read_only_fields = ['phone_number']
        extra_kwargs = {'image': {'write_only': True}}