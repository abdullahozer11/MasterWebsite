# Create your views here.
from datetime import datetime, timedelta

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from commerce_app.forms import ProfileForm, CustomerForm
from commerce_app.models import Product, Profile, OrderProduct


class IndexView(ListView):
    template_name = "commerce_app/index.html"
    model = Product
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.all().order_by('id')


class AboutView(TemplateView):
    template_name = "commerce_app/about.html"


class ContactView(SuccessMessageMixin, CreateView):
    form_class = CustomerForm
    template_name = "commerce_app/contact.html"
    success_url = reverse_lazy("contact")
    success_message = "Your customer contact form is saved successfully!"


class ProductView(ListView):
    template_name = "commerce_app/product.html"
    model = Product
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.all().order_by('id')


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

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        paginator = Paginator(Product.objects.filter(favorites__username__contains=self.request.user).order_by('id'), 6)
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)
        try:
            context['object_list'] = paginator.page(page_number)
        except PageNotAnInteger:
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            context['object_list'] = paginator.page(paginator.num_pages)
        return context


class LoginPageView(NotLoggedAllow, LoginView):
    next_page = 'index'
    template_name = "commerce_app/registration/login.html"


class SignupView(NotLoggedAllow, CreateView):
    form_class = UserCreationForm
    template_name = "commerce_app/registration/signup.html"

    def get_success_url(self):
        return reverse_lazy("login")


def get_cart_total():
    total = 0
    for obj in OrderProduct.objects.all():
        total += obj.get_total()
    return total

class CartView(LoginRequiredMixin, ListView):
    template_name = "commerce_app/cart.html"
    model = OrderProduct
    login_url = '/login/'

    def get_queryset(self):
        return OrderProduct.objects.filter(in_cart_quantity__gte=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CartView, self).get_context_data()
        context["cart_total"] = get_cart_total()
        context["delivery_min"] = (datetime.today() + timedelta(days=3)).strftime("%d.%m.%Y")
        context["delivery_max"] = (datetime.today() + timedelta(days=7)).strftime("%d.%m.%Y")
        return context


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = "commerce_app/checkout.html"

    def get_context_data(self, **kwargs):
        context = super(CheckoutView, self).get_context_data(**kwargs)
        context["cart_total"] = get_cart_total()
        return context

def CartAddView(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        order_product = OrderProduct.objects.filter(product=product)
        if order_product:
            order_product[0].in_cart_quantity += 1
            order_product[0].save()
        else:
            OrderProduct(user=request.user, product=product).save()
        return HttpResponseRedirect(reverse('cart'))
    else:
        return HttpResponseRedirect(reverse('login'))


def CheckoutAddDirectView(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        order_product = OrderProduct.objects.filter(product=product)
        if order_product:
            order_product[0].in_cart_quantity += 1
            order_product[0].save()
        else:
            OrderProduct(user=request.user, product=product).save()
        return HttpResponseRedirect(reverse('checkout'))
    else:
        return HttpResponseRedirect(reverse('login'))


def CartItemFavorView(request, product_id):
    OrderProduct.objects.get(id=product_id).product.favorites.add(request.user)
    return HttpResponseRedirect(reverse("cart"))

def ItemFavorView(request, product_id):
    Product.objects.get(id=product_id).favorites.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', '/'))

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