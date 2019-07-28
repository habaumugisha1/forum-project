from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Forum(models.Model):
        name        = models.CharField(max_length=40)
        description = models.CharField(max_length=120)

        def __str__(self):
           return self.name




class Topic(models.Model):
    subjects     = models.CharField(max_length=150)
    last_updated = models.DateTimeField(default=datetime.now())
    forum        = models.ForeignKey(Forum, related_name='topics', on_delete= models.CASCADE)
    starter      = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    def __str__(self):
        return self.subjects

class Post(models.Model):
    message    = models.CharField(max_length=350)
    topic      = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default= datetime.now())
    updated_at = models.DateTimeField(default= datetime.now())
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    update_by  = models.ForeignKey(User, related_name='+', on_delete=models.CASCADE)

