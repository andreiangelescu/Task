from django import forms

from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import MyUser

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email', 'date_of_birth', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    #clean email field
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            MyUser._default_manager.get(email=email)
        except MyUser.DoesNotExist:
            return email
        raise forms.ValidationError('This email is already in use!')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.is_active = False
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

class ActivationForm(forms.Form):
    activation_field = forms.CharField(required=True)

    def activate_user(self, activation_key):
        if MyUser.objects.filter(activation_key=activation_key).exists():
            self.user = MyUser.objects.get(activation_key=activation_key)
            self.user.is_active = True
            self.user.save()
            return self.user
        else:
            return False

    def clean(self):
        user = self.activate_user(self.cleaned_data.get('activation_field'))
        if not user:
            raise forms.ValidationError('Activation key incorect!')
        return super(ActivationForm, self).clean()