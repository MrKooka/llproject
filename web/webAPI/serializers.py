from rest_framework import serializers
from ..models import Customer, Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'ru', 'eng', 'context']



class GoogleAuthSerializer(serializers.Serializer):
    """Сериализвция данных от Google"""
    email = serializers.EmailField()
    token = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["name", "email", "chat_id"]