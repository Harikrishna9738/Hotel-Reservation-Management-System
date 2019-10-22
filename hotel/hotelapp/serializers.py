from rest_framework import serializers
from .models import *



class ManagerSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('name','room_nu',)



class BookingSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('booking_id','check_in_date','check_out_date','price')


class GuestSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('guest_name','govt_id','number_of_guest')