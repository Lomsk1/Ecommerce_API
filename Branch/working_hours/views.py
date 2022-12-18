from rest_framework.decorators import api_view
from rest_framework.response import Response
from Branch.models import BranchWorkingHours
from Branch.serializers import BranchWorkingHoursSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint returns all Branch Working hours",
                     method="GET")
@api_view(['Get'])
def getAllWorkingHours(request):
    working = BranchWorkingHours.objects.all()
    serializer = BranchWorkingHoursSerializer(working, many=True)

    return Response(serializer.data)

@swagger_auto_schema(operation_description="This endpoint returns Branch Working Hours by ID",
                     method="GET")
@api_view(['Get'])
def getWorkingHoursByID(request, pk):
    working = BranchWorkingHours.objects.get(id=pk)
    serializer = BranchWorkingHoursSerializer(working, many=False)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns Branch Working Hours by Branch",
                     method="GET")
@api_view(['Get'])
def getWorkingHoursByBranch(request, branch_id):
    working = BranchWorkingHours.objects.filter(branch=branch_id)
    serializer = BranchWorkingHoursSerializer(working, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint create Branch Working Hours",
                     method="POST",  request_body=BranchWorkingHoursSerializer)
@api_view(["POST"])
def createBranchWorkingHours(request):
    serializer = BranchWorkingHoursSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Change Branch Working Hours",
                     method="PUT",  request_body=BranchWorkingHoursSerializer)
@api_view(["PUT"])
def putBranchWorkingHours(request, pk):
    working = BranchWorkingHours.objects.get(id=pk)
    serializer = BranchWorkingHoursSerializer(working, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Delete Branch Working Hours",
                     method="DELETE")
@api_view(["DELETE"])
def deleteBranchWorkingHours(request, pk):
    working = BranchWorkingHours.objects.get(id=pk)

    if working:
        if working.delete():
            return Response("Branch Working Hours has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Branch  Working Hours with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)