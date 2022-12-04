"""master_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from master_website import settings
from portfolio.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo_app.urls', namespace="todo")),
    path('commerce/', include('commerce_app.urls', namespace="commerce")),
    path('', IndexView.as_view(), name="portfolio"),
    # captcha
    path('captcha/', include('captcha.urls')),
    # rest_framework views
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# pylint: disable=invalid-name
handler404 = "master_website.views.page_not_found_view"
