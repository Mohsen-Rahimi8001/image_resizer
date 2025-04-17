from django.shortcuts import get_object_or_404
from converter.models import Image
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from converter.serializers import ImageSerializer, ImageRetrieveSerializer, ResizeImageSerializer
from converter.permissions import HasImage
from converter.tasks import resize_image



class UploadImageAPIView(generics.CreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [IsAuthenticated]


class RetrieveImagesAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImageRetrieveSerializer

    def get_queryset(self):
        owner_id = self.kwargs.get("owner_id")
        return Image.objects.filter(owner_id=owner_id)


class ResizeImageAPIView(generics.UpdateAPIView):
    queryset = Image.objects.all()
    permission_classes = [IsAuthenticated, HasImage]
    serializer_class = ResizeImageSerializer
    
    def perform_update(self, serializer):
        image_id = self.kwargs.get("pk")
        serializer.save()
        validated_data = serializer.validated_data
        h, w = validated_data["hight"], validated_data["width"]
        
        resize_image.delay(image_id, w, h)
