from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from commerce_app.views import IndexView, AboutView, ContactView, ProductView, TestimonialView, ProfileView, \
    SignupView, LoginPageView, CartView, CartAddView, CartDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from eCommerce import settings

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('product/', ProductView.as_view(), name='product'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(next_page="index"), name='logout'),
    path('edit-profile/', ProfileView.as_view(extra_context={"edit": True}, success_url=reverse_lazy("profile")), name='edit-profile'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/<product_id>', CartAddView, name='cart-add'),
    path('cart/delete/<pk>', CartDeleteView, name='cart-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
