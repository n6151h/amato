from django.test import TestCase

from library.models import *

class BookTestCase(TestCase):

    def setUp(self):

        Book.objects.create(title="Death of a Salesman",
                            publisher="Doubleday",
                            published=1937,
                            synopsis="A salesman dies.  His family is sad.")

        Book.objects.create(title="You Can't Take it With You",
                            publisher="Penguin",
                            published=1928,
                            synopsis="Racist, xenophibic fun for all.")

    def test_000(self):
        '''Basic attribute dereferencing and manipulation'''

        b1 = Book.objects.get(title__startswith="Death")
        self.assertEqual(b1.published, 1937)

        b2 = Book.objects.get(published=1928)
        self.assertEqual(b2.title, "You Can't Take it With You")

    def test_001(self):
        '''str and unicode special methods'''

        b1 = Book.objects.get(title__startswith="Death")
        self.assertEqual(str(b1), 'Death of a Salesman (Doubleday)')


class ScriptTestCase(TestCase):

    def setUp(self):

        Script.objects.create(title="The Crucible",
                            publisher="Abner & Co",
                            published=1943,
                            author="Miller",
                            synopsis="Trying to tell which witch is which.")

        Script.objects.create(title="You Can't Take it With You",
                            publisher="Penguin",
                            author="Moss Hart",
                            published=1928,
                            synopsis="Racist, xenophibic fun for all.")

    def test_000(self):
        '''Basic attribute dereferencing and manipulation'''

        b1 = Script.objects.get(title="The Crucible")
        self.assertEqual(b1.published, 1943)
        self.assertEqual(b1.author, "Miller")


    def test_001(self):
        '''str and unicode special methods'''

        b1 = Script.objects.get(title="The Crucible")
        self.assertEqual(str(b1), 'The Crucible (Abner & Co)')


class MusicalTestCase(TestCase):

    def setUp(self):

        Musical.objects.create(title="Pajama Game",
                            publisher="Little Big Horn",
                            published=1957,
                            composer="Adler & Ross",
                            lyricist="Abbott & Bissell",
                            synopsis="Just knock 3x and say you were sent by 'Joe'.")

    def test_000(self):
        '''Basic attribute dereferencing and manipulation'''

        b1 = Musical.objects.get(title="Pajama Game")
        self.assertEqual(b1.published, 1957)
        self.assertNotEqual(b1.composer, "Miller")
        self.assertEqual(b1.lyricist, "Abbott & Bissell")


    def test_001(self):
        '''str and unicode special methods'''

        b1 = Musical.objects.get(published=1957)
        self.assertEqual(str(b1), 'Pajama Game (Little Big Horn)')


class OperaTestCase(TestCase):

    def setUp(self):

        Opera.objects.create(title="La Boheme",
                            publisher="Ricordi",
                            published=1896,
                            composer="Puccini",
                            librettist="Illica",
                            synopsis="Rodolfo's Worst. Year. Ever.")

    def test_000(self):
        '''Basic attribute dereferencing and manipulation'''

        b1 = Opera.objects.get(librettist="Illica")
        self.assertEqual(b1.published, 1896)
        self.assertEqual(b1.composer, "Puccini")


    def test_001(self):
        '''str and unicode special methods'''

        b1 = Opera.objects.get(published=1896)
        self.assertEqual(str(b1), "La Boheme (Ricordi)")


class RoleTestCase(TestCase):

    def setUp(self):

        mo = Musical.objects.create(title="Pajama Game",
                            publisher="Little Big Horn",
                            published=1957,
                            composer="Adler & Ross",
                            lyricist="Abbott & Bissell",
                            synopsis="Just knock 3x and say you were sent by 'Joe'.")

        Role.objects.create(name="Sid Sorokin",
                            description="the handsome new factory superintendent.",
                            book=mo,
                            role_type=RoleTypeEnum.singing)

        Role.objects.create(name='Katherine "Babe" Williams',
                            description="the leader of the Union Grievance Committee",
                            book=mo,
                            role_type=RoleTypeEnum.singing)

    def test_000(self):
        pjg = Musical.objects.get(title="Pajama Game")

        self.assertEqual(pjg.roles.count(), 2)


class OperaticRoleTestCase(TestCase):

    def setUp(self):

        oo = Opera.objects.create(title="Faust",
                            publisher="Schirmer",
                            published=1859,
                            composer="Gounod, Charles",
                            librettist="Barbier & Carre",
                            synopsis="A deal with the devil.  (You KNOW this won't end well.)")

        OperaticRole.objects.create(name="Faust",
                            description="Philosopher",
                            book=oo,
                            role_type=RoleTypeEnum.singing,
                            voice=VoiceTypeEnum.tenor,
                            fach=FachEnum.lyric)

        OperaticRole.objects.create(name="Marguerite",
                            description="Yourg woman adored by Faust",
                            book=oo,
                            role_type=RoleTypeEnum.singing,
                            voice=VoiceTypeEnum.soprano)

    def test_000(self):
        '''Basic attribute access'''

        f = Opera.objects.get(title="Faust")

        self.assertEqual(f.roles.count(), 2)

    def test_001(self):

        fo = Opera.objects.get(published=1859)

        # Get the roles as Role instances
        m = fo.roles.filter(operaticrole__voice=VoiceTypeEnum.soprano).first()
        f = fo.roles.filter(operaticrole__voice=VoiceTypeEnum.tenor).first()

        self.assertEqual(m.operaticrole.fach, FachEnum.unspecified)
        self.assertEqual(f.book, fo)

