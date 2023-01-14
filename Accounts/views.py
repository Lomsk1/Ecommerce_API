from django.contrib.auth import get_user_model
from rest_framework import viewsets
from djoser.conf import settings
# from .serializers import CurrentUserSerializer
from .models import UserAccount, UserAccountManager

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    pass

# class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = CurrentUserSerializer