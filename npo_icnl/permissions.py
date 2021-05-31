from rest_framework import permissions

from npo_user.models import CLIENT


class ISCLIENT(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            return request.user.user_type == CLIENT