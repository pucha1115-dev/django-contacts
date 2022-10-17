from rest_framework import serializers
from app.models import Contacts

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'