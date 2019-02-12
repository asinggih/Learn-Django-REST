from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is editing their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        # if request is not in safe methods, then check if user owns
        # this object
        return obj.id == request.user.id
