from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import *
from .models import *
import random

class FavFood(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def get(self, request):
    #     query = User.objects.all()
    #     serialize = UserSerializer(query,many=True)
    #     return Response(serialize.data)
    #
    # def post(self, request):
    #     serialize = UserSerializer(data=request.data)
    #     if serialize.is_valid():
    #         serialize.save()
    #         return Response({"Successfully Created" : serialize.data})
    #     return Response("Invalid Data")

class RandomData(APIView):

    def get(self, request):
        result = list(User.objects.all())
        res = random.sample(result,1)
        serialize=FavouriteFoodSerializer(res,many=True)
        return Response(serialize.data)