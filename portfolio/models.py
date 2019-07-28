from django.db import models

from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class portfolio(models.Model):
    title       = models.CharField(max_length= 150)
    image       = models.ImageField(upload_to='portfolio')
    description = models.TextField()
    created_at  = models.DateTimeField(default= datetime.now())
    def __str__(self):
        return self.title
