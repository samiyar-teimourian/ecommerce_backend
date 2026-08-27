from django.shortcuts import get_object_or_404
from .models import product
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(["GET"])
def prod(request ,id):
    productt = get_object_or_404(product, id=id)
    return Response({
        "id": productt.id,
        "name": productt.name,
        "price": productt.price,
    })
@api_view(["GET"])
def products(request):
    product_list = list(product.objects.all().values())
    return Response({"productlist": product_list})