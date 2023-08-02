from django import forms
from .models import Reservation
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'email', 'phone',
                  'no_of_guests', 'date', 'time',)
        widgets = {'date': DateInput()}
   
    def clean(self):
        cleaned_data = super(ReservationForm, self).clean()
        date = cleaned_data.get('date')
        no_of_guests = cleaned_data.get('no_of_guests')
        # Check if the date is in the past
        if date and date < date.today():
            raise forms.ValidationError("You can't book a table in the past")
        # Check if number_of_guests are not None and not small or equal to null
        if no_of_guests is not None and no_of_guests <= 0:
            raise forms.ValidationError('Number of guests must be greater than 0.')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'no_of_guests': 'Guests',
            'date': 'Date',
            'time': 'Time',
        }

        self.fields['name'].widget.attrs['autofocus'] = False
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
            self.fields[field].label = False
