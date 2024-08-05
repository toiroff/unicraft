from django.contrib import admin
from .models import *

admin.site.register(CertificateType)
admin.site.register(Subject)
admin.site.register(UserSubject)
admin.site.register(UserCertificates)


