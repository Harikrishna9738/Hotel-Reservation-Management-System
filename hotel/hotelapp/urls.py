
from django.urls import path,include

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('managers',views.ManagerView)
router.register('booking',views.BookingView)
router.register('guest',views.GuestView)

urlpatterns = [
    path('',include(router.urls)),
]