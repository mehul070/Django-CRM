from typing import Self
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name =forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)

        Self.fields['username'].widget.attrs['class'] = 'form-control'
        Self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        Self.fields['username'].label = ''
        Self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        Self.fields['password1'].widget.attrs['class'] = 'form-control'
        Self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        Self.fields['password1'].label = ''
        Self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        Self.fields['password2'].widget.attrs['class'] = 'form-control'
        Self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        Self.fields['password2'].label = ''
        Self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	
