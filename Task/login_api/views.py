from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from passlib.hash import pbkdf2_sha256 as handler
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import *
from .models import *


class Signup(APIView):

    def get(self, request):
        query = User.objects.all()
        serialize = SignupSerializer(query,many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = SignupSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            user = User.objects.get(username=serialize.data['username'])
            token,created = Token.objects.get_or_create(user=user)
            print(token)
            return Response({"Successfully Registered": serialize.data, "Token": token.key, "Created": created})
        return Response("Invalid data")

class Login(APIView):

    def post(self, request):
        login = request.data
        try:
            query = User.objects.get(username=login['username'])
            user = authenticate(username=login['username'], password=login['password'])
            # print(query.username)
            # print(query.password, login['password'])
            # print(check_password(login['password'], query.password))
            if query is not None:
                if query.username == login['username'] and check_password(login['password'], query.password):
                    # if query.username == login['username'] and handler.verify(query.password, handler.hash(login['password'])):
                    return Response("Login Successful")
                else:
                    return Response("Password doesn't match")

        except:
            return Response("User not Registered")


class EmployeeEntry(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = Employee.objects.all()
        serialize = EmployeeSerializer(query, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = EmployeeSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({"Successfully Created" : serialize.data})


class EmployeeUpdate(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            query = Employee.objects.get(emp_id=pk)
            serialize = EmployeeSerializer(query)
            return Response(serialize.data)
        except:
            return Response("Data Not Found")

    def put(self, request, pk):
        try:
            query = Employee.objects.get(emp_id=pk)
            serialize = EmployeeSerializer(instance=query,data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response("Updated Successfully")
            return Response("Invalid Data")

        except:
            return Response("Data not Found")

    def delete(self, request, pk):

        try :
            query = Employee.objects.get(emp_id=pk)
            query.delete()
            return Response("Deleted Successfully")
        except:
            return Response("Data not Found")


class EmployeeAsset(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = UserAssetDetail.objects.all()
        serialize = EmployeeAssetSerializer(query, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = EmployeeAssetSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({"Successfully Created": serialize.data})


class EmployeeAssetUpdate(APIView):

    permission_classes = [IsAuthenticated]

    def get (self, request, pk):
        try:
            query = UserAssetDetail.objects.get(emp_id=pk)
            serialize = EmployeeAssetSerializer(query)
            return Response(serialize.data)
        except:
            return Response("Data Not found")


    def put(self, request, pk):

        try:
            query = UserAssetDetail.objects.get(emp_id=pk)
            serialize = EmployeeAssetSerializer(instance=query,data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response("Updated Successfully")
            return Response("Invalid Data")
        except:
            return Response("Data not found")

    def delete(self, request, pk):

        try:
            query = UserAssetDetail.objects.get(emp_id=pk)
            query.delete()
            return Response("Deleted Successfully")
        except:
            return Response("Data not Found")


class EmployeeFamily(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = UserFamilyDetail.objects.all()
        serialize = EmployeeFamilySerializer(query, many=True)
        return Response(serialize.data)

    def post(self, request):
        serialize = EmployeeFamilySerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({"Successfully Created": serialize.data})


class EmployeeFamilyUpdate(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            query = UserFamilyDetail.objects.get(emp_id=pk)
            serialize = EmployeeFamilySerializer(query)
            return Response(serialize.data)
        except:
            return Response("Data not Found")


    def put(self, request, pk):
        try:
            query = UserFamilyDetail.objects.get(emp_id=pk)
            serialize = EmployeeFamilySerializer(instance=query, data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response("Updated Successfully")
            return Response("Invalid Data")
        except:
            return Response("Data not Found")

    def delete(self, request, pk):

        try:
            query = UserFamilyDetail.objects.get(emp_id=pk)
            query.delete()
            return Response("Deleted Successfully")
        except:
            return Response("Data not Found")