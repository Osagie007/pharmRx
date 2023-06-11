from django import forms
from .models import Paystack_CustomerInfo

class Paystack_CustomerInfoForm(forms.ModelForm):
    class Meta:
        model = Paystack_CustomerInfo
        fields = '__all__'


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    message = forms.CharField(widget=forms.Textarea)