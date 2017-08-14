from django.db import models

# Create your models here.

import people

class Company(models.Model):
    '''
    Opera or Theatre company informtation.
    '''
    name = models.CharField(max_length=100)
    #ad = # need a PeopleField here.
