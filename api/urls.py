from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificateTypeViewSet, UserSubjectViewSet, SubjectViewSet

router = DefaultRouter()
router.register(r'certificate-types', CertificateTypeViewSet)
router.register(r'user-subjects', UserSubjectViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
