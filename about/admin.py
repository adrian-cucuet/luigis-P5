from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', )

    list_display = (
        'name',
        'date',
        'no_of_guests',
        'status',
        'created_on',
    )


admin.site.register(Reservation, ReservationAdmin)
