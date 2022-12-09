from django.db import models


# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    year = models.IntegerField()
    imge = models.ImageField(upload_to='image')
    def __str__(self):
        return self.name
