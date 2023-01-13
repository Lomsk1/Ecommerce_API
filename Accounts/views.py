from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.utils.timezone import now
from rest_framework import generics, status, views, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from ecommerceAPI import settings
from djoser import signals, utils
from djoser.compat import get_user_email
from djoser.conf import settings
from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = settings.SERIALIZERS.user
    queryset = User.objects.all()
    # permission_classes = settings.PERMISSIONS.user
    # token_generator = default_token_generator
    # lookup_field = settings.USER_ID_FIELD
    def perform_update(self, serializer, *args, **kwargs):
        super().perform_update(serializer, *args, **kwargs)
        user = serializer.instance
        signals.user_updated.send(
            sender=self.__class__, user=user, request=self.request
        )

        # Only send activation email when email is changed
        if user.email_changed:
            context = {"user": user}
            to = [get_user_email(user)]
            settings.EMAIL.activation(self.request, context).send(to)

    # def partial_update(self, request, *args, **kwargs):
    #     user = request.user
    #     serializer = UserSerializer(user, request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     if settings.SEND_UPDATE_EMAIL.data and user.is_active:
    #         context = {"user": user}
    #         to = [get_user_email(user)]
    #         # UpdateEmail(self.request, context).send(to)
    #
    #     return  Response(self.get_serializer(request.user).data)