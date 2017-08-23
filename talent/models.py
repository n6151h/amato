from django.db import models
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

class Talent(models.Model):
    '''
    Describes a company members abilities.
    '''
    category = EnumChoiceField(TalentCategoryEnum,
                               default=TalentCategoryEnum.unspecified)

    def __str__(self):
        return self.category.name

    def __unicode__(self):
        return self.category.name

class Singing(Talent):
    '''
    A subtype of talent that includes musicians whose instrument is
    "voice".
    '''

    def __init__(self, *args, **kwargs):
        super(Singing, self).__init__(*args,
                        category=TalentCategoryEnum.singing, **kwargs)

    voice = EnumChoiceField(VoiceTypeEnum,
                            default=VoiceTypeEnum.unspecified,
                            verbose_name="Voice Type")
    fach = EnumChoiceField(FachEnum,
                           default=FachEnum.unspecified)

class Orchestra(Talent):
    '''
    A subtype of *Talent* whose musical instrument is something other than their voice.
    '''
    instrument = models.CharField(null=False, blank=True, max_length=40)


class Dancing(Talent):
    '''
    Included for completeness.  At this time I'm not really
    sure about what else to put in here.  Ideally there should perhaps
    be an enumeration field of some sort that allows a dancer to be
    listed as a subset of types.  (E.g. ballet, tap, and jazz).
    '''
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




