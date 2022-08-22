from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='uploads')
    price_from = models.DecimalField(decimal_places=2, max_digits=5, null=True)

    def __str__(self):
        return self.name
    


class Member(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='members')

    def __str__(self):
        return self.name
    