from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificatesViewSet

router = DefaultRouter()
router.register(r'certificates', CertificatesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
