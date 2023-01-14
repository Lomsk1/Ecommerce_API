from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from WeeklySales.models import WeeklySale
from WeeklySales.serializers import WeeklySaleSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint returns all Weekly Sales",
                     method="GET")
@api_view(['GET'])
def getAllWeekly(request):
    sale = WeeklySale.objects.all()
    serializer = WeeklySaleSerializer(sale, many=True)
    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns every Weekly Sales by ID",
                     method="GET")
@api_view(["GET"])
def getWeeklyById(request, pk):
    sale = WeeklySale.objects.get(id=pk)
    serializer =WeeklySaleSerializer(sale, many=False)
    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint create Weekly Sales",
                     method="POST",  request_body=WeeklySaleSerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
def createWeekly(request):
    serializer = WeeklySaleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint change Weekly Sales",
                     method="PUT", request_body=WeeklySaleSerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def updateWeekly(request, pk):
    sale = WeeklySale.objects.get(id=pk)
    serializer = WeeklySaleSerializer(sale, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint delete Weekly Sales",
                     method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteWeekly(request, pk):
    sale = WeeklySale.objects.get(id=pk)
    image = sale.image.path

    if sale:
        if sale.delete():
            sale.img_delete(image)
            return Response("Brand has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Brand with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)
