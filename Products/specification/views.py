from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from Products.models import Specifications
from Products.serializers import SpecificationsSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(operation_description="This endpoint returns Specifications by Product",
                     method="GET")
@api_view(["GET"])
def getSpecificationsByProduct(request, product_id):
    specification = Specifications.objects.filter(product=product_id)
    serializer = SpecificationsSerializer(specification, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns all Specification of  Product",
                     method="GET")
@api_view(["GET"])
def getAllSpecification(request):
    specification = Specifications.objects.all()
    serializer = SpecificationsSerializer(specification, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns Specification by ID",
                     method="GET")
@api_view(["GET"])
def getSpecificationByID(request, pk):
    specification = Specifications.objects.get(id=pk)
    serializer = SpecificationsSerializer(specification, many=False)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint create Specification",
                     method="POST",  request_body=SpecificationsSerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
def createSpecification(request):
    serializer = SpecificationsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Change Specification",
                     method="PUT",  request_body=SpecificationsSerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def putSpecification(request, pk):
    specification = Specifications.objects.get(id=pk)
    serializer = SpecificationsSerializer(specification, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint returns Delete Specification",
                     method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteSpecification(request, pk):
    specification = Specifications.objects.get(id=pk)

    if specification:
        if specification.delete():
            return Response("Specification has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Specification with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)
