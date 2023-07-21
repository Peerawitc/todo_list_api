from rest_framework import serializers
from .models import Worklist


class WorklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worklist
        fields = ['id','workname','date']