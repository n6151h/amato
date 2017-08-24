from django.test import TestCase

from people.models import *
from talent.models import *

from django.db import transaction
from django.db.utils import IntegrityError


class TalentTestCast(TestCase):

    def setUp(self):
        Artist.objects.create(firstname="Ryan", surname="Gosling")
        Artist.objects.create(firstname="Emma", surname="Stone")


    def test_000(self):
        '''Populte the db with Talent instances'''

        for t in TalentCategoryEnum:
            Talent.objects.create(category=t)

        # So far, so good if we got here w/out problems.

        # Now try to add any one of these.  Should
        # raise a DB integrity error
        with transaction.atomic():
            self.assertRaises(IntegrityError,
                lambda: Talent.objects.create(category=TalentCategoryEnum.singing))

        # Delete this one and try again.
        st = Talent.objects.get(category=TalentCategoryEnum.singing)
        st.delete()

        with transaction.atomic():
            Talent.objects.create(category=TalentCategoryEnum.singing)

        # # Ryan is a really talented guy!
        ryan = Person.objects.get(surname="Gosling")

        for t in Talent.objects.filter(category__in=[TalentCategoryEnum.singing,
                                    TalentCategoryEnum.acting,
                                    TalentCategoryEnum.dancing]):
            ryan.talents.add(t)


        # Can Ryan act?
        self.assertTrue(Talent.objects.get(category=TalentCategoryEnum.acting) in ryan.talents.all())

        # Can he play an instrument?
        self.assertFalse(Talent.objects.get(category=TalentCategoryEnum.instrument) in ryan.talents.all())

        # See what the artists share (and what they don't)
        emma = Person.objects.get(surname="Stone")
        for t in Talent.objects.filter(category__in=[TalentCategoryEnum.singing,
                                    TalentCategoryEnum.acting,
                                    TalentCategoryEnum.dancing,
                                    TalentCategoryEnum.lighting,
                                    TalentCategoryEnum.instrument]):
            emma.talents.add(t)

        singers = Person.objects.filter(talents=Talent.objects.get(category=TalentCategoryEnum.singing))
        self.assertIn(ryan, singers)
        self.assertIn(emma, singers)
        self.assertEqual(len(singers), 2)


class SingingTestCase(TestCase):

    def setUp(self):


        Artist.objects.create(firstname="Ryan", surname="Gosling",
                                email="ryang@lala-land.com")

        Artist.objects.create(firstname="Emma", surname="Stone",
                                email="emmas@lala-land.com")


    def test_000(self):

        ryan = Artist.objects.get(surname="Gosling")
        emma = Artist.objects.get(email__startswith="emma")


