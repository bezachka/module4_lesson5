from django import forms

class AdvertismentForm(forms.Form):
    title = forms.CharField(max_length=128, widget=forms.TextInput(attrs = {'class': 'form-control-lg'}))
    description = forms.CharField(widget=forms.Textarea(attrs = {'class': 'form-control form-contol-lg'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs = {'class': 'form-control form-control-lg'}))
    auction_test = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs = {'class': 'form-check-input'}))
    image = forms.ImageField(widget=forms.FileInput(attrs = {'class': 'form-control form-control-lg'}))