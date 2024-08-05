from rest_framework import viewsets
from app.models import CertificateType, UserSubject, Subject
from .serializers import CertificateTypeSerializer, UserSubjectSerializer, SubjectSerializer

class CertificateTypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CertificateType.objects.filter(usersubject__isnull=False).distinct()
    serializer_class = CertificateTypeSerializer

class UserSubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserSubject.objects.all()
    serializer_class = UserSubjectSerializer

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
