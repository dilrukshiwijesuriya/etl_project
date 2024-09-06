from rest_framework import serializers
from datetime import datetime

class ItemSerializer(serializers.Serializer):
    item_id = serializers.CharField(required=True)
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(min_value=0.01)

class DataSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True, allow_blank=False)
    email = serializers.EmailField(required=True)
    timestamp = serializers.DateTimeField(required=True)
    items = ItemSerializer(many=True)

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("The 'items' list must not be empty.")
        return value

    def validate_timestamp(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%fZ')
        except ValueError:
            raise serializers.ValidationError("Invalid timestamp format. Use ISO 8601.")
        return value
