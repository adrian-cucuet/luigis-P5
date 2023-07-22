from django import forms
from .models import Reservation


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.ModelForm):
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
                'name': 'Name',
                'email': 'Email',
                'phone': 'Phone',
                'no_of_guests': 'Guests',
                'time': 'Choose time',
                'date': 'dd/mm/yy',
            }

            self.fields['name'].widget.attrs['autofocus'] = True
            for field_name, field in self.fields.items():
                self.fields[field_name].widget.attrs['placeholder'] = field.label
            for field in self.fields:
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['class'] = 'lp-group-input reservation-form-input'
                self.fields[field].label = False
