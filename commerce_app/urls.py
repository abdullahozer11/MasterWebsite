from django.urls import path

from commerce_app.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('', ContactView.as_view(), name='contact'),
    path('', ProductView.as_view(), name='product'),
    path('', TestimonialView.as_view(), name='testimonial'),
]