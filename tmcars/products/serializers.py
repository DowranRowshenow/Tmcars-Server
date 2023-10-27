from rest_framework import serializers

from .models import Category, Location, Product
from images.serializers import ImageSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    images = ImageSerializer(read_only=True, many=True)
    location = LocationSerializer()

    class Meta:
        model = Product
        fields = "__all__"
