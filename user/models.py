from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wallet = models.DecimalField(max_digits=10, decimal_places=2)
