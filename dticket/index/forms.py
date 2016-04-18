from django import forms


class HomePageForm(forms.Form):
    ticket_number = forms.HiddenInput()
