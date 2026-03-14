from django.test import TestCase 
from .models import *
# Create your tests here.

class FlightTestCase(TestCase):
    def setUp(self):
        a1=Airport.objects.create(city="City A",code="AAA")
        a2=Airport.objects.create(city="City B",code="BBB")
        Flight.objects.create(origin=a1,destination=a1,duration=100)
        Flight.objects.create(origin=a1,destination=a1,duration=120)
        Flight.objects.create(origin=a1,destination=a2,duration=-100)

    def test_departure_count(self):
        a=Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(),3)

    def test_arrival_count(self):
        a=Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(),2)

    def test_valid_flight(self):
        a1=Airport.objects.get(code="AAA")
        a2=Airport.objects.get(code="BBB")
        f=Flight.objects.get(origin=a1,destination=a2,duration=-100)  
        self.assertFalse(f.is_valid_flight())          


    