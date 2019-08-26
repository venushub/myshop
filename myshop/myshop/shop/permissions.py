from rest_framework import permissions

class UserAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return not request.user.is_staff


class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method not in permissions.SAFE_METHODS and request.user.is_staff:
            return True
        else:
            return False
