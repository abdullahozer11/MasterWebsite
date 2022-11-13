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
from rest_framework import viewsets, permissions

from commerce_app.forms import ProfileForm, CustomerForm
from commerce_app.models import Product, Profile, OrderProduct
from commerce_app.serializers import ProductSerializer


class IndexView(ListView):
    template_name = "commerce_app/index.html"
    model = Product
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.all()


class AboutView(TemplateView):
    template_name = "commerce_app/about.html"
    extra_context = {'inner_page_header_title': 'About'}


class ContactView(SuccessMessageMixin, CreateView):
    form_class = CustomerForm
    template_name = "commerce_app/contact.html"
    success_url = reverse_lazy("contact")
    success_message = "Your customer contact form is saved successfully!"
    extra_context = {'inner_page_header_title': 'Contact Us'}


class ProductView(ListView):
    template_name = "commerce_app/product.html"
    model = Product
    paginate_by = 6
    extra_context = {'inner_page_header_title': 'Products'}

    def get_queryset(self):
        query = self.request.GET.get("q_search")
        if query:
            object_list = Product.objects.filter(name__icontains=query)
        else:
            object_list = Product.objects.all()
        return object_list


class ProductViewHtoL(ProductView):
    def get_queryset(self):
        object_list = super(ProductViewHtoL, self).get_queryset()
        return object_list.order_by('-price')

class ProductViewLtoH(ProductView):
    def get_queryset(self):
        object_list = super(ProductViewLtoH, self).get_queryset()
        return object_list.order_by('price')


class TestimonialView(TemplateView):
    template_name = "commerce_app/testimonial.html"
    extra_context = {'inner_page_header_title': 'Testimonial'}


class NotLoggedAllow(UserPassesTestMixin):
    login_url = '/login/'

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        return HttpResponseRedirect(reverse("login", kwargs={'message': 'Login is required !' }))


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = "commerce_app/profile.html"
    model = Profile
    form_class = ProfileForm
    login_url = '/login/'
    extra_context = {'inner_page_header_title': 'Profile'}

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        paginator = Paginator(Product.objects.filter(favorites__username__contains=self.request.user), 6)
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
    extra_context = {'inner_page_header_title': 'LOGIN'}


class SignupView(NotLoggedAllow, CreateView):
    form_class = UserCreationForm
    template_name = "commerce_app/registration/signup.html"
    extra_context = {'inner_page_header_title': 'SIGN UP'}

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
    extra_context = {'inner_page_header_title': 'Shopping Cart'}

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
    extra_context = {'inner_page_header_title': 'Checkout'}

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


def ItemFavorView(request, product_id):
    if request.user.is_authenticated:
        Product.objects.get(id=product_id).favorites.add(request.user)
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return reverse('login')

def ItemDefavorView(request, product_id):
    Product.objects.get(id=product_id).favorites.remove(request.user)
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

# create a viewset
class ProductViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Product.objects.all()

    # specify serializer to be used
    serializer_class = ProductSerializer

    # specify permission
    permission_classes = [permissions.IsAuthenticated]
