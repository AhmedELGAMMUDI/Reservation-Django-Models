from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.core.exceptions import ValidationError
import datetime
from res_app.models import Reservation,Rental
import unittest

class ReservationListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("reservation-list")
        
        self.rental_1 = Rental.objects.create(name="Ahmed")
        self.rental_2 = Rental.objects.create(name="Denisa")

        self.reservation_1 = Reservation.objects.create(
            rental_id=self.rental_1,
            checkin=datetime.date(2022, 1, 1),
            checkout=datetime.date(2022, 1, 1),
        )
        self.reservation_2 = Reservation.objects.create(
            rental_id=self.rental_1,
            checkin=datetime.date(2022, 1, 3),
            checkout=datetime.date(2022, 1, 4),
        )

        number_of_reservation = 11

        for reservation_id in range(1,number_of_reservation+1):
            checkin_day = reservation_id
            checkout_day = reservation_id + 1
            Reservation.objects.create(
                rental_id=self.rental_2,
                checkin=datetime.date(2022, 2, checkin_day),
                checkout=datetime.date(2022, 2, checkout_day),
            )
        
        
    def test_reservation_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
    def test_reservation_view_url_accessible_by_name(self):
        response = self.client.get(reverse('reservation-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_previous_id_reservation(self):
        reservation = Reservation.objects.filter(
                            checkin__lt=self.reservation_2.checkin,
                            rental_id=self.rental_1
                        ).last()
        response = self.client.get(reverse('reservation-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(reservation.id, 1) # check if the previous reservation for rental "Denisa" --> 1

    def test_reservation_is_ten(self):
        response = self.client.get(reverse('reservation-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['reservation_list']), 10)
    
    def test_lists_all_reservation(self):
        response = self.client.get(reverse('reservation-list')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        self.assertEqual(len(response.context['reservation_list']), 3)
    


    
    

