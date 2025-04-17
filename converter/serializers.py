from rest_framework import serializers
from converter.models import Image

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["id", "title", "description", "content"]
        read_only_fields = ["id"]


class ImageRetrieveSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    content = serializers.ImageField()


class ResizeImageSerializer(serializers.Serializer):
    width = serializers.IntegerField()
    hight = serializers.IntegerField()

    def validate_hight(self, value):
        if value <= 0 or value >= 10000:
            raise serializers.ValidationError({"message": "hight should be in range 1 to 9999"})
        return value

    def validate_width(self, value):
        if value <= 0 or value >= 10000:
            raise serializers.ValidationError({"message": "width should be in range 1 to 9999"})
        return value
    
    def update(self, instance, validated_data):
        instance.width = validated_data["width"]
        instance.hight = validated_data["hight"]
        instance.save()
        return instance
