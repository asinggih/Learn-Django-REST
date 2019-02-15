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


class PostOwnStatus(permissions.BasePermission):
    """Allow users to only post their own status"""

    def has_object_permission(self, request, view, obj):
        """Check if user is posting status to their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        # if request is not in safe methods, then check if user owns
        # this object
        return obj.user_profile.id == request.user.id
