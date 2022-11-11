from django.forms import ModelForm

from commerce_app.models import Profile, CustomerFormModel


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'role']


class CustomerForm(ModelForm):
    class Meta:
        model = CustomerFormModel
        fields = '__all__'
