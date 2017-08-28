"""
Note that the *Castmember* model, even though it describes a *Person* is
found in the _schedule_ app's model. This is done mainly to avoid circular import
hassles.  However, it also reflects the notion that a cast member is
scheduled to play their role in a given *Show*, so it does make some
intuitive, not to mention logictical sense for *CastMember* to be
defined in the _schedule_ app.
"""

from __future__ import unicode_literals

from django.db import models

from django.db.utils import IntegrityError

from polymorphic.models import PolymorphicModel
from polymorphic.manager import PolymorphicManager
from polymorphic.showfields import ShowFieldType

from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from talent.models import Talent


class Person(PolymorphicModel):
    '''
    Basic but essential information about a person.  This is by and large
    an abstract class for the other models defined herein.
    '''

    class Meta:
        verbose_name_plural = "People"

    firstname = models.CharField(max_length=30, null=False, blank=False)
    surname = models.CharField(max_length=30)

    phone = PhoneNumberField(blank=True, null=False, default='')
    email = models.EmailField(blank=True, default='')

    talents = models.ManyToManyField(Talent,
                                     verbose_name="talents and skills")

    @property
    def sorting_name(self):
        return '{}, {}'.format(self.surname, self.firstname)

    @property
    def name(self):
        return '{} {}'.format(self.firstname, self.surname)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    @property
    def type(self):
        return self.__class__.__name__


class Artist(Person):
    '''
    Yet another layer of abstraction, mainly to distinguish between
    performers and non-performers, such as production staff, ushers,
    and box-office staff.   Using the term "talent" instead of, say,
    "musician" lets us off the hook in having to implicitly insult
    singers by referring only to orchestra members as "musicians".

    *Talent* can (and will) refer to actors (at the moment there is no
    *Actor* model, nor do I plan on there being one) as well as
    speakers (narrators, MCs, voice-over artists, etc.)

    *Talent* can (and for now will) also include conductors, choreaographers,
    and directors.
    '''
    agent = models.CharField(max_length=60, null=False, blank=True, default='')
    headshot = models.ImageField(null=True, blank=True, default=None)


