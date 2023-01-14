from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from Products.models import ProductBranch
from Products.serializers import ProductBranchSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser


@swagger_auto_schema(operation_description="This endpoint return Product Stocks by Branch",
                     method="GET")
@api_view(["GET"])
def getStockByProduct(request, product_id):
    stock = ProductBranch.objects.filter(product=product_id)
    serializer = ProductBranchSerializer(stock, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns all Stocks of  Product",
                     method="GET")
@api_view(["GET"])
def getAllStock(request):
    stock = ProductBranch.objects.all()
    serializer = ProductBranchSerializer(stock, many=True)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint returns Stocks by ID",
                     method="GET")
@api_view(["GET"])
def getStockByID(request, pk):
    stock = ProductBranch.objects.get(id=pk)
    serializer = ProductBranchSerializer(stock, many=False)

    return Response(serializer.data)


@swagger_auto_schema(operation_description="This endpoint create Stock",
                     method="POST",  request_body=ProductBranchSerializer)
@api_view(["POST"])
@permission_classes([IsAdminUser])
def createStock(request):
    serializer = ProductBranchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint Change Stock",
                     method="PUT",  request_body=ProductBranchSerializer)
@api_view(["PUT"])
@permission_classes([IsAdminUser])
def putStock(request, pk):
    stock = ProductBranch.objects.get(id=pk)
    serializer = ProductBranchSerializer(stock, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint returns Delete Stock",
                     method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAdminUser])
def deleteStock(request, pk):
    basic = ProductBranch.objects.get(id=pk)

    if basic:
        if basic.delete():
            return Response("Stock has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Stock with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)
