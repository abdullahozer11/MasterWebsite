
# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "commerce_app/index.html"

class AboutView(TemplateView):
    template_name = "commerce_app/about.html"

class ContactView(TemplateView):
    template_name = "commerce_app/contact.html"

class ProductView(TemplateView):
    template_name = "commerce_app/product.html"

class TestimonialView(TemplateView):
    template_name = "commerce_app/testimonial.html"
