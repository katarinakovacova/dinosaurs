from rest_framework import serializers
from .models import Dinosaur, User


class DinosaurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinosaur
        fields = ["id", "name", "eating_classification", "typical_color", "period", "average_size", "image1", "image2"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "favorite_dinosaurs"]
