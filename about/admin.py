from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', )

    list_display = (
        'created_on',
        'name',
        'date',
        'time',
        'no_of_guests',
        'status',
    )

    list_filter = ('created_on', 'date', 'time', 'status', )


admin.site.register(Reservation, ReservationAdmin)
