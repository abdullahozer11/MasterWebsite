import os

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView, TemplateView

from portfolio.views import PortfolioIndexView
from portfolio2.views import Portfolio2IndexView
from settings import local


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo_old/', include('todo_app.urls', namespace="todo")),
    path('todo/', TemplateView.as_view(template_name='todo_react.html'), name="todo_react"),
    path('words/', TemplateView.as_view(template_name='word_game.html'), name="word_game"),
    path('pacman/', TemplateView.as_view(template_name='pacman/index.html'), name="pacman"),
    path('easter/', TemplateView.as_view(template_name='easter/index.html'), name="easter"),
    path('commerce/', include('commerce_app.urls', namespace="commerce")),
    path('words_api/', include('word_game_api.urls', namespace="words_api")),
    path('countdown/', include('countdown.urls', namespace="countdown")),
    path('toronto/', include('toronto.urls', namespace="toronto")),
    path('old/', PortfolioIndexView.as_view(), name="portfolio"),
    path('', Portfolio2IndexView.as_view(), name="portfolio2"),
    # captcha
    path('captcha/', include('captcha.urls')),
    # allauth urls
    path('accounts/', include('allauth.urls')),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
]

if os.getenv("LOCAL_DEV"):
    urlpatterns += static(local.MEDIA_URL, document_root=local.MEDIA_ROOT)
    urlpatterns += static(local.STATIC_URL, document_root=local.STATIC_ROOT)

# pylint: disable=invalid-name
handler404 = "master_website.views.page_not_found_view"
