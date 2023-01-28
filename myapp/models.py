from django.db import models

# Create your models here.
class Movie(models.Model):
    image = models.ImageField(upload_to='images', default='images/none/sampleimg.jpg')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    rating = models.FloatField()

    def __str__(self):
        return self.name