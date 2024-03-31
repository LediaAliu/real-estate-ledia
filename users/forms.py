from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordResetForm as PasswordResetFormCore
from .models import Profile
from property.models import Property


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image"]


FIELDS = [
    "title",
    "property_status",
    "address",
    "city",
    "description",
    "category",
    "price",
    "bedrooms",
    "bathrooms",
    "garage",
    "sqm",
    "MainPhoto",
    "photo_1",
    "photo_2",
    "photo_3",
    "photo_4",
    "photo_5",
    "photo_6",
    "scr_map",
]


class CreatePropertyForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Street"}))
    description = forms.CharField(widget=forms.Textarea(attrs={"style": "resize:none;"}))
    city = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "e.g Tirane"}))


    class Meta:
        model = Property
        exclude = ["author", "views"]


class PasswordResetForm(PasswordResetFormCore):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(
        attrs={"autocomplete": "email"}
    ))

    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        """
        This method is inherating Django's core `send_mail` method from `PasswordResetForm` class
        """
        context['user'] = context['user'].id
        send_password_reset_email_task.delay(
            subject_template_name=subject_template_name, 
            email_template_name=email_template_name,
            context=context,
            from_email=from_email,
            to_email=to_email,
            html_email_template_name=html_email_template_name
        )