from rest_framework import permissions

class IsPostOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        # Permite todas las solicitudes POST
        if request.method == 'POST, GET':
            return True
        # De otra manera, unicamente permite la autenticacion
        # Post Django 1.10, 'is_authenticated' es un atributo solo-lectura/read-only
        return request.user and request.user.is_authenticated
