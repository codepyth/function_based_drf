from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


# class ProductList(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

@api_view(['POST'])
def productCreate(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # return Response('Fill the fields')


@api_view(['GET'])
def productDetail(request, pk):
    try:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except:
        return Response('No Records Found', status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def productUpdate(request, pk):
    try:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=request.data)
        if request.method == 'PUT':
            if serializer.is_valid():
                serializer.save()
                return Response(request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response('Nothing found', status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def productDelete(pk):
    try:
        obj = Product.objects.get(id=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response('This is already deleted!')
        # return Response(status=status.HTTP_404_NOT_FOUND)
