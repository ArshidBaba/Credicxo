from rest_framework import permissions


class IsStudentPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        username = request.user
        print(username)
        return super().has_permission(request, view)