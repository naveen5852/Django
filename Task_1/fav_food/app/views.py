from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import *
from .models import *

class FavFood(APIView):
    def get(self, request):
        query = User.objects.all()
        serialize = UserSerializer(query,many=True)
        return Response(serialize.data)
