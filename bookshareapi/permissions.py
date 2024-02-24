from rest_framework import permissions


class BookPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # sabai action allow garxa creator lai
        if obj.created_by == request.user:
            return True

        # shared users lai allow garxa to perform actions if they have the required permission
        if request.user in obj.shared_with.all():
            required_permission = ''

            if request.method == 'GET':
                return True  # Allow viewing details for shared users, sabai shared users lai

            elif request.method in ['PUT', 'PATCH', 'DELETE']:
                required_permission = 'Update'

            # Allow the action only if the user has the required permission
            return obj.shared_permissions.filter(permission=required_permission).exists()

        return False  # Deny access for other cases
