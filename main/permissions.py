from rest_framework import permissions


class IsStaffDeleteOnly(permissions.BasePermission):
    message = "Only staff users can delete objects"

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE":
            return request.user.is_staff is True
        return True
