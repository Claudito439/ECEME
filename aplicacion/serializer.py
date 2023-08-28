from rest_framework import serializers
from .models import Pais, Fuerza, Regimiento

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class FuerzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuerza
        fields = ['id','nombre']

class RegimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regimiento
        fields = ['id','nombre']





