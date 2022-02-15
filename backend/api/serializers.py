
from rest_framework import serializers
from .models import User_info

class User_info_Serializers (serializers.ModelSerializer):
    class Meta:
        model= User_info
        fields = ('id','name','age','gender','weight','height','created_on','username','password')