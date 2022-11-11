# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, ListView

from commerce_app.forms import ProfileForm
from commerce_app.models import Product, Profile, OrderProduct


class IndexView(TemplateView):
    template_name = "commerce_app/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["product_list"] = Product.objects.all()
        return context


class AboutView(TemplateView):
    template_name = "commerce_app/about.html"


class ContactView(TemplateView):
    template_name = "commerce_app/contact.html"


class ProductView(ListView):
    template_name = "commerce_app/product.html"
    model = Product
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
    paginate_by = 5
    login_url = '/login/'

    def get_queryset(self):
        return OrderProduct.objects.filter(in_cart_quantity__gte=1)


def CartAddView(request, product_id):
    product = Product.objects.get(id=product_id)
    order_product = OrderProduct.objects.filter(product=product)
    if order_product:
        order_product.in_cart_quantity += 1
    else:
        OrderProduct(user=request.user, product=product).save()
    return HttpResponseRedirect(reverse('cart'))


def take_order(user, product):
    return OrderProduct(user=user, product=product)

def CartItemFavorView(request, product_id):
    OrderProduct.objects.get(id=product_id).product.favourites.add(request.user)
    return HttpResponseRedirect(redirect_to="#")

def ItemFavorView(request, product_id):
    Product.objects.get(id=product_id).favourites.add(request.user)

def IncreaseCartItemCount(request, product_id):
    cart_product = OrderProduct.objects.get(id=product_id)
    cart_product.in_cart_quantity += 1
    cart_product.save()
    return HttpResponseRedirect(reverse('cart'))

def DecreaseCartItemCount(request, product_id):
    cart_product = OrderProduct.objects.get(id=product_id)
    if cart_product.in_cart_quantity == 1:
        cart_product.delete()
    else:
        cart_product.in_cart_quantity -= 1
        cart_product.save()
    return HttpResponseRedirect(reverse('cart'))

def RemoveCartItem(request, product_id):
    cart_product = OrderProduct.objects.get(id=product_id)
    cart_product.delete()
    return HttpResponseRedirect(reverse('cart'))