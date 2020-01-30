from django.shortcuts import render
from .models import Manager
from rest_framework import viewsets
from .serializers import *


# Create your views here.
class ManagerView(viewsets.ModelViewSet):
    serializer_class = ManagerSerialiser
    queryset = Manager.objects.all()

class BookingView(viewsets.ModelViewSet):
    serializer_class = BookingSerialiser
    queryset = Booking.objects.all()

class GuestView(viewsets.ModelViewSet):
    serializer_class = GuestSerialiser
    queryset = Guest.objects.all()