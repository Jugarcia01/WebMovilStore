from rest_framework import serializers
from .models import User  # Aqui importamos el modelo desde models.py de la carpeta user
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):

    # Con este class Meta y las instrucciones siguientes nos evitamos tener que definir todos los campos del modelo user (UsuariosSerializer)
    class Meta:
        # Con esta opcion estamos indicando al serializers que se muestren todos los campos del modelo.
        model = User
        # fields = '__all__'  # Excepto username y password debido a la opcion de write_only=True, esos dos campos no serán visibles.
        exclude = ('is_superuser', 'is_staff')
        extra_kwargs = {
            'password': {'write_only': True},
            'username': {'write_only': True},
            'birthday': {'required': False},
        }

    def create(self, validated_data, instance=None):
        print(validated_data)
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        kwargs = {
            "id=validated_data['group']"
        }
        group = Group.objects.get(**kwargs)
        # group =Group.objects.get(id=validated_data['group']) #Utilizado cuando solo se tiene un argumento
        group.user_set.add(user)
        return user
 