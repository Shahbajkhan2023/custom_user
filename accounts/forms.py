# accounts/forms.py

from django import forms
from django.contrib.auth import get_user_model

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'phone_number', 'address']
