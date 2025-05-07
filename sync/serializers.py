from rest_framework import serializers
from .models import SyncEvent

class SyncEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyncEvent
        fields = '__all__'
