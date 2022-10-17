from django.db import models

# Create your models here.


class Jobs(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    publicationDate = models.TimeField()

    def __str__(self):
        return f"{self.title} fue publicado por {self.empresa}"
