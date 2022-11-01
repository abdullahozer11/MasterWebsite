from django.forms import ModelForm

from commerce_app.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'photo', 'role']