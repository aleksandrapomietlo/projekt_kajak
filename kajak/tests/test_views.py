from django.test import SimpleTestCase
from kajak.forms import ReservationForm

class TestForm(SimpleTestCase):

    def test_reservation_form_valid_data(self):
        form = ReservationForm(data={
            'route': 'trasa1',
            'date': '22.09.2023',
            'name': 'name',
            'surname': 'surname'
            'participants': 10,
            'kayaks': 5,
            'phone_number': 48796650325,
            'mail': 'test@test.com',
            'message': 'Witaj'
        })

        self.assertTrue(form.is_valid())

    def test_reservation_form_no_data(self):
        form = ReservationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 9)