from django import forms
from .models import Reservation
from django.core.exceptions import ValidationError
from django.utils import timezone


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.ModelForm):
    # Validate date to be in the future
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < timezone.now().date():
            raise forms.ValidationError(message='Date cannot be in the past')
        return date

    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone',
                  'no_of_guests', 'date', 'time',)
        widgets = {'date': DateInput()}

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'name',
            'email': 'email',
            'phone': 'phone',
            'no_of_guests': 'guests',
            'date': 'Date',
            'time': 'Time',
        }

        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'no_of_guests': 'Guests (max 12)',
            'date': 'Preferred Date',
            'time': 'Preferred Time',
        }

        self.fields['name'].widget.attrs['autofocus'] = False
        for field in self.fields:
            placeholder = placeholders[field]
            if self.fields[field].required:
                placeholder = f'{placeholder} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = labels[field]
