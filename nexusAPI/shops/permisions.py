
from rest_framework.permissions import BasePermission

class IsStaffPermission(BasePermission):
    """used to check if the user is staff"""
    def has_permission(self, request, view):
        return request.user.is_staff
