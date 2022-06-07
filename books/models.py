from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    desc = models.TextField()
    image = models.ImageField(upload_to = 'image')
    publisher = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
