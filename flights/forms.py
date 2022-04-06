from django import forms


class FlightForm(forms.Form):
    origin = forms.CharField(label='Origin Airport Code')
    destination = forms.CharField(label='Destination Airport Code')
