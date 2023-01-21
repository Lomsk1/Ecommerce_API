from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from wishlist.models import Wishlist
from wishlist.serializers import WishlistSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from Products.models import Product


@swagger_auto_schema(operation_description="This endpoint returns all Wishlist", method="GET")
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getAllWishlist(request):
    wishlist = Wishlist.objects.all()
    serializer = WishlistSerializer(wishlist, many=True)
    return Response(serializer.data)

@swagger_auto_schema(operation_description="This endpoint returns every Wishlsit by ID",
                     method="GET")
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getWishlistById(request, pk):
    wishlist = Wishlist.objects.get(id=pk)
    serializer =WishlistSerializer(wishlist, many=False)
    return Response(serializer.data)

@swagger_auto_schema(operation_description="This endpoint returns Wishlist by User",
                     method="GET")
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getWishlistByUser(request, user_id):
    wishlist = Wishlist.objects.filter(user=user_id)
    # products = Product.objects.filter(id=)
    serializer = WishlistSerializer(wishlist, many=True)

    return Response(serializer.data)




@swagger_auto_schema(operation_description="This endpoint create Wishlist", method="POST",
                     request_body=WishlistSerializer)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def createWishlist(request):
    serializer = WishlistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint change Wishlist",
                     method="PUT", request_body=WishlistSerializer)
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def updateWishlist(request, pk):
    wishlist = Wishlist.objects.get(id=pk)
    serializer = WishlistSerializer(wishlist, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint delete Wishlist", method="DELETE")
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def deleteWishlist(request, pk):
    wishlist = Wishlist.objects.get(id=pk)

    if wishlist:
        if wishlist.delete():
            return Response("Wishlist has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Wishlist with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)


# @swagger_auto_schema(operation_description="This endpoint returns Products by User",
#                      method="GET")
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getProductsByUser(request):
#     products = Product.objects.all()
#     serializer = ProductWishlistSerializer(products, many=True)
#
#     return Response(serializer.data)