from rest_framework.decorators import api_view
from rest_framework.response import Response
from Category.models import Category
from Category.serializers import CategorySerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint returns all Category", method="GET")
@api_view(['GET'])
def getAllCategory(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

@swagger_auto_schema(operation_description="This endpoint returns Category by ID", method="GET")
@api_view(['GET'])
def getCategoryByID(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint Create Category", method="POST",
                     request_body=CategorySerializer)
@api_view(['POST'])
def createCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Change Category", method="PUT",
                     request_body=CategorySerializer)
@api_view(['PUT'])
def changeCategory(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Delete Category by ID", method="DELETE")
@api_view(['DELETE'])
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    image = category.image.path

    if category:
        category.img_delete(image)
        if category.delete():
            return Response("Category has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Category with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)



