# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, ListView

from commerce_app.forms import ProfileForm
from commerce_app.models import Product, Profile, OrderProduct, InventoryProduct


class IndexView(TemplateView):
    template_name = "commerce_app/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["product_list"] = InventoryProduct.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "commerce_app/about.html"


class ContactView(TemplateView):
    template_name = "commerce_app/contact.html"


class ProductView(ListView):
    template_name = "commerce_app/product.html"
    model = InventoryProduct
    paginate_by = 30


class TestimonialView(TemplateView):
    template_name = "commerce_app/testimonial.html"


class NotLoggedAllow(UserPassesTestMixin):
    login_url = '/login/'

    def test_func(self):
        return not self.request.user.is_authenticated


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = "commerce_app/profile.html"
    model = Profile
    form_class = ProfileForm
    login_url = '/login/'

    def get_object(self, queryset=None):
        return self.request.user.profile


class LoginPageView(NotLoggedAllow, LoginView):
    next_page = 'index'
    template_name = "commerce_app/registration/login.html"


class SignupView(NotLoggedAllow, CreateView):
    form_class = UserCreationForm
    template_name = "commerce_app/registration/signup.html"

    def get_success_url(self):
        return reverse_lazy("login")


class CartView(LoginRequiredMixin, ListView):
    template_name = "commerce_app/cart.html"
    model = OrderProduct

    def get_queryset(self):
        return OrderProduct.objects.filter(in_cart_quantity__gte=1)


def CartAddView(request, product_id):
    product = InventoryProduct.objects.get(id=product_id)
    order_product = take_order(request.user, product)
    order_product.save()
    return HttpResponseRedirect(reverse('cart'))


def take_order(user, product):
    return OrderProduct(
        user=user,
        name=product.name,
        price=product.price,
        photo=product.photo,
        color=product.color,
        size=product.size,
    )

def RemoveCartItem(request, product_id):
    cart_product = OrderProduct.objects.get(id=product_id)
    cart_product.delete()
    return HttpResponseRedirect(reverse('cart'))
