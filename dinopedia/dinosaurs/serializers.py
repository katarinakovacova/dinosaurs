from rest_framework import serializers
from dinosaurs.models import Dinosaur


class DinosaurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinosaur
        fields = ["id", "name", "eating_classification", "typical_color", "period", "average_size", "image1", "image2"]

