from rest_framework import serializers
from .models import *

class CategSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

