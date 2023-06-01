from django.db import models

# Create your models here.
class Data(models.Model):
    capteur = models.CharField(max_length=200)
    date = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return str(self.value)
