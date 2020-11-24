from django.shortcuts import render
from .models import User
from .serializers import UserSerializer # Se importa/habilita la autenticacion post.
from .permissions import IsPostOrIsAuthenticated 
from rest_framework.decorators import permission_classes # Este decorador nos evita que django nos solite el token cuando se utilicen los endpoin de user
from rest_framework import generics

# Create your views here / Aqui se definen las vistas que van a estar disponibles por medio del urls.py
@permission_classes((IsPostOrIsAuthenticated, ))
class UserList(generics.ListCreateAPIView): # Se crea el apiView del serializer en forma de lista
    serializer_class = UserSerializer
    queryset = User.objects.all().exclude(is_superuser=1)  # Con esta opcion .exclude(is_superuser=1) evitamos listar usuarios administradores.

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
