from django.db import models

class League(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    founded = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
