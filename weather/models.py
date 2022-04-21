from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=30)

    def str(self):
        return self.name