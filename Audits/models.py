from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Audit(models.Model):
    fecha = models.DateTimeField()
    nombre = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.nombre

class Question(models.Model):
    user = models.ForeignKey(User)
    pregunta = models.TextField()
    audit = models.ForeignKey(Audit)
    def __unicode__(self):
        return self.pregunta

class Document(models.Model):
    filename = models.CharField(max_length=100)
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')