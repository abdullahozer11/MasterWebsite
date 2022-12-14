"""This is eCommerce app urls file"""
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from rest_framework import routers

from commerce_app.views import IndexView, ContactView, ProductView, ProfileView, \
    SignupView, LoginPageView, CartView, CartAddView, RemoveCartItem, IncreaseCartItemCount, \
    DecreaseCartItemCount, ItemFavorView, CheckoutView, CheckoutAddDirectView, ItemDefavorView, ProductViewHtoL, \
    ProductViewLtoH, ProductViewSet

router = routers.DefaultRouter()
router.register(r'api/products/get', ProductViewSet)

app_name = "commerce"

urlpatterns = [
    # main views
    path('', IndexView.as_view(), name='index'),
    path('about/', TemplateView.as_view(template_name="commerce_app/about.html"), name='about'),
    path('disclaimer/', TemplateView.as_view(template_name='commerce_app/disclaimer.html'), name='disclaimer'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('testimonial/', TemplateView.as_view(template_name="commerce_app/testimonial.html"), name='testimonial'),
    # profile views
    path('profile/', ProfileView.as_view(), name='profile'),
    path('edit-profile/', ProfileView.as_view(extra_context={"edit": True},
                                              success_url=reverse_lazy("commerce:profile")), name='edit-profile'),
    # auth views
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page="commerce:index"), name='logout'),
    # product views
    path('product/', ProductView.as_view(), name='product'),
    path('product/htol', ProductViewHtoL.as_view(), name='product-htol'),
    path('product/ltoh/', ProductViewLtoH.as_view(), name='product-ltoh'),
    path('item-favor/<product_id>', ItemFavorView.as_view(), name='item-favor'),
    path('item-defavor/<product_id>', ItemDefavorView.as_view(), name='item-defavor'),
    # purchasing views
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<product_id>', CartAddView.as_view(), name='cart-add'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('checkout/add/<product_id>', CheckoutAddDirectView.as_view(), name='checkout-add'),
    path('cart/delete/<product_id>', RemoveCartItem.as_view(), name='cart-remove'),
    path('cart/increase/<product_id>', IncreaseCartItemCount.as_view(), name='item-increase'),
    path('cart/decrease/<product_id>', DecreaseCartItemCount.as_view(), name='item-decrease'),
]

urlpatterns += router.urls
