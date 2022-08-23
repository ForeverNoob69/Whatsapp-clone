from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import *

class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class roomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class profileSerializer(serializers.ModelSerializer):



    class Meta:
        model = Profile
        fields = '__all__'

