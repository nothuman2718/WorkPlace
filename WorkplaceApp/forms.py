from django import forms
from django.core.validators import RegexValidator

class StudentAccountForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=25, required=True)
    last_name = forms.CharField(label='Last Name', max_length=25, required=True)
    address = forms.CharField(label='Address', max_length=200, required=True)
    email = forms.EmailField(label='Enter Your Email', required=True)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message='Please enter a valid 10-digit phone number.')
    phone = forms.CharField(label='Contact Number', max_length=10, validators=[phone_regex])
    stupropic = forms.ImageField(label='Profile Picture', required=True)
    resume = forms.FileField(label='Resume', required=True)
    stupan = forms.ImageField(label='Pan Picture')
    stuaadhar = forms.ImageField(label='Aadhar Picture')
    uni = forms.CharField(label='University', max_length=50)
    degree = forms.CharField(label='Degree', max_length=20)
    acc = forms.URLField(label='LinkedIn Profile', required=False)  # Marked as not required
    username = forms.CharField(label='Username (for Workplace login)', max_length=20)
    password = forms.CharField(label='Password (for Workplace login)', widget=forms.PasswordInput)
    # ... other fields

    def clean(self):
        cleaned_data = super().clean()
        # Add custom validation logic here if needed
        return cleaned_data
