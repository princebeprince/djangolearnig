from django.db import models

# Create your models here.
#projects

class Projects(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    imgs = models.ImageField(upload_to="Portfolio/images")
    urls = models.URLField(blank=True)

