from django.db import models

# Create your models here.
class Data(models.Model):
    date = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return self.value
