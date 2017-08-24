from django.test import TestCase

from schedule.models import *
from people.models import *
from library.models import *
from company.models import *

from django.db import transaction
from django.db.utils import IntegrityError


class SeasonTestCase(TestCase):

    def setUp(self):
        self.co = Company.objects.create(name="New Dork City Opera")

    def test_000(self):
        '''Basic CRUD'''

        s1 = Season.objects.create(company=self.co,
                                   name="2017-2018",
                                   start_date='2017-09-01',
                                   end_date='2018-06-01')

        s1a = Season.objects.get(name="2017-2018")
        self.assertEqual(str(s1a), "{} ({})".format(str(self.co), s1a.name))

        # Test that we can access it from the company instance.
        self.assertIn(s1a, self.co.seasons.all())


class ProductionTestCase(TestCase):

    def setUp(self):
        self.co = Company.objects.create(name="New Dork City Opera")
        Season.objects.create(company=self.co,
                              name="2017-2018",
                              start_date='2017-09-01',
                              end_date='2018-06-01')
        Opera.objects.create(title="Don Giovanni",
                             composer="Mozart",
                             librettist="Da Ponte",
                             publisher="Ricordi",
                             published=1787)

    def test_000(self):
        '''Basic CRUD'''

        s = self.co.seasons.first()
        p = Production.objects.create(season=s,
                                      book=Book.objects.get(title="Don Giovanni"))

        self.assertIn(p, s.productions.all())




class CallTestCase(TestCase):
    def setUp(self):
        self.co = Company.objects.create(name="New Dork City Opera")

        s = Season.objects.create(company=self.co,
                              name="2017-2018",
                              start_date='2017-09-01',
                              end_date='2018-06-01')

        op = Opera.objects.create(title="Don Giovanni",
                             composer="Mozart",
                             librettist="Da Ponte",
                             publisher="Ricordi",
                             published=1787)

        p = Production.objects.create(season=s, book=op)

        Artist.objects.create(firstname="Ryan", surname="Gosling")
        Artist.objects.create(firstname="Emma", surname="Stone")


    def test_000(self):
        '''Basic CRUD'''

        p = Production.objects.get(book__title="Don Giovanni")

        c = Call.objects.create(dtg="2017-08-27 18:00",
                            duration="4:00:00",
                            location="Armadale Uniting",
                            production=p,
                            type=CallTypes.rehearsal)

        c.called.add(Artist.objects.get(surname="Gosling"))
        c.save()

        print (p.calls.all())


class ShowTestCase(TestCase):
    pass

class CastMemberTestCase(TestCase):
    pass




