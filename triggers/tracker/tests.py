"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from models import Thing,DataPoint


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ObjectsAndValuesTest(TestCase):
    def setUp(self):
        thing1 = Thing(name="Thing1")
        thing1.save()
        thing1 = Thing.objects.get(name="Thing1")

        thing2 = Thing(name="Thing2")
        thing2.save()
        thing2 = Thing.objects.get(name="Thing2")
        
        v = DataPoint(value={"state":"open"}, thing=thing1)
        v.save()
        v = DataPoint(value={"state":"closed"}, thing=thing1)
        v.save()
        v = DataPoint(value={"state":"frobbed"}, thing=thing1)
        v.save()
        v = DataPoint(value={"state":"blipped"}, thing=thing2)
        v.save()


    def tearDown(self):
        pass

    def test_get_latest_value(self):
        thing1 = Thing.objects.get(name='Thing1')
        latest = thing1.get_latest_value() 
        self.assertTrue(latest.value.has_key('state'))
        self.assertEqual(latest.value['state'], 'frobbed')

    def test_get_previous_change(self):
        thing1 = Thing.objects.get(name='Thing1')
        latest = thing1.get_previous_change() 
        self.assertTrue(latest.value.has_key('state'))
        self.assertEqual(latest.value['state'], 'closed')

