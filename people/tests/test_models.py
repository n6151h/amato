from django.test import TestCase

from people.models import *
from talent.models import *

class PeopleTestCase(TestCase):

    def setUp(self):

        ato = Talent.objects.create(category=TalentCategoryEnum.acting)

        bw = Person.objects.create(firstname="Bruce", surname="Willis",
                              phone="5675805", email="bruce@red.org")
        bw.talents = [ato]
        bw.save()

        Person.objects.create(firstname="Helen", surname="Hayes",
                                email="helen@deceased.edu")

    def test_000(self):
        '''Basic attribute dereference'''

        bw = Person.objects.get(firstname="Bruce")
        self.assertEqual(bw.sorting_name, "Willis, Bruce")
        self.assertEqual(str(bw), "Bruce Willis")

class ArtistTestCase(TestCase):

    def setUp(self):

        st = Singing.objects.create(voice=VoiceTypeEnum.tenor)

        ra = Artist.objects.create(firstname="Roberto", surname="Alagna",
                              phone="", email="ralagna@operatest.com",
                              agent="Boldoni", headshot=None)
        ra.talents = [st]
        ra.save()

        ct = Singing.objects.create(voice=VoiceTypeEnum.soprano,
                                    fach=FachEnum.coloratura)

        kb = Artist.objects.create(firstname="Kathleen", surname="Battle",
                              phone="445-1212", email="kathy@battle.net",
                              agent="CAMI")
        kb.talents = [ct]
        kb.save()


    def test_000(self):

        ra = Artist.objects.get(surname="Alagna")
        self.assertEqual(ra.talents.first().category, TalentCategoryEnum.singing)
