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


    def save(self, **kwargs):
        '''
        We overload this so that we don't inadverntently save multiple instances.
        Found I had to do this b/c the admin interface doesn't seem to use
        the TalentManager.create method.  Rather, in creates an instance and then
        calls ``save``.
        '''
        fields = dict([(f.name, getattr(self, f.name)) \
                      for f in self._meta.fields \
                        if not f.is_relation and (getattr(self, f.name) is not None)])
        t = self.__class__.objects.non_polymorphic().filter(**fields)
        if t:
            raise IntegrityError('<{}: {}> already exists'.format(self.__class__.__name__, t))
        return super(Talent, self).save(**kwargs)




# The following subclasses of Talent have specific, additional attributes.
# Other subclasses might be added later.  But, for now, an actor is and actor
# is an actor -- no specialities really need yet be encoded.  (With apologies
# to my fine and talented actor friends.)

class Singing(Talent):
    '''
    A subtype of Talent that gives additional details as to
    the singer's voice range (e.g. 'tenor') and fach ('e.g. lyric').
    '''

    def __init__(self, *args, **kwargs):
        super(Singing, self).__init__(*args, category=TalentCategoryEnum.singing,
                                      **kwargs)

    voice = EnumChoiceField(VoiceTypeEnum,
                            default=VoiceTypeEnum.unspecified,
                            verbose_name="Voice Type")
    fach = EnumChoiceField(FachEnum,
                           default=FachEnum.unspecified)

    def __str__(self):
        result = str(self.voice)
        if self.fach != FachEnum.unspecified:
            result += " ({})".format(self.fach)
        return result

    __unicode__ = __str__


class Orchestra(Talent):
    '''
    A virtual subtype of *Talent* whose musical instrument is something other than their voice.
    '''
    def __init__(self, *args, **kwargs):
        super(Singing, self).__init__(*args, category=TalentCategoryEnum.instrument,
                                      **kwargs)

    instrument = models.CharField(null=False, blank=True, max_length=40)


class Dancing(Talent):
    '''
    Included for completeness.  At this time I'm not really
    sure about what else to put in here.  Ideally there should perhaps
    be an enumeration field of some sort that allows a dancer to be
    listed as a subset of types.  (E.g. ballet, tap, and jazz).
    '''
    def __init__(self, *args, **kwargs):
        super(Singing, self).__init__(*args, category=TalentCategoryEnum.dancing,
                                      **kwargs)

    style = EnumChoiceField(DancingStyleEnum,
                            default = DancingStyleEnum.unspecified)

#class Acting(Talent):
#    '''
#    This will include non-singing and non-dancing.
#
#    This will be undefined until we can come up with
#    attributes worth making it explicit.  Otherwise
#    the Talent model sufficies.
#    '''




