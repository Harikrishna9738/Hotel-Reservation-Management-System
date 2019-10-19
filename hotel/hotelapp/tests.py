from django.test import TestCase
from .models import  Guest,Room,Room_type,Manager,Booking


class GuestTestCase(TestCase):
    def setUp(self):
        Guest.objects.create(guest_name = 'hari',govt_id = 123, number_of_guest = 2,age = 23,contact = 12345678,
                             email = 'hari@gmail.com')


    def test_guest_name(self):
        guest = Guest.objects.get(guest_name='hari')
        guest = Guest.objects.get(govt_id=123)
        self.assertEqual(guest.guest_name,'hari')
        self.assertEqual(guest.govt_id, 123)


class RoomTestCase(TestCase):
    def setUp(self):
        room_t = Room_type.objects.create(classic = False,delux = False)
        Room.objects.create(room_number=101,room_type =room_t,  )

    def test_guest_name(self):
        room = Room.objects.get(room_number = 101)
        self.assertEqual(room.room_number,101)


class ManagerTestCase(TestCase):
    def setUp(self):
        room_t = Room_type.objects.create(classic = False,delux = False)
        rooom = Room.objects.create(room_number=101,room_type =room_t,  )
        guest =  Guest.objects.create(guest_name = 'hari',govt_id = 123, number_of_guest = 2,age = 23,contact = 12345678,
                             email = 'hari@gmail.com')
        Manager.objects.create(name = 'hari',room_nu =12 ,add_room = room_t,room_details = rooom,guest_details = guest)

    def test_guest_name(self):
        mana = Manager.objects.get(name = 'hari')
        self.assertEqual(mana.name,'hari')