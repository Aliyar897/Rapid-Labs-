from rest_framework.permissions import BasePermission

class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'admin'

class IsManagerUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'manager'

class IsRegularUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'user'
