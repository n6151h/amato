from django.db import models

# Create your models here.

import people

class Company(models.Model):
    '''
    Opera or Theatre company informtation.
    '''
    name = models.CharField(max_length=100)

    # We'll add other fields l ater.

