from django.db import models
from django.contrib.auth.models import User

class Winner(models.Model):
    times_won = models.IntegerField()
    times_lost = models.IntegerField()
    winner = models.ForeignKey(User, on_delete=models.CASCADE)
