from django.db import models


class Movies_Info(models.Model):
    name = models.CharField(max_length=100, help_text="the name of the movie")
    date = models.DateField(verbose_name="Date the movie was released")
