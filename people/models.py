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

from library.models import Book

class Person(PolymorphicModel):
    '''
    Basic but essential information about a person.  This is by and large
    an abstract class for the other models defined herein.
    '''

    class Meta:
        verbose_name_plural = "People"


    talents = models.ManyToManyField(Talent,
                                     verbose_name="talents and skills")

    def __str__(self):
        return self.full_name

    __unicode__ = __str__

    @property
    def type(self):
        return self.__class__.__name__


    @property
    def full_name(self):
        contact = self.contacts.first()
        if contact is not None:
            return "%s %s" % (contact.firstname, contact.surname)
        else:
            return ""


class Staff(Person):
    '''
    This would include people who are not performers or artists.
    Production staff, stage crew, house staff (box office, ushers)
    would fall into this category.
    '''
    class Meta:
        verbose_name_plural = 'staff'


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



class ContactData(models.Model):
    '''
    We separate this from *Person* subclasses for two reasons:

      1. DRY -- both *Artist* and *Staff* subclasses require this
         information.
      2. We use a different naming scheme for *Role* instances.

    '''
    firstname = models.CharField(max_length=30, null=False, blank=False)
    surname = models.CharField(max_length=30, blank=True, null=False, default='')
    phone = PhoneNumberField(blank=True, null=False, default='')
    email = models.EmailField(blank=True, default='')
    person = models.ForeignKey(Person, related_name='contacts', default=None, null=True)

    class Meta:
        verbose_name_plural = 'contact data'

class RoleLevel(models.Model):
    '''
    Levels are used to describe the size or difficulty of
    a role.  Levels mig0t include "principal" and "comprimario", or
    "major" and "minor".
    '''
    name = models.CharField(max_length=100, blank=False, null=False)
    rank = models.IntegerField(blank=False, null=False, default=-1)

    def __str__(self):
        return self.name

    __unicode__ = __str__

class Role(Person):
    '''
    We'll use this subclass to encode roles associated with operas
    (or musicals or scripts).
    '''
    book = models.ForeignKey(Book)  # related_name will be role_set
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    level = models.ForeignKey(RoleLevel)

    def __str__(self):
        return "%s (%s)" % (self.name, self.book.title)

    __unicode__ = __str__