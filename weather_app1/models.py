from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name # it return django admin with name and not return static string

    class Meta:
        verbose_name_plural = 'cities' # Correct Grammar cities