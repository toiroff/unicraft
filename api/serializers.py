from rest_framework import serializers
from app.models import CertificateType, UserSubject, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name']

class UserSubjectSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    certificate_type = serializers.StringRelatedField()  # You can customize this as needed

    class Meta:
        model = UserSubject
        fields = ['id', 'user', 'certificate_type', 'subject', 'score']

class CertificateTypeSerializer(serializers.ModelSerializer):
    usersubjects = UserSubjectSerializer(many=True, read_only=True)

    class Meta:
        model = CertificateType
        fields = ['id', 'name', 'usersubjects']
