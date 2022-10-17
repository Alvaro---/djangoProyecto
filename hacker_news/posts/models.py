from django.db import models

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    points = models.IntegerField()
    author = models.CharField(max_length=200)
    publicationDate = models.TimeField()

    def __str__(self):
        return f"{self.title} fue publicado por {self.author} en la fecha"
