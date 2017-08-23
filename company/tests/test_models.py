from django.test import TestCase

from company.models import *

class CompanyTestCase(TestCase):

    def setUp(self):

        Company.objects.create(name="Amato Opera Theatre")
        Company.objects.create(name="Metropolitan Opera")
        Company.objects.create(name="La Scala")

    def test_000(self):
        '''Basic attribute dereference'''

        aot = Company.objects.get(name__startswith="Metro")
        self.assertEqual(str(aot), "Metropolitan Opera")

