from django.urls import path

from .views import (
    UploadImageAPIView,
    RetrieveImagesAPIView,
    ResizeImageAPIView,
)


urlpatterns = [
    path("upload/", UploadImageAPIView.as_view(), name="upload-image"),
    path("retrieve/<int:owner_id>", RetrieveImagesAPIView.as_view(), name="retrieve-images"),
    path("resize/<int:pk>", ResizeImageAPIView.as_view(), name="resize-image"),
]

