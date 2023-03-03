from rest_framework import serializers
from mainApp.models import conversations

class Chatserialier(serializers.ModelSerializer):
    class Meta:
        model= conversations
        fields=['id','user','input_text','response_text']
    