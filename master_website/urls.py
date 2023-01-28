import os

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from portfolio.views import PortfolioIndexView
from portfolio2.views import Portfolio2IndexView
from settings import local

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo_app.urls', namespace="todo")),
    path('commerce/', include('commerce_app.urls', namespace="commerce")),
    path('countdown/', include('countdown.urls', namespace="countdown")),
    path('old/', PortfolioIndexView.as_view(), name="portfolio"),
    path('', Portfolio2IndexView.as_view(), name="portfolio2"),
    # captcha
    path('captcha/', include('captcha.urls')),
    # rest_framework views
    path('api-auth/', include('rest_framework.urls')),
    # allauth urls
    path('accounts/', include('allauth.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
]

if os.getenv("LOCAL_DEV"):
    urlpatterns += static(local.MEDIA_URL, document_root=local.MEDIA_ROOT)
    urlpatterns += static(local.STATIC_URL, document_root=local.STATIC_ROOT)

# pylint: disable=invalid-name
handler404 = "master_website.views.page_not_found_view"
