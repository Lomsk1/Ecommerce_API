from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from Branch.models import BranchCoord
from Branch.serializers import BranchCoordSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@swagger_auto_schema(operation_description="This endpoint returns all Branch Coord",
                     method="GET")
@api_view(['GET'])
def getAllBranchCoord(request):
    coord = BranchCoord.objects.all()
    serializer = BranchCoordSerializer(coord, many=True)

    return Response(serializer.data)

@swagger_auto_schema(operation_description="This endpoint returns Branch Coord by ID",
                     method="GET")
@api_view(['GET'])
def getBranchCoordByID(request, pk):
    coord = BranchCoord.objects.get(id=pk)
    serializer = BranchCoordSerializer(coord, many=False)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns BranchCoord by Branch",
                     method="GET")
@api_view(['GET'])
def getBranchCoordByBranch(request, branch_id):
    coord = BranchCoord.objects.filter(branch=branch_id)
    serializer = BranchCoordSerializer(coord, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint create Branch Coord",
                     method="POST",  request_body=BranchCoordSerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
def createBranchCoord(request):
    serializer = BranchCoordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Change Branch Coord",
                     method="PUT",  request_body=BranchCoordSerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def putBranchCoord(request, pk):
    coord = BranchCoord.objects.get(id=pk)
    serializer = BranchCoordSerializer(coord, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Delete Branch Coord",
                     method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteBranchCoord(request, pk):
    coord = BranchCoord.objects.get(id=pk)

    if coord:
        if coord.delete():
            return Response("Branch Coord has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Branch Coord with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)