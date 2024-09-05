# forms.py
from django import forms
from .models import Contact,Donation
from .models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'image', 'description', 'age', 'breed', 'adoption_fee', 'sex', 'color', 'size']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone_number', 'address', 'message']

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'email', 'amount']

class AdoptionForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(required=False, max_length=15)
    message = forms.CharField(widget=forms.Textarea)
