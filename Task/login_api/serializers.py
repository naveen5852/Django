from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from . models import *



class SignupSerializer(ModelSerializer):
    class Meta :
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'],validated_data['email'])
        user.set_password(validated_data['password'])
        print(user.password)
        user.save()
        return user
        # #
        # def validate(self, data):
        #     data['password']=make_password(data['password'])
        #     return data


class EmployeeSerializer(ModelSerializer):
    class Meta :
        model = Employee
        fields = '__all__'


class EmployeeAssetSerializer(ModelSerializer):
    class Meta:
        model = UserAssetDetail
        fields = '__all__'


class EmployeeFamilySerializer(ModelSerializer):
    class Meta:
        model = UserFamilyDetail
        fields = '__all__'
