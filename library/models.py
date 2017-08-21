"""
Library
=======

Simply put, the library app is where we keep the "books" that relate to the
various productions.  For plays, a "book" is the script.  For operas, this is
the score, and so forth.   There are several subclasses of *Book* that add
or overload attributes relevant to the subclass.  For instance, the *Musical*
subclass has a _composer_ and a _lyricist_, whereas *Opera* objects have
_composer_ attributes but have a _librettist_ instead of a _lyricist_.

Roles
-----

Roles are related to books since they describe the characters who play
in the story, regardless of what type of story (i.e. *Book*) we're talking
about.  In the *schedule* models we relate *Role* to *Show* in the
*CastMember* model.

"""

from django.db import models
from django.utils.translation import ugettext_lazy as _
from enumchoicefield import ChoiceEnum, EnumChoiceField
from talent.models import VoiceTypeEnum, FachEnum

from django.core.validators import MaxValueValidator, MinValueValidator

class Book(models.Model):
    '''
    This is more or less an abstract class that can be subclassed to
    better describe the literary element specific to a given
    production type.
    '''
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    published = models.IntegerField(null=True, default=None,
       validators=[MinValueValidator(1300), ])
    synopsis = models.TextField()

    def __str__(self):
        return "{} ({})".format(self.title, self.publisher)

    def __unicode__(self):
        return "{} ({})".format(self.title, self.publisher)


class Script(Book):
    '''
    *Book* subclass for plays or other non-musical
    literary elements. Note, for instance, that a script
    has no _composer_ attribute.
    '''
    author = models.CharField(max_length=100)

class Musical(Book):
    '''
    *Book* subclass for musicalliterary elements.
    Here, we're talking about broadway musicals, as opposed
    to, say, operas or operettas.
    Note, for instance, that a musical
    has a composer and a lyracist, whereas a play has
    only an author.
    '''
    composer = models.CharField(max_length=100)
    lyricist = models.CharField(max_length=100)

class Opera(Book):
    '''
    Somewhat difficult to distinquish from a musical, this
    is provided mainly to keep librettists happy (or from
    spinning in their graves.)
    '''
    composer = models.CharField(max_length=100)
    librettist = models.CharField(max_length=100)

    # Where this is used in a dropdown (See serializers.OperaticRoleSerializer.book)
    # it will appear as "Opera object" on every dropdown line unless you
    # redefine the __unicode__ and __str__ magic methods.  We do this for both
    # See: https://stackoverflow.com/questions/34885381/see-description-in-django-rest-framework-dropdown
    def __unicode__(self):   # Need this for python 2
        return "{0.title} ({0.publisher})".format(self)

    def __str__(self):       # Need this for python 3
        return "{0.title} ({0.publisher})".format(self)

class Oratorio(Book):
    '''
    This class is included to contain other musical works
    including oratories, masses, and other performance works
    that are typically non-staged.
    '''
    composer = models.CharField(max_length=100)

class RoleTypeEnum(ChoiceEnum):
    speaking = "speaking"
    non_speaking = "non-speaking"
    singing = "singing"
    unspecified = "unspecified"

class Role(models.Model):
    '''
    This descripbes a member of an ensemble of actors in
    a given book.   A *Role* is matched up with a *CastMember*
    in the schedule app.   (See *CastMember* and *Show* models
    in the _schedule_ app.)
    '''
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, null=True, blank=True, default='')
    book = models.ForeignKey(Book, related_name='roles')
    role_type = EnumChoiceField(RoleTypeEnum,
                                default=RoleTypeEnum.unspecified)

    def __str__(self):
        return "{} ({})".format(self.name, self.description)

    def __unicode__(self):
        return "{} ({})".format(self.name, self.description)


class OperaticRole(Role):
    voice = EnumChoiceField(VoiceTypeEnum, default=VoiceTypeEnum.unspecified)
    fach = EnumChoiceField(FachEnum, default=FachEnum.unspecified)

    def __init__(self, *args, **kwargs):
        super(OperaticRole, self).__init__(*args, **kwargs)
        self._meta.get_field('role_type').default=RoleTypeEnum.singing

