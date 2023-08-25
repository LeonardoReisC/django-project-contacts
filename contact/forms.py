from django import forms
from django.core.exceptions import ValidationError

from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': '',
                'placeholder': 'name',
            }
        ),
        label='First name',
        help_text='Must contain only characters'
    )

    class Meta:
        model = models.Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
        )

    def clean(self):
        self.add_error(
            None,
            ValidationError(
                'Error message',
                code='invalid',
            )
        )

        return super().clean()