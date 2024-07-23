from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Services
from .serializers import ProductSerializer, ServicesSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(
            product_name=data['product_name'],
            Business_name=data['Business_name'],
            description=data['description'],
            price=data['price']
        )
        return JsonResponse({
            'id': product.id,
            'product_name': product.product_name,
            'Business_name': product.Business_name,
            'description': product.description,
            'price': str(product.price)
        }, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


class ServicesListView(APIView):
    def get(self, request):
        services = Services.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ServicesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@csrf_exempt
def add_service(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        services = Services.objects.create(
            serviceName = data['serviceName'],
            description_ser = data['description_ser'],
            highestAmount = data['highestAmount'],
            location = data['location'],
            lowestAmount = data['lowestAmount'],
            serviceCategory = data['serviceCategory'],
            selectedEventTypes = data['selectedEventTypes'],
            selectedServices = data['selectedServices'],
            images = data['images'],
            videos = data['videos']
        )
        return JsonResponse({
            'serviceName' : services.serviceName,
            'description_ser':services.description_ser,
            'highestAmount':services.highestAmount,
            'location':services.location,
            'lowestAmount':services.lowestAmount,
            'serviceCategory':services.serviceCategory,
            'selectedEventTypes':services.selectedEventTypes,
            'selectedServices':services.selectedServices,
            'images':services.images,
            'videos':services.videos
        }, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
