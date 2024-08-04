from rest_framework import serializers
from app.models import Certificates

class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        fields = ['id', 'user', 'name', 'score']
