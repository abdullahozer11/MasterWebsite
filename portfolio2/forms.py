from django.forms import ModelForm

from portfolio2.models import CustomerFormModel


class CustomerForm(ModelForm):
    # pylint: disable=too-few-public-methods
    class Meta:
        """set class meta attributes here"""
        model = CustomerFormModel
        fields = '__all__'
