from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Genre, Book


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        max_length=255,
        validators=[UniqueValidator(queryset=Genre.objects.all())]
    )

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    introduction = serializers.CharField(max_length=13, required=False)
    price = serializers.IntegerField(min_value=-32768, max_value=32767, required=False)
    image = serializers.ImageField(required=False, allow_null=True)
    address = serializers.CharField(max_length=255, required=False, allow_null=True, allow_blank=True)
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
        required=False,
        allow_null=True
    )

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.introduction = validated_data.get('introduction', instance.introduction)
        instance.price = validated_data.get('price', instance.price)
        instance.image = validated_data.get('image', instance.image)
        instance.address = validated_data.get('address', instance.address)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()
        return instance
