from django.db import models

# Create your models here.
class SampleModel (models.Model):
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 20)
    age = models.IntegerField
    def __str__(self):
        return str(self.first_name)