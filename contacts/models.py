from django.db import models
from datetime import datetime

# Create your models here.

class Contact(models.Model):
    listings = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(blank=True)
    phone = models.IntegerField()
    Contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name
