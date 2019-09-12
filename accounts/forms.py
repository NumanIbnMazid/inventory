from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.template.defaultfilters import filesizeformat
from django.conf import settings
import datetime
import re
import os


# class DateInput(forms.DateInput):
#     input_type = 'date'


class CustomSignupForm(SignupForm):
    def signup(self, request, user):
        user.save()
        userprofile, created = self.get_or_create(user=user)
        user.userprofile.save()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name']


class UserProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs['instance'].user
        user_kwargs = kwargs.copy()
        user_kwargs['instance'] = self.user
        self.uf = UserForm(*args, **user_kwargs)

        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)

        self.fields.update(self.uf.fields)
        self.initial.update(self.uf.initial)

        self.fields['first_name'] = forms.CharField(required=False,
                                                    widget=forms.TextInput(attrs={'placeholder': 'Enter your first name...'}))
        self.fields['first_name'].widget.attrs.update({
            'id': 'profile_first_name',
            'maxlength': 15,
            'pattern': "^[A-Za-z.,\- ]{1,}$",
        })
        self.fields['last_name'] = forms.CharField(required=False,
                                                   widget=forms.TextInput(attrs={'placeholder': 'Enter your last name...'}))
        self.fields['last_name'].widget.attrs.update({
            'id': 'profile_last_name',
            'maxlength': 20,
            'pattern': "^[A-Za-z.,\- ]{1,}$"
        })
        self.fields['dob'].widget.attrs.update({
            'placeholder': 'Ex: 1996-02-27',
            'id': 'profile_dob',
        })
        self.fields['contact'] = forms.CharField(required=False,
                                                 widget=forms.TextInput())
        self.fields['contact'].widget.attrs.update({
            'id': 'profile_contact',
            'maxlength': 20,
        })
        self.fields['address'].widget.attrs.update({
            'id': 'profile_address',
            'rows': 2,
            'cols': 2,
            'placeholder': 'Enter your address',
            'maxlength': 100
        })
        self.fields['city'].widget.attrs.update({
            'id': 'profile_city',
            'placeholder': 'Enter city...',
            'maxlength': 25,
        })
        self.fields['state'].widget.attrs.update({
            'id': 'profile_state',
            'placeholder': 'Enter state...',
            'maxlength': 25,
        })
        self.fields['country'].widget.attrs.update({
            'id': 'profile_country',
            'placeholder': 'Select country...',
            'maxlength': 25,
        })
        self.fields['about'] = forms.CharField(required=False, max_length=250,
                                               widget=forms.Textarea(attrs={'rows': 2, 'cols': 2, 'placeholder': 'Enter more about you...'}))
        # Help Texts
        self.fields['first_name'].help_text = "Maximum length 15 and only these 'A-Za-z.,-' characters and spaces are allowed."
        self.fields['last_name'].help_text = "Maximum length 20 and only these 'A-Za-z.,-' characters and spaces are allowed."
        self.fields['gender'].help_text = 'Enter your Gender.'
        self.fields['dob'].help_text = 'Enter your Date of Birth.'
        self.fields['dob'].label = "Date of Birth"
        self.fields['contact'].help_text = 'Phone number must be valid and start with +880'
        self.fields['address'].help_text = 'Enter your Address.'
        self.fields['city'].help_text = 'Enter your City.'
        self.fields['state'].help_text = 'Enter your State.'
        self.fields['country'].help_text = 'Select your Country.'
        self.fields['about'].help_text = 'Enter More About You.'
        self.fields[
            'image'].help_text = 'Enter your Profile Picture. Only JPEG/JPG/PNG Files (Maximum 1.5 MB) are allowed.'

    class Meta:
        model = UserProfile
        fields = ['about', 'address', 'country',
                  'state', 'city', 'image', 'dob', 'contact', 'gender']

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if first_name != "":
            allowed_char = re.match(r'^[A-Za-z-., ]+$', first_name)
            length = len(first_name)
            if length > 15:
                raise forms.ValidationError("Maximum 15 characters allowed !")
            if not allowed_char:
                raise forms.ValidationError(
                    "Only 'A-Za-z.,-' these characters and spaces are allowed.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")
        if last_name != "":
            allowed_char = re.match(r'^[A-Za-z-., ]+$', last_name)
            length = len(last_name)
            if length > 20:
                raise forms.ValidationError("Maximum 20 characters allowed !")
            if not allowed_char:
                raise forms.ValidationError(
                    "Only 'A-Za-z.,-' these characters and spaces are allowed.")
        return last_name

    def clean_contact(self):
        contact = self.cleaned_data.get('contact')
        if contact != "":
            allowed_chars = re.match(r'^[0-9+]+$', contact)
            if not allowed_chars:
                raise forms.ValidationError(
                    "Only '+0-9' these characters and spaces are allowed.")
            length = len(contact)
            if length > 20:
                raise forms.ValidationError(
                    f"Maximum 20 characters allowed. [currently using: {length}]")
        return contact

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image == None and not image == False:
            image_extension = os.path.splitext(image.name)[1]
            allowed_image_types = settings.ALLOWED_IMAGE_TYPES
            if not image_extension in allowed_image_types:
                raise forms.ValidationError("Only %s file formats are supported! Current file format is %s" % (
                    allowed_image_types, image_extension))
            if image.size > settings.MAX_IMAGE_UPLOAD_SIZE:
                raise forms.ValidationError("Please keep filesize under %s. Current filesize %s" % (
                    filesizeformat(settings.MAX_IMAGE_UPLOAD_SIZE), filesizeformat(image.size)))
        return image

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if not dob == None:
            today = datetime.date.today()
            if dob > today:
                raise forms.ValidationError(
                    "Please enter valid Date of Birth. Date cannot be greater than today!")
        return dob

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if not address == None:
            length = len(address)
            if length > 100:
                raise forms.ValidationError(
                    f"Maximum 100 characters allowed. [currently using: {length}]")
        return address

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if not city == None:
            length = len(city)
            if length > 25:
                raise forms.ValidationError(
                    f"Maximum 25 characters allowed. [currently using: {length}]")
        return city

    def clean_state(self):
        state = self.cleaned_data.get('state')
        if not state == None:
            length = len(state)
            if length > 25:
                raise forms.ValidationError(
                    f"Maximum 25 characters allowed. [currently using: {length}]")
        return state

    def clean_country(self):
        country = self.cleaned_data.get('country')
        if not country == None:
            length = len(country)
            if length > 25:
                raise forms.ValidationError(
                    f"Maximum 25 characters allowed. [currently using: {length}]")
        return country

    def clean_about(self):
        about = self.cleaned_data.get('about')
        if not about == None:
            length = len(about)
            if length > 250:
                raise forms.ValidationError("Maximum 250 characters allowed !")
        return about


    def save(self, *args, **kwargs):
        self.uf.save(*args, **kwargs)
        return super(UserProfileUpdateForm, self).save(*args, **kwargs)
