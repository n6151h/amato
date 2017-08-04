from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(required=True, max_length=30)
    surname = models.CharField(required=True, max_length=30)

    phone = model.PhoneNumberField(blank=True)


class Musician(Person):
    pass  #

class Singer(Musician):
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
        (BASE, _("bass")),
        (UNSPECIFIED, _("unspecified")),
    ]

    FACHS = enumerate(['lyric', 'coloratura', 'dramatic', 'verdi', 'mozart', 'helgen'])

    voice = models.IntegerField(choices=VOICE_TYPES, verbose_name=_("Voice"),
                                required=True, nullable=False, default=UNSPECIFIED)
    fach = models.IntegerField(choices=FACHS, verbose_name=_("Fach"))


class Instrumentalist(Musician):
    instrument = model.CharField(required)

class Staff(Person):
    PRODUCTION_FUNCTION = 1
    HOUSE_FUNCTION = 2
    ADMIN_FUNCTION = 3
    GENERAL_FUNCTION = 4

    STAFF_FUNCTIONS = [
        (PRODUCTION_FUNCTION, _"production"),
        (HOUSE_FUNCTION, _"house"),
        (ADMIN_FUNCTION, _("administration"),
        (GENERAL_FUNCTION, _("support")),
    ]

    function models.IntegerField(choices=STAFF_FUNCTIONS, verbose_name=_("Function"),
                                required=True, nullable=False, default=GENERAL_FUNCTION)


# Need a way to model director, chorus master, choreographer, stage manager, lighting designer, set designer, costumer

# Need a way to maintain customer / subscriber data