from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    """ Form for contact page """

    class Meta:

        model = ContactUs
        fields = ('department', 'name', 'email',
                  'subject', 'message', )

        widgets = {'message': forms.Textarea(attrs={'rows': 5}), }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'department': 'Department',
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }
        excluded_fields = ['department', 'message']

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
