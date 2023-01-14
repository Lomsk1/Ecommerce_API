from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from Brands.models import BrandCategories
from Brands.serializers import BrandCategorySerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint returns Categories by Brands", method="GET")
@api_view(["GET"])
def getCategoriesByBrand(request, brand_id):
    categories = BrandCategories.objects.filter(brands=brand_id)
    serializer = BrandCategorySerializer(categories, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns all Brand Category", method="GET")
@api_view(["GET"])
def getAllBrandCategory(request):
    categories = BrandCategories.objects.all()
    serializer = BrandCategorySerializer(categories, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns Brand Category by ID", method="GET")
@api_view(["GET"])
def getBrandCategory(request, pk):
    categories = BrandCategories.objects.get(id=pk)
    serializer = BrandCategorySerializer(categories, many=False)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint create Brand Category",
                     method="POST",  request_body=BrandCategorySerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
def createBrandCategory(request):
    serializer = BrandCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Change Brand Category",
                     method="PUT",  request_body=BrandCategorySerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def putBrandCategory(request, pk):
    category = BrandCategories.objects.get(id=pk)
    serializer = BrandCategorySerializer(category, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint returns Delete Brand Category",
                     method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteBrandCategory(request, pk):
    category = BrandCategories.objects.get(id=pk)

    if category:
        if category.delete():
            return Response("Brand Category has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Brand Category with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)
