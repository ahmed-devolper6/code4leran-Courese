from argparse import _MutuallyExclusiveGroup
from django.db import models

# Create your models here.
class coures(models.Model):
    title = models.CharField(max_length=50)
    contant = models.CharField(max_length=1000)
    image = models.ImageField(upload_to= 'coureses/')
    price = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title()