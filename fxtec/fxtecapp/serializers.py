from rest_framework import serializers
from .models import Robot

class RobotModelSerializer(serializers.ModelSerializer):
     class Meta:
         model = Robot
         fields = '__all__'
