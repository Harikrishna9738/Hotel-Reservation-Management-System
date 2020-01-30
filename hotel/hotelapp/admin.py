from django.contrib import admin
from django import forms
from .models import Guest,Room_type,Room,Manager,Booking


class GuestAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GuestAdminForm, self).__init__(*args, **kwargs)

    def clean(self):
        number_of_guest = self.cleaned_data.get('number_of_guest')
        if number_of_guest >3:
            raise forms.ValidationError(f"can't be more than 3", code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(GuestAdminForm, self).save(commit=commit)



class GuestAdmin(admin.ModelAdmin):
    list_display = ('guest_name','govt_id','number_of_guest','age','contact','email')
    form = GuestAdminForm


admin.site.register(Guest,GuestAdmin)


class Room_typeAdmin(admin.ModelAdmin):
    list_display = ('classic','delux')


admin.site.register(Room_type,Room_typeAdmin )


class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number','room_type')



admin.site.register(Room,RoomAdmin )


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name','room_nu','add_room','room_details','guest_details')


admin.site.register(Manager,ManagerAdmin )

class FormBookingAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormBookingAdmin, self).__init__(*args, **kwargs)


    def clean(self):
        room1 = self.cleaned_data.get('room')
        if room1.guest_details.govt_id > 1 :
            raise forms.ValidationError(f'you can book only one room', code='invalid')

        return self.cleaned_data

    def save(self, commit=True):
        return super(FormBookingAdmin, self).save(commit=commit)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id','check_in_date','check_out_date','cancel','Complete','price','room','cal')
    # form = FormBookingAdmin



admin.site.register(Booking,BookingAdmin )


