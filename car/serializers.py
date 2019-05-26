from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    placa = serializers.CharField()
    duenio = serializers.CharField()
    modelo = serializers.IntegerField()
    marca = serializers.CharField()

    def create(self, validated_data):
        return Car.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.placa = validated_data.get('placa', instance.placa)
        instance.duenio = validated_data.get('duenio', instance.duenio)
        instance.modelo = validated_data.get('modelo', instance.modelo)
        instance.marca = validated_data.get('marca', instance.modelo)
        instance.save()
        return instance
    """
    placa = models.CharField(max_length=6)
    duenio = models.CharField(max_length=50)
    modelo =  models.IntegerField(default=0)
    """