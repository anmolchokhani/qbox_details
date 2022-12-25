from django.db import models

# Create your models here.
class ClientData(models.Model):
    name=models.CharField(max_length=70)
    boxno= models.IntegerField(max_length=10)
    qtrack_email=models.EmailField(max_length=100)
    qtrack_password=models.CharField(max_length=100)
    sudo_password=models.CharField(max_length=100)








