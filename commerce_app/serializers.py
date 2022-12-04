"""serializers.py. Create your Serializers here. """
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    ProductSerializer
    Serialize Product model and serve it through API.
    """

    # pylint: disable=too-few-public-methods
    class Meta:
        """set class meta attributes here"""
        model = Product
        exclude = ['photo']
