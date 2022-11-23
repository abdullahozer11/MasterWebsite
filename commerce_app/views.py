# Create your views here.
from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, UpdateView, ListView
from rest_framework import viewsets, permissions

from commerce_app.forms import ProfileForm, CustomerForm
from commerce_app.models import Product, Profile, OrderProduct
from commerce_app.serializers import ProductSerializer

LOGIN_REQUIRED_MESSAGE = 'Login is required for the action!'


class IndexView(ListView):
    template_name = "commerce_app/index.html"
    model = Product
    paginate_by = 6


class ContactView(SuccessMessageMixin, CreateView):
    form_class = CustomerForm
    template_name = "commerce_app/contact.html"
    success_url = reverse_lazy("commerce:contact")

    def form_valid(self, form):
        subject = "Website Inquiry"
        body = {
            'name': form.cleaned_data['name'],
            'email': form.cleaned_data['email'],
            'subject': form.cleaned_data['subject'],
            'message': form.cleaned_data['message'],
        }
        message = "\n".join(body.values())
        try:
            send_mail(subject, message, 'abdullahdrive1@gmail.com', ['abdullahozer11@hotmail.com'])
            messages.add_message(self.request, messages.SUCCESS, "Your customer contact form is saved successfully!")
        except BadHeaderError:
            messages.add_message(self.request, messages.ERROR, "Bad Header Error")
        response = super().form_valid(form)
        return response


class ProductView(ListView):
    template_name = "commerce_app/product.html"
    model = Product
    paginate_by = 6

    def get_queryset(self):
        object_list = super().get_queryset()
        query = self.request.GET.get("q_search")
        if query:
            object_list = Product.objects.filter(name__icontains=query)
        return object_list


class ProductViewHtoL(ProductView):
    def get_queryset(self):
        object_list = super().get_queryset()
        return object_list.order_by('-price')


class ProductViewLtoH(ProductView):
    def get_queryset(self):
        object_list = super().get_queryset()
        return object_list.order_by('price')


class NotLoggedAllow(UserPassesTestMixin):
    login_url = 'commerce:login'

    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.add_message(self.request, messages.ERROR, 'You must log out first!')
        super().handle_no_permission()


class CustomLoginRequiredMixin(LoginRequiredMixin):
    login_url = 'commerce:login'

    def handle_no_permission(self):
        messages.add_message(self.request, messages.INFO, LOGIN_REQUIRED_MESSAGE)
        return HttpResponseRedirect(reverse(self.login_url))


class ProfileView(CustomLoginRequiredMixin, UpdateView):
    template_name = "commerce_app/profile.html"
    model = Profile
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
    next_page = 'commerce:index'
    template_name = "commerce_app/registration/login.html"


class SignupView(NotLoggedAllow, CreateView):
    form_class = UserCreationForm
    template_name = "commerce_app/registration/signup.html"

    def get_success_url(self):
        return reverse_lazy("commerce:login")


def get_cart_total():
    total = 0
    for obj in OrderProduct.objects.all():
        total += obj.get_total()
    return total


class CartView(CustomLoginRequiredMixin, ListView):
    template_name = "commerce_app/cart.html"
    model = OrderProduct

    def get_queryset(self):
        return OrderProduct.objects.filter(in_cart_quantity__gte=1)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context["cart_total"] = get_cart_total()
        context["delivery_min"] = (datetime.today() + timedelta(days=3)).strftime("%d.%m.%Y")
        context["delivery_max"] = (datetime.today() + timedelta(days=7)).strftime("%d.%m.%Y")
        return context


class CheckoutView(CustomLoginRequiredMixin, TemplateView):
    template_name = "commerce_app/checkout.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart_total"] = get_cart_total()
        return context

class CartAddView(CustomLoginRequiredMixin, View):
    success_url = "commerce:cart"

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            product = Product.objects.get(id=kwargs['product_id'])
            order_product = OrderProduct.objects.filter(product=product)
            if order_product:
                order_product[0].in_cart_quantity += 1
                order_product[0].save()
            else:
                OrderProduct(user=self.request.user, product=product).save()
            return HttpResponseRedirect(reverse(self.success_url))
        else:
            messages.add_message(self.request, messages.INFO, LOGIN_REQUIRED_MESSAGE)
            return redirect(self.request.META.get('HTTP_REFERER', '/'))


class CheckoutAddDirectView(CartAddView):
    success_url = "commerce:checkout"


class ItemFavorView(CustomLoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            Product.objects.get(id=kwargs['product_id']).favorites.add(self.request.user)
        else:
            messages.add_message(self.request, messages.INFO, LOGIN_REQUIRED_MESSAGE)
        return redirect(self.request.META.get('HTTP_REFERER', '/'))


class ItemDefavorView(CustomLoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        Product.objects.get(id=kwargs['product_id']).favorites.remove(self.request.user)
        return redirect(self.request.META.get('HTTP_REFERER', '/'))


class IncreaseCartItemCount(CustomLoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        cart_product = OrderProduct.objects.get(id=kwargs['product_id'])
        cart_product.in_cart_quantity += 1
        cart_product.save()
        return HttpResponseRedirect(reverse('commerce:cart'))


class DecreaseCartItemCount(CustomLoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        cart_product = OrderProduct.objects.get(id=kwargs['product_id'])
        if cart_product.in_cart_quantity == 1:
            cart_product.delete()
        else:
            cart_product.in_cart_quantity -= 1
            cart_product.save()
        return HttpResponseRedirect(reverse('commerce:cart'))


class RemoveCartItem(CustomLoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        cart_product = OrderProduct.objects.get(id=kwargs['product_id'])
        cart_product.delete()
        return HttpResponseRedirect(reverse('commerce:cart'))


# create a viewset
class ProductViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Product.objects.all()
    # specify serializer to be used
    serializer_class = ProductSerializer
    # specify permission
    permission_classes = [permissions.IsAuthenticated]
