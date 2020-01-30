from django.db import models
from datetime import datetime,date

from django.db.models import CASCADE, signals
from django.dispatch import receiver


class Guest(models.Model):
    guest_name = models.CharField(max_length=50)
    govt_id = models.IntegerField(default=0)
    number_of_guest = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    contact = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return str(self.guest_name)+' ,'+str(self.govt_id)


class Room_type(models.Model):
    classic = models.BooleanField(default=False)
    delux = models.BooleanField(default=False)


    def __str__(self):
        return str(self.classic)


class Room(models.Model):
    room_number = models.IntegerField()
    room_type = models.ForeignKey(Room_type, on_delete=CASCADE)

    def __str__(self):
        return str(self.room_number)


class Manager(models.Model):
    name = models.CharField(max_length=100)
    room_nu = models.IntegerField(primary_key=True)
    add_room = models.ForeignKey(Room_type, on_delete=CASCADE)
    guest_details = models.ForeignKey(Guest, on_delete=CASCADE)
    room_details = models.ForeignKey(Room, on_delete=CASCADE)

    def __str__(self):
        return str(self.name)


class Booking(models.Model):

    booking_id = models.IntegerField()
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    cancel = models.BooleanField(default=False)
    Complete = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

    room = models.ForeignKey(Manager, on_delete=CASCADE)

    def __str__(self):
        return str(self.room)


    def cal(self ):
        total = (self.check_out_date - self.check_in_date).days
        total_amount = total * self.price
        return total_amount






# @receiver(signals.post_save, sender=Booking)
# def one(sender, instance, created, room_details=False, **kwargs):
#     if not instance.room_details:
#         if created:
#             room_details.complete == False
#             room_details.save()


