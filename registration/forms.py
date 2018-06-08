from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()

from .models import SignUp

class RegisterForm(forms.Form):
    full_name = forms.CharField()
    primary_email    = forms.EmailField()
    secondry_email    = forms.EmailField(blank=True , null= True)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_primary_email(self):
        primary_email = self.cleaned_data.get('primary_email')
        qs = User.objects.filter(primary_email=primary_email)
        if qs.exists():
            raise forms.ValidationError("email is taken")

        return primary_email


    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Passwords must match.")
        return data
