from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from enumchoicefield import ChoiceEnum, EnumChoiceField

import company.models as co
import library.models as lm
import people.models as pm


class Season(models.Model):
    '''
    Container for *Production*s.
    '''
    company = models.ForeignKey(co.Company, related_name='seasons')
    name = models.CharField(max_length=50)   # e.g. 'Spring 2017' or just '2018'
    start_date = models.DateField()
    end_date = models.DateField()

class Production(models.Model):
    '''
    Container for *Show*s.
    '''
    book = models.CharField(max_length=100)
    season = models.ForeignKey(Season, related_name='productions')

class Show(models.Model):
    '''
    Information about a particular performance of a particular production.
    There should be a *Call* instance of type ``PERFORMANCE``
    that references any given *Show* instance.   If a production has
    multiple performances there should be a single *Show* instance for
    each of these.  This let's us just have a *Call* model that doesn't
    need to be sub-classed and that doesn't need to have attributes
    included that are extraneous to call types other than PERFORMANCE.
    '''
    name = models.CharField(max_length=100)
    production = models.ForeignKey(Production, related_name='shows')
    when = models.DateTimeField()


class Director(models.Model):
    person = models.ForeignKey(pm.Artist, related_name="director",
                                  on_delete=models.CASCADE)
    show = models.OneToOneField(Show, related_name="director",
                                on_delete=models.CASCADE)

class Conductor(models.Model):
    person = models.ForeignKey(pm.Artist, related_name="conductors",
                               on_delete=models.CASCADE)
    show = models.OneToOneField(Show, related_name="conductor",
                             on_delete=models.CASCADE)

class Choreographer(models.Model):
    person = models.ForeignKey(pm.Artist, related_name="choreographers",
                               on_delete=models.CASCADE)
    show = models.OneToOneField(Show, related_name="choreographer",
                             on_delete=models.CASCADE)

class StageManager(models.Model):
    person = models.ForeignKey(pm.Artist, related_name="stage_managers",
                               on_delete=models.CASCADE)
    show = models.OneToOneField(Show, related_name="stage_manager",
                             on_delete=models.CASCADE)

class SetDesigner(models.Model):
    person = models.ForeignKey(pm.Artist, related_name="set_designers",
                               on_delete=models.CASCADE)
    show = models.OneToOneField(Show, related_name="set_designer",
                             on_delete=models.CASCADE)

class LightingDesigner(models.Model):
    person = models.ForeignKey(pm.Artist, related_name="lighting_designers",
                               on_delete=models.CASCADE)
    show = models.OneToOneField(Show, related_name="lighting_designer",
                             on_delete=models.CASCADE)

class Costumer(models.Model):
    person = models.ForeignKey(pm.Artist, related_name="costumer",
                               on_delete=models.CASCADE)
    show = models.OneToOneField(Show, related_name="costumer",
                             on_delete=models.CASCADE)


class CastMember(models.Model):
    '''
    This associates an actor (which can include production stahis itshff
    such as directors and crew members) with a particular show
    '''
    role = models.ForeignKey(lm.Role, related_name='played_by')
    person = models.ForeignKey(pm.Artist, related_name='repetoire')
    show = models.ForeignKey(Show, related_name='cast')


class CrewMember(models.Model):
    person = models.ForeignKey(pm.Person, related_name='crews')
    show = models.ForeignKey(Show, related_name='crew')


class CallTypeEnum(ChoiceEnum):
    unspecified = "unspecified"
    rehearsal = "rehearsal"
    performance = "performance"
    meeting = "meeting"


class Call(models.Model):
    '''
    Anyone who's worked in theatre of any sort will know what this is.
    For those who have not, it's really nothing more than a specific time
    and place where (and when) you're expected to be.  This can be a rehearsal,
    a performance, a coaching session, or just a meeting of some sort.
    '''

    dtg = models.DateTimeField()
    duration = models.DurationField()
    location = models.CharField(max_length=100)
    show = models.ForeignKey(Show, related_name="calls")
    type = EnumChoiceField(CallTypeEnum,
                           default=CallTypeEnum.unspecified)
    callee = models.ForeignKey(pm.Person, related_name="calls")
