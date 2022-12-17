from rest_framework.decorators import api_view
from rest_framework.response import Response
from Brands.models import Brand
from .serializers import BrandSerializer
from rest_framework import status


@api_view(['Get'])
def getAllBrand(request):
    brands = Brand.objects.all()
    serializer = BrandSerializer(brands, many=True)
    return  Response(serializer.data)


@api_view(["GET"])
def getBrandById(request, pk):
    brand = Brand.objects.get(id=pk)
    serializer =BrandSerializer(brand, many=False)
    return  Response(serializer.data)


@api_view(["POST"])
def createBrand(request):
    serializer = BrandSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def updateBrand(request, pk):
    brand = Brand.objects.get(id=pk)
    serializer = BrandSerializer(brand, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return  Response(serializer.data, status=status.HTTP_200_OK)

    return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["DELETE"])
def deleteBrand(request, pk):
    brand = Brand.objects.get(id=pk)
    thumbnail = brand.thumbnail.path
    image = brand.image.path

    if brand:
        if brand.delete():
            brand.img_delete(image, thumbnail)
            return Response("Brand has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Brand with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)
