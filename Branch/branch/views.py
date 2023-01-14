from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from Branch.models import Branch
from Branch.serializers import BranchSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@swagger_auto_schema(operation_description="This endpoint returns all Branch",
                     method="GET")
@api_view(['GET'])
def getAllBranch(request):
    branch = Branch.objects.all()
    serializer = BranchSerializer(branch, many=True)

    return Response(serializer.data)

@swagger_auto_schema(operation_description="This endpoint returns Branch by ID",
                     method="GET")
@api_view(['GET'])
def getBranchByID(request, pk):
    branch = Branch.objects.get(id=pk)
    serializer = BranchSerializer(branch, many=False)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint create Branch",
                     method="POST",  request_body=BranchSerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
def createBranch(request):
    serializer = BranchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Change Branch",
                     method="PUT",  request_body=BranchSerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def putBranch(request, pk):
    branch = Branch.objects.get(id=pk)
    serializer = BranchSerializer(branch, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Delete Branch",
                     method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteBranch(request, pk):
    branch = Branch.objects.get(id=pk)

    if branch:
        if branch.delete():
            return Response(f"Branch ID {pk} has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Branch with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)