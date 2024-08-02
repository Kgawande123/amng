from django.db import models
from django.core import validators
# Create your models here.
class Voter(models.Model):
    gen = [("Female","Female"),("Male","Male"),("Other","Other")]
    voter_id = models.AutoField(auto_created=True,primary_key=True,validators=[validators.MinValueValidator(1),validators.MaxValueValidator(50)])
    first_name = models.CharField(max_length=23)
    last_name = models.CharField(max_length=23)
    gender = models.CharField(max_length=23,choices=gen)
    address = models.CharField(max_length=23)
    city = models.CharField(max_length=23)
    state = models.CharField(max_length=23)
    pincode = models.IntegerField()
    dob = models.DateField()
    contact = models.BigIntegerField()