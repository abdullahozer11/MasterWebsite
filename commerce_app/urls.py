from django.urls import path

from commerce_app.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]