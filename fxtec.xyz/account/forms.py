from django import forms

class LogInForm(forms.Form):
    email = forms.EmailField(label="EMAIL", max_length=20)
    password = forms.CharField(label="PASSWORD", widget=forms.PasswordInput())
