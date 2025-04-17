from rest_framework.permissions import BasePermission

class HasImage(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # obj is image
        return obj.owner == request.user
