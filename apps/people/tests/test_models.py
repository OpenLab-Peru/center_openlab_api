# Python imports


# Django imports
from django.test import TestCase
from django.utils import timezone

# Third party apps imports
from model_mommy import mommy

# Local imports
from ..models import Person, Document


# Create your model tests here.
class PersonTestCase(TestCase):
    def setUp(self):
        self.person_1 = mommy.make(Person, _fill_optional=['born_date', 'sex'])
        self.person_2 = mommy.make(Person)

    def test_full_name_type_name(self):
        self.assertEqual(
            '{} {}, {}'.format(
                self.person_1.last_name_father, self.person_1.last_name_mother,
                self.person_1.name), self.person_1.__str__())
        self.assertEqual(
            '{} {}, {}'.format(
                self.person_2.last_name_father, self.person_2.last_name_mother,
                self.person_2.name), self.person_2.__str__())
        self.assertNotEqual(self.person_1.__str__(), self.person_2.__str__())
        self.assertNotEqual(
            self.person_1.full_name(), self.person_2.full_name())

    def test_age(self):
        today = timezone.now().date()
        if self.person_1.born_date:
            person_1_age = today - self.person_1.born_date
        else:
            person_1_age = None
        if self.person_2.born_date:
            person_2_age = today - self.person_2.born_date
        else:
            person_2_age = None
        self.assertEqual(person_1_age, self.person_1.age)
        self.assertEqual(person_2_age, self.person_2.age)

    def tearDown(self):
        self.person_1.delete()
        self.person_2.delete()


class DocumentTestCase(TestCase):
    def setUp(self):
        self.person_1 = mommy.make(Person, _fill_optional=['born_date', 'sex'])
        self.person_2 = mommy.make(Person)
        self.document_1 = mommy.make(Document, person=self.person_1)
        self.document_2 = mommy.make(Document, person=self.person_2)

    def test_full_name_type_name(self):
        self.assertEqual(
            '{} {}, {}'.format(
                self.document_1.person.last_name_father,
                self.document_1.person.last_name_mother,
                self.document_1.person.name), self.document_1.__str__())
        self.assertEqual(
            '{} {}, {}'.format(
                self.document_2.person.last_name_father,
                self.document_2.person.last_name_mother,
                self.document_2.person.name), self.document_2.__str__())

    def tearDown(self):
        self.person_1.delete()
        self.person_2.delete()
        self.document_1.delete()
        self.document_2.delete()
