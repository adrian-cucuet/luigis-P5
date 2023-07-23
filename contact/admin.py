from django.contrib import admin
from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    """ Display the Queries in the Admin Panel """

    list_display = ('created_at', 'department', 'name',
                    'email', 'subject', 'message',)

    list_filter = ('created_at', 'name', 'department')

    ordering = ('-created_at',)


admin.site.register(ContactUs, ContactUsAdmin)
