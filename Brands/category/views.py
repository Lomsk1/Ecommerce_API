from rest_framework.decorators import api_view
from rest_framework.response import Response
from Brands.models import BrandCategories
from Brands.serializers import BrandCategorySerializer
from rest_framework import status

from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

@api_view(["GET"])
def getCategoriesByBrand(request, brand_id):
    categories = BrandCategories.objects.filter(brands=brand_id)
    serializer = BrandCategorySerializer(categories, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def getAllBrandCategory(request):
    categories = BrandCategories.objects.all()
    serializer = BrandCategorySerializer(categories, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def getBrandCategory(request, pk):
    categories = BrandCategories.objects.get(id=pk)
    serializer = BrandCategorySerializer(categories, many=False)

    return Response(serializer.data)


@api_view(["POST"])
def createBrandCategory(request):
    serializer = BrandCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def putBrandCategory(request, pk):
    category = BrandCategories.objects.get(id=pk)
    serializer = BrandCategorySerializer(category, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def deleteBrandCategory(request, pk):
    category = BrandCategories.objects.get(id=pk)

    if category:
        if category.delete():
            return Response("Brand Category has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Brand Category with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)
