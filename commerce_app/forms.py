from captcha.fields import CaptchaField, CaptchaTextInput
from django.forms import ModelForm, Form

from commerce_app.models import Profile, CustomerFormModel


class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'commerce_app/custom_captcha.html'


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'role']


class CustomerForm(ModelForm):
    captcha = CaptchaField(widget=CustomCaptchaTextInput)
    class Meta:
        model = CustomerFormModel
        fields = '__all__'

