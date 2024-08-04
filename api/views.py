from rest_framework import viewsets
from app.models import Certificates
from .serializers import CertificatesSerializer

class CertificatesViewSet(viewsets.ModelViewSet):
    queryset = Certificates.objects.all()
    serializer_class = CertificatesSerializer
