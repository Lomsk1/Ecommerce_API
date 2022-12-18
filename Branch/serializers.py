from rest_framework.serializers import ModelSerializer
from Branch.models import Branch, BranchCoord, BranchWorkingHours


class BranchCoordSerializer(ModelSerializer):
    class Meta:
        model = BranchCoord
        fields = "__all__"


class BranchWorkingHoursSerializer(ModelSerializer):
    class Meta:
        model = BranchWorkingHours
        fields = "__all__"


class BranchSerializer(ModelSerializer):
    coord = BranchCoordSerializer(many=True, read_only=True)
    working_hours = BranchWorkingHoursSerializer(many=True, read_only=True)

    class Meta:
        model = Branch
        fields = "__all__"