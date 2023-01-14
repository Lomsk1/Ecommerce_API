from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from Products.models import ProductImages
from Products.serializers import ProductImageSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint returns Images by Product",
                     method="GET")
@api_view(["GET"])
def getImagesByProduct(request, product_id):
    image = ProductImages.objects.filter(product=product_id)
    serializer = ProductImageSerializer(image, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns all Images of  Product",
                     method="GET")
@api_view(["GET"])
def getAllImages(request):
    image = ProductImages.objects.all()
    serializer = ProductImageSerializer(image, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns Images by ID",
                     method="GET")
@api_view(["GET"])
def getImagesByID(request, pk):
    image = ProductImages.objects.get(id=pk)
    serializer = ProductImageSerializer(image, many=False)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint create Image",
                     method="POST",  request_body=ProductImageSerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
def createImage(request):
    serializer = ProductImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Change Images",
                     method="PUT",  request_body=ProductImageSerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def putImage(request, pk):
    image = ProductImages.objects.get(id=pk)
    serializer = ProductImageSerializer(image, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint returns Delete Image",
                     method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteImage(request, pk):
    images = ProductImages.objects.get(id=pk)
    image = images.image.path

    if images:
        if images.delete():
            images.img_delete(image)
            return Response("Image has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Image with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)
