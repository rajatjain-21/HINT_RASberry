from __future__ import unicode_literals
from django.db import models

class fill(models.Model):
     title = models.CharField( max_length=100)
     causes = models.TextField(default="")
     symptoms = models.TextField(blank="")
     diagnosis = models.TextField(blank="")
     complications = models.TextField(blank="")
     medicine = models.TextField(blank="")
     upvote=models.IntegerField(default=0)
     downvote=models.IntegerField(default=0)
