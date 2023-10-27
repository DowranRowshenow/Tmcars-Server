from rest_framework import viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from .models import Category, Location, Product
from .serializers import CategorySerializer, LocationSerializer, ProductSerializer


class CategoryViewSet(viewsets.ViewSet):
    # CUSTOM FILTERS
    def get_queryset(self):
        name = self.request.query_params.get("name", "")
        limit = self.request.query_params.get("limit", "")
        limit = abs(int(limit)) if limit.isdigit() else None

        queryset = Category.objects.filter(name__contains=name).order_by("id")[:limit]

        return queryset

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class LocationViewSet(viewsets.ViewSet):
    # CUSTOM FILTERS
    def get_queryset(self):
        name = self.request.query_params.get("name", "")
        limit = self.request.query_params.get("limit", "")
        limit = abs(int(limit)) if limit.isdigit() else None

        queryset = Location.objects.filter(name__contains=name).order_by("id")[:limit]

        return queryset

    @extend_schema(responses=LocationSerializer)
    def list(self, request):
        serializer = LocationSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    # CUSTOM FILTERS
    def get_queryset(self):
        name = self.request.query_params.get("name", "")
        location = self.request.query_params.get("location", "")
        category = self.request.query_params.get("category", "")
        price_min = self.request.query_params.get("price_min", "")
        price_max = self.request.query_params.get("price_max", "")
        require_image = self.request.query_params.get("require_image", "")
        limit = self.request.query_params.get("limit", "")

        price_min = abs(float(price_min)) if price_min.isdigit() else float()
        price_max = abs(float(price_max)) if price_max.isdigit() else float(10**6)
        limit = abs(int(limit)) if limit.isdigit() else None

        queryset = Product.objects.filter(
            name__contains=name,
            location__name__contains=location,
            category__name__contains=category,
            price__gte=price_min,
            price__lte=price_max,
        ).order_by("id")[:limit]

        return queryset

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)
