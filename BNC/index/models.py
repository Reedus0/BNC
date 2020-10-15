from django.db import models

# Create your models here.
class Expert(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=10)
    image = models.ImageField(upload_to='static\images')
    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=30)
    review = models.TextField()
    type = models.CharField(max_length=50)
    def __str__(self):
        return self.name
