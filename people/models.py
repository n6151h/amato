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
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    '''
    Basic but essential information about a person.  This is by and large
    an abstract class for the other models defined herein.
    '''
    firstname = models.CharField(max_length=30, null=False, blank=False)
    surname = models.CharField(max_length=30)

    phone = PhoneNumberField(blank=True, null=False, default='')
    email = models.EmailField(blank=True, default='')

    @property
    def name(self):
        return '{}, {}'.format(self.surname, self.firstname)

class Talent(Person):
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


class Singer(Talent):
    '''
    A subtype of talent that includes musicians whose instrument is
    "voice".
    '''
    UNSPECIFIED = -1
    SOPRANO = 1
    ALTO = 2
    MEZZO = 3
    TENOR = 4
    COUNTERTENOR = 5
    BARITONE = 6
    BASS = 7

    VOICE_TYPES = [
        (SOPRANO, _("soprano")),
        (ALTO, _("alto")),
        (MEZZO, _("mezzo-soprano")),
        (TENOR, _("tenor")),
        (COUNTERTENOR, _("counter-tenor")),
        (BARITONE, _("baritone")),
        (BASS, _("bass")),
        (UNSPECIFIED, _("unspecified")),
    ]

    FACHS = enumerate(map(_, ['', 'lyric', 'coloratura', 'dramatic', 'verdi', 'mozart', 'helgen']))

    voice = models.IntegerField(choices=VOICE_TYPES, verbose_name=_("Voice"),
                                null=False, default=UNSPECIFIED)
    fach = models.IntegerField(choices=FACHS, verbose_name=_("Fach"), default=0)


class Instrumentalist(Talent):
    '''
    A subtype of *Talent* whose musical instrument is something other than their voice.
    '''
    instrument = models.CharField(null=False, blank=True, max_length=40)

class Dancer(Talent):
    '''
    Included for completeness.  At this time I'm not really
    sure about what else to put in here.  Ideally there should perhaps
    be an enumeration field of some sort that allows a dancer to be
    listed as a subset of types.  (E.g. ballet, tap, and jazz).
    '''
    style = models.CharField(max_length=100)

class Staff(Person):
    '''
    Staff are those *Person*s who work behind the scene to make things happen.
    '''
    PRODUCTION_AREA = 1
    STAGE_AREA = 2
    HOUSE_AREA = 3
    ADMIN_AREA = 4
    GENERAL_AREA = 5

    STAFF_AREAS = [
        (PRODUCTION_AREA, _("production")),
        (STAGE_AREA, _("stage")),
        (HOUSE_AREA, _("house")),
        (ADMIN_AREA, _("administration")),
        (GENERAL_AREA, _("support")),
    ]

    area = models.IntegerField(choices=STAFF_AREAS, verbose_name=_("Area"),
                                null=False, default=GENERAL_AREA)

