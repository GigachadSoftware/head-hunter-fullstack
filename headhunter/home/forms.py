from django import forms


class SignUpForm(forms.Form):
    phone_number = forms.CharField(max_length=16, required=True)
    city = forms.CharField(max_length=64, required=True)
    birthday = forms.DateField(required=True)
