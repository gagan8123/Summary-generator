from django.db import models

# Create your models here.
class inptext(models.Model):
    text = models.TextField()
    output = models.TextField()
