from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        permission_classes = [IsAuthenticated]