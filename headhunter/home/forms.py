from django import forms


class SignUpForm(forms.Form):
    phone_number = forms.CharField(max_length=16, required=True)
    city = forms.CharField(max_length=64, required=True)
    birthday = forms.DateField(required=True)


class NewSummaryForm(forms.Form):
    education = forms.CharField(max_length=1, required=True)
    profession = forms.CharField(max_length=64, required=True)
    city = forms.CharField(max_length=64, required=True)
    end_of_education = forms.DateField(required=True)
    skills = forms.CharField(max_length=256, required=True)
