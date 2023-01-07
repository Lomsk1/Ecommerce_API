from rest_framework.decorators import api_view
from rest_framework.response import Response
from Products.models import Product
from Products.serializers import ProductSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint returns all limited Product", method="GET")
@api_view(['GET'])
def getAllLimitProduct(request, limit):
    product = Product.objects.all()[:limit]
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)

@swagger_auto_schema(operation_description="This endpoint returns all Product", method="GET")
@api_view(['GET'])
def getAllProduct(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns every Product by ID",
                     method="GET")
@api_view(["GET"])
def getProductById(request, pk):
    product = Product.objects.get(id=pk)
    serializer =ProductSerializer(product, many=False)
    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint create Product",
                     method="POST",  request_body=ProductSerializer)
@api_view(["POST"])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(operation_description="This endpoint change Product",
                     method="PUT", request_body=ProductSerializer)
@api_view(["PUT"])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint delete Product", method="DELETE")
@api_view(["DELETE"])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    thumbnail = product.thumbnail.path

    if product:
        if product.delete():
            product.img_delete(thumbnail)
            return Response(f"Product with ID {pk} has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Product with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)
