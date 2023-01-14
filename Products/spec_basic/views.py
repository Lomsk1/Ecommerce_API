from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from Products.models import SpecificationBasics
from Products.serializers import SpecificationBasicsSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint return Spec Basic by Product",
                     method="GET")
@api_view(["GET"])
def getSpecBasicBySpec(request, basic_id):
    basic = SpecificationBasics.objects.filter(basic_id=basic_id)
    serializer = SpecificationBasicsSerializer(basic, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns all Spec Basic of  Product",
                     method="GET")
@api_view(["GET"])
def getAllSpecBasic(request):
    basic = SpecificationBasics.objects.all()
    serializer = SpecificationBasicsSerializer(basic, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns Spec Basic by ID",
                     method="GET")
@api_view(["GET"])
def getSpecBasicByID(request, pk):
    basic = SpecificationBasics.objects.get(id=pk)
    serializer = SpecificationBasicsSerializer(basic, many=False)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint create Spec Basic",
                     method="POST",  request_body=SpecificationBasicsSerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
def createSpecBasic(request):
    serializer = SpecificationBasicsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Change Spec Basic",
                     method="PUT",  request_body=SpecificationBasicsSerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def putSpecBasic(request, pk):
    specification = SpecificationBasics.objects.get(id=pk)
    serializer = SpecificationBasicsSerializer(specification, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint returns Delete Spec Basic",
                     method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteSpecBasic(request, pk):
    basic = SpecificationBasics.objects.get(id=pk)

    if basic:
        if basic.delete():
            return Response("Spec Basic has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Spec Basic with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)
