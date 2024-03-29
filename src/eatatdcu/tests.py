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

class A2Tests(TestCase):

    def test_webservice(self):
        """Test calling of webservice for each restaurant 
        """
        for restaurant in ['main restaurant','1838','nubar restaurant','canteen']:
           self.webservice(restaurant)

    def test_invalid_name(self):
        """ Test calling webservice for invalid restaurant 
        """
        response = self.client.get(reverse('eatatdcu:specials',kwargs={'restaurant':'1839'}))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Restaurant name')
        self.assertContains(response,'is unknown')

    def webservice(self, rest):
        """ Test calling webservice for individual restaurant
        """
        response = self.client.get(reverse('eatatdcu:specials',kwargs={'restaurant':rest}))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, rest)
        self.assertNotContains(response,'An error has occurred')


class A3Tests(TestCase):

    def setup(self):
        """
        Sets up a test database 
        """
        campus1 = Campus(1,'test campus')
        rest1 = Restaurant(1, 'test r1','student centre',1,time(hour=8),time(hour=17),750)
        rest2 = Restaurant(2, 'test r2','ballymun road',1,time(hour=9),time(hour=18),250)
        campus1.save()
        rest1.save()
        rest2.save()

    def part2_setup(self):
        """
        Sets up a test database - for testing part two
        """
        campus1 = Campus(1,'test campus')
        campus2 = Campus(2,'another test campus')
        rest1 = Restaurant(1, 'test r1','student centre',1,time(hour=8),time(hour=17),750,False)
        rest2 = Restaurant(2, 'test r2','ballymun road',1,time(hour=9),time(hour=18),250,True)
        rest3 = Restaurant(3, 'test r3','in library',1,time(hour=10),time(hour=17),300,False)
        rest4 = Restaurant(4, 'test r4','beside entrance',2,time(hour=10),time(hour=16),200,True)
        campus1.save()
        campus2.save()
        rest1.save()
        rest2.save()
        rest3.save()
        rest4.save()

    def part3_setup(self):
        """
        Sets up a test database - for testing part three
        """
        campus1 = Campus(1,'test campus')
        campus2 = Campus(2,'another test campus')
        campus3 = Campus(3,'yet another test campus')
        rest1 = Restaurant(1, 'test r1','student centre',1,time(hour=8),time(hour=16),750,False,True,time(hour=7,minute=15),time(hour=17,minute=34))
        rest2 = Restaurant(2, 'test r2','ballymun road',1,time(hour=9),time(hour=18),250,False,True,time(hour=6,minute=12),time(hour=19,minute=42))
        rest3 = Restaurant(3, 'test r3','in library',2,time(hour=10),time(hour=17),300)
        rest4 = Restaurant(4, 'test r4','beside entrance',3,time(hour=10),time(hour=16),200,True,False)
        campus1.save()
        campus2.save()
        campus3.save()
        rest1.save()
        rest2.save()
        rest3.save()
        rest4.save()

    def test_show_opening(self):
        """ Test restaurant opening hours are displayed """
        self.setup()
        response = self.client.get(reverse('eatatdcu:restaurants'),{'campus':'test campus'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'8')
        self.assertContains(response,'5')

    def test_rest_staff_only(self):
        """ Test for staff only message """
        self.part2_setup()
        response = self.client.get(reverse('eatatdcu:restaurants'),{'campus':'another test campus'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'(staff only!)')

    def test_rest_open_weekends(self):
        self.part3_setup()
        response = self.client.get(reverse('eatatdcu:restaurants'),{'campus':'test campus'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'7:15 a.m.')
        self.assertContains(response, '5:34 p.m.')
   
    def test_rest_closed_weekends(self):
        self.part3_setup()
        response = self.client.get(reverse('eatatdcu:restaurants'),{'campus':'another test campus'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'closed weekends')
        self.assertNotContains(response, '12 a.m.')

