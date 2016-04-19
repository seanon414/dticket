from django import forms
from django.forms.fields import IntegerField, CharField


class HomePageForm(forms.Form):
    ticket_number = IntegerField(required=False,
                                 initial=0,
                                 min_value=0,
                                 widget=forms.HiddenInput())

    ticket_id = CharField(required=False)

    slack_username = CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(HomePageForm, self).__init__(*args, **kwargs)
