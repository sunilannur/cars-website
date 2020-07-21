from rest_framework import serializers
from . import models


class CarsSerializer(serializers.ModelSerializer):
    # Serializer for the Restaurant model, in fields we specify the model attributes we want to
    # deserialize and serialize
    class Meta:
        model = models.Car
        fields = ['id','name','detail','car_image']