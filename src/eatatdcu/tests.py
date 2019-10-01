from django.test import TestCase
from django.urls import reverse
from eatatdcu.models import Campus,Restaurant
from datetime import time

class A0Tests(TestCase):

    def test_welcome(self):
      """
      The index page loads and an appropriate welcome message is displayed
      """
      response = self.client.get(reverse('eatatdcu:index'))
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, "Eat at DCU!")

    #def test_restaurants(self):
    #  """
    #  The restaurants page loads 
    #  """
    #  response = self.client.get(reverse('eatatdcu:restaurants'))
    #  self.assertEqual(response.status_code, 200)

class A1Tests(TestCase):

    def setup(self):
        """
        Sets up a test database 
        """
        campus1 = Campus(1,'test campus')
        campus2 = Campus(2,'another test campus')
        campus3 = Campus(3,'yet another test campus')
        rest1 = Restaurant(1, 'test r1','student centre',1,time(hour=8),time(hour=17),750)
        rest2 = Restaurant(2, 'test r2','ballymun road',1,time(hour=9),time(hour=18),250)
        rest3 = Restaurant(3, 'test r3','in library',1,time(hour=10),time(hour=17),300)
        rest4 = Restaurant(4, 'test r4','beside entrance',3,time(hour=10),time(hour=16),200)
        campus1.save()
        campus2.save()
        campus3.save()
        rest1.save()
        rest2.save()
        rest3.save()
        rest4.save()

    def test_rest_retrieval(self):
        """ 
        Test retrieval of restaurants for a campus
        """
        self.setup()
        response = self.client.get(reverse('eatatdcu:restaurants'),{'campus':'test campus'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'r1')
        self.assertContains(response,'r2')
        self.assertContains(response,'r3')

    def test_rest_retrieval_case(self):
        """ Test retrieval of restaurants for a campus (case-insensitive)"""
        self.setup()
        response = self.client.get(reverse('eatatdcu:restaurants'),{'campus':'Test Campus'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'r1')
        self.assertContains(response,'r2')
        self.assertContains(response,'r3')
    
    def test_rest_empty_retrieval(self):
        """ Test empty retrieval of restaurants for a campus """
        self.setup()
        response = self.client.get(reverse('eatatdcu:restaurants'),{'campus':'another test campus'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'No restaurants found')

    def test_rest_retrieval_invalid(self):
        """ Test retrieval of restaurants for an invalid campus """
        self.setup()
        response = self.client.get(reverse('eatatdcu:restaurants'),{'campus':'invalid campus'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'No such campus')

