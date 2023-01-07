from rest_framework.decorators import api_view
from rest_framework.response import Response
from Subscription.models import Subscription
from Subscription.serializations import SubscriptionSerializer
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(operation_description="This endpoint returns all Subscriptions",
                     method="GET")
@api_view(['GET'])
def getAllSubscriptions(request):
    email = Subscription.objects.all()
    serializer = SubscriptionSerializer(email, many=True)
    return Response(serializer.data)

@swagger_auto_schema(operation_description="This endpoint returns every Subscriptions by ID",
                     method="GET")
@api_view(["GET"])
def getSubscriptionsById(request, pk):
    email = Subscription.objects.get(id=pk)
    serializer =SubscriptionSerializer(email, many=False)
    return Response(serializer.data)

@swagger_auto_schema(operation_description="This endpoint create Subscriptions",
                     method="POST",  request_body=SubscriptionSerializer)
@api_view(["POST"])
def createSubscriptions(request):
    serializer = SubscriptionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(operation_description="This endpoint change Subscriptions",
                     method="PUT", request_body=SubscriptionSerializer)
@api_view(["PUT"])
def updateSubscriptions(request, pk):
    email = Subscription.objects.get(id=pk)
    serializer = SubscriptionSerializer(email, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(operation_description="This endpoint delete Subscriptions",
                     method="DELETE")
@api_view(["DELETE"])
def deleteSubscriptions(request, pk):
    email = Subscription.objects.get(id=pk)

    if email:
        if email.delete():
            return Response("Subscriptions has been Deleted", status=status.HTTP_200_OK)
        else:
            return Response("Error while deleting", status.HTTP_400_BAD_REQUEST)

    return Response("Subscriptions with this ID Does not Exist", status=status.HTTP_404_NOT_FOUND)
