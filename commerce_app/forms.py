"""This is forms.py of commerce_app. Create your model forms here."""
from captcha.fields import CaptchaField, CaptchaTextInput
from django.forms import ModelForm, ImageField, FileInput

from commerce_app.models import Profile, CustomerFormModel


class CustomCaptchaTextInput(CaptchaTextInput):
    """
    This custom captcha is created to customize the captcha widget.
    """
    template_name = 'commerce_app/custom_captcha.html'


class ProfileForm(ModelForm):
    """
    This form is created in order to update profile informations.
    """
    photo = ImageField(widget=FileInput)

    # pylint: disable=too-few-public-methods
    class Meta:
        """set class meta attributes here"""
        model = Profile
        exclude = ['user', 'role']


class CustomerForm(ModelForm):
    """
    This customer form is created to fill and save contact form in the contact page.
    """
    captcha = CaptchaField(widget=CustomCaptchaTextInput)

    # pylint: disable=too-few-public-methods
    class Meta:
        """set class meta attributes here"""
        model = CustomerFormModel
        fields = '__all__'
