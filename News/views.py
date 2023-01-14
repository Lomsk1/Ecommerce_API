from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from News.models import News
from News.serializers import NewsSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(operation_description="This endpoint returns all News", method="GET")
@api_view(['GET'])
def newsAll(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns News by ID", method="GET")
@api_view(['GET'])
def newsByID(request, pk):
    news = News.objects.get(id=pk)
    serializer = NewsSerializer(news, many=False)
    return Response(serializer.data)

@swagger_auto_schema(operation_description="This endpoint Create News", method="POST")
@api_view(['POST'])
@permission_classes([IsAdminUser])
def createNews(request):
    serializer = NewsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Change News", method="PUT")
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def changeNews(request, pk):
    news = News.objects.get(id=pk)
    serializer = NewsSerializer(news, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Delete News", method="DELETE")
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteNews(request, pk):
    news = News.objects.get(id=pk)
    image = news.image.path

    if news:
        if news.delete():
            news.img_delete(image)
            return Response("News has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)
    return Response("News with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)