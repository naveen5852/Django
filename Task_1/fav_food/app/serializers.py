from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FavouriteFoodSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'favourite_food']