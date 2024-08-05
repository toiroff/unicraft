from django.db import models
from django.contrib.auth.models import User

class CertificateType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Subject(models.Model):
    certificate_type = models.ForeignKey(CertificateType, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

      
    def __str__(self):
        return f"{self.name} for {self.certificate_type}"
    

class UserSubject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(CertificateType, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.certificate_type.name} - {self.subject.name}"

class UserCertificates(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(CertificateType, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(UserSubject)