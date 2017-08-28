from django.db import models
from django.db.utils import IntegrityError

from polymorphic.models import PolymorphicModel
from polymorphic.manager import PolymorphicManager
from polymorphic.showfields import ShowFieldType

from enumchoicefield import ChoiceEnum, EnumChoiceField

class TalentCategoryEnum(ChoiceEnum):
    unspecified = "unspecified"
    singing = "singing"
    dancing = "dancing"
    acting = "acting"
    instrument = "instrument"
    directing = "directing"
    choreography = "choreography"
    stage = "stage"
    lighting = "lighting"
    house = "house"
    admin = "admin"
    sales = "sales/marketing"

class VoiceTypeEnum(ChoiceEnum):
    unspecified = "unspecified"
    soprano = "soprano"
    alto = "alto"
    mezzo = "mezzo-soprano"
    tenor = "tenor"
    countertenor = "countertenor"
    baritone = "baritone"
    bass = "bass"

class FachEnum(ChoiceEnum):
    unspecified = ""
    lyric = 'lyric'
    coloratura = 'coloratura'
    dramatic = 'dramatic'
    spinto = 'spinto'
    verdi = 'verdi'
    mozart = 'mozart'
    helgen = 'helgen'
    wagnerian = 'wagnerian'
    baroque = 'baroque'

class DancingStyleEnum(ChoiceEnum):
    unspecified = ""
    ballet = "ballet"
    tap = "tap"
    modern = "modern"
    jazz = "jazz"
    exotic = "exotic"



class Talent(PolymorphicModel):
    '''
    Describes a company members abilities.
    '''
    category = EnumChoiceField(TalentCategoryEnum,
                               max_length=50,
                               default=TalentCategoryEnum.unspecified)

    def __str__(self):
        return self.category.name

    def __unicode__(self):
        return self.category.name


    # def save(self, **kwargs):
    #     '''
    #     We overload this so that we don't inadverntently save multiple instances.
    #     Found I had to do this b/c the admin interface doesn't seem to use
    #     the TalentManager.create method.  Rather, in creates an instance and then
    #     calls ``save``.
    #     '''
    #     fields = dict([(f.name, getattr(self, f.name)) \
    #                   for f in self._meta.fields \
    #                     if not f.is_relation and (getattr(self, f.name) is not None)])
    #     t = self.__class__.objects.non_polymorphic().filter(**fields)
    #     if t:
    #         raise IntegrityError('<{}: {}> already exists'.format(self.type, t))
    #     return super(self.__class__, self).save(**kwargs)

    @property
    def type(self):
        return self.__class__.__name__



# The following subclasses of Talent have specific, additional attributes.
# Other subclasses might be added later.  But, for now, an actor is and actor
# is an actor -- no specialities really need yet be encoded.  (With apologies
# to my fine and talented actor friends.)

class Voice(models.Model):
    name = models.CharField(max_length=40, verbose_name="Range or Type",
                            blank=False, null=False)

    class Meta:
        verbose_name_plural = "Vocal Ranges/Types"

    def __str__(self):
        return self.name

    __unicode__ = __str__

    def save(self, **kwargs):
        '''
        We overload this so that we don't inadverntently save multiple instances.
        Found I had to do this b/c the admin interface doesn't seem to use
        the *Manager.create method.  Rather, in creates an instance and then
        calls ``save``.
        '''
        fields = dict([(f.name, getattr(self, f.name)) \
                      for f in self._meta.fields \
                        if not f.is_relation and (getattr(self, f.name) is not None)])
        t = self.__class__.objects.filter(**fields)
        if t:
            raise IntegrityError('<{}: {}> already exists'.format(self.type, t))
        return super(self.__class__, self).save(**kwargs)


    @property
    def type(self):
        return self.__class__.name


class Fach(models.Model):
    name = models.CharField(max_length=40, verbose_name="Fach or style",
                            blank=True, null=False, default="")

    def __str__(self):
        return self.name

    __unicode__ = __str__

    class Meta:
        verbose_name_plural = "Fachs/Styles (Voice)"

    def save(self, **kwargs):
        '''
        We overload this so that we don't inadverntently save multiple instances.
        Found I had to do this b/c the admin interface doesn't seem to use
        the *Manager.create method.  Rather, in creates an instance and then
        calls ``save``.
        '''
        fields = dict([(f.name, getattr(self, f.name)) \
                      for f in self._meta.fields \
                        if not f.is_relation and (getattr(self, f.name) is not None)])
        t = self.__class__.objects.filter(**fields)
        if t:
            raise IntegrityError('<{}: {}> already exists'.format(self.type, t))
        if kwargs['name'] is None:
            kwargs['name'] = ''
        return super(self.__class__, self).save(**kwargs)

    @property
    def type(self):
        return self.__class__.name


class Singing(Talent):
    '''
    A subtype of Talent that gives additional details as to
    the singer's voice range (e.g. 'tenor') and fach ('e.g. lyric').
    '''

    class Meta:
        verbose_name_plural = "Singing"
        unique_together = ('voice', 'fach',)

    def __init__(self, *args, **kwargs):
        super(Singing, self).__init__(*args, category=TalentCategoryEnum.singing,
                                      **kwargs)

    voice = models.ForeignKey(Voice, verbose_name="Vocal Range or Type")
    fach = models.ForeignKey(Fach, verbose_name="Fach or Style",
                             null=False, blank=True)

    def __str__(self):
        return "{} ({})".format(self.voice, self.fach) \
                if str(self.fach) else str(self.voice)

    __unicode__ = __str__


class Instrument(models.Model):

    name = models.CharField(max_length=100, verbose_name="Instrument Name",
                            blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

    __unicode__ = __str__


class Orchestra(Talent):
    '''
    A virtual subtype of *Talent* whose musical instrument is something other than their voice.
    '''

    class Meta:
        verbose_name_plural = "Orchestra"

    instrument = models.ForeignKey(Instrument)

    def __init__(self, *args, **kwargs):
        super(Orchestra, self).__init__(*args, category=TalentCategoryEnum.instrument,
                                      **kwargs)

    def __str__(self):
        result = "{}: {}".format(super(Orchestra, self).__str__(), str(self.instrument))

    __unicode__ = __str__


class DancingStyle(models.Model):

    name = models.CharField(max_length=100, verbose_name="Dance Style",
                            blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

    __unicode__ = __str__


class Dancing(Talent):
    '''
    Included for completeness.  At this time I'm not really
    sure about what else to put in here.  Ideally there should perhaps
    be an enumeration field of some sort that allows a dancer to be
    listed as a subset of types.  (E.g. ballet, tap, and jazz).
    '''

    class Meta:
        verbose_name_plural = "Dancing"

    def __init__(self, *args, **kwargs):
        super(Dancing, self).__init__(*args, category=TalentCategoryEnum.dancing,
                                      **kwargs)

    style = models.ForeignKey(DancingStyle)

    def __str__(self):
        result = "{}: {}".format(super(Dancing, self).__str__(), str(self.style))

    __unicode__ = __str__


class Acting(Talent):
    '''
    This will include non-singing and non-dancing.

    This will be undefined until we can come up with
    attributes worth making it explicit.  Otherwise
    the Talent model sufficies.
    '''

    class Meta:
        verbose_name_plural = "Acting"

    def __init__(self, *args, **kwargs):
        super(Acting, self).__init__(*args, category=TalentCategoryEnum.acging,
                                      **kwargs)





