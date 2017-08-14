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


class Book(models.Model):
    '''
    This is more or less an abstract class that can be subclassed to
    better describe the literary element specific to a given
    production type.
    '''
    title = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    pub_date = models.DateField()
    synopsis = models.TextField()

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

class Oratorio(Book):
    '''
    This class is included to contain other musical works
    including oratories, masses, and other performance works
    that are typically non-staged.
    '''
    composer = models.CharField(max_length=100)

class Role(models.Model):
    '''
    This descripbes a member of an ensemble of actors in
    a given book.   A *Role* is matched up with a *CastMember*
    in the schedule app.   (See *CastMember* and *Show* models
    in the _schedule_ app.)
    '''
    SPEAKING = 1
    NON_SPEAKING = 2
    SINGING = 3
    UNSPECIFIED = 0

    ROLE_TYPES = (
                  (SPEAKING, _("speaking")),
                  (NON_SPEAKING, _("non-speakng")),
                  (SINGING, _("singing")),
                  (UNSPECIFIED, _("unspecified")),
                  )

    name = models.CharField(max_length=50)
    book = models.ForeignKey(Book, related_name='roles')
    type = models.IntegerField(choices=ROLE_TYPES, verbose_name="Type",
                               default=UNSPECIFIED)

