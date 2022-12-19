from rest_framework.serializers import ModelSerializer, DateField
from WeeklySales.models import WeeklySale


class WeeklySaleSerializer(ModelSerializer):
    class Meta:
        model = WeeklySale
        fields = "__all__"
