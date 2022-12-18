from rest_framework.serializers import ModelSerializer
from WeeklySales.models import WeeklySale

class WeeklySalesSerializer(ModelSerializer):
    class Meta:
        model = WeeklySale
        fields = "__all__"
