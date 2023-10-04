import os

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView, TemplateView

from countdown.views import CountdownView
from portfolio2.views import Portfolio2IndexView
from settings import local


urlpatterns = [
    re_path('^admin/?', admin.site.urls),
    re_path('^todo_old/?', include('todo_app.urls', namespace="todo")),
    re_path(r'^todo/?$', TemplateView.as_view(template_name='todo_react.html'), name="todo_react"),
    re_path(r'^words/?$', TemplateView.as_view(template_name='word_game.html'), name="word_game"),
    re_path(r'^pacman/?$', TemplateView.as_view(template_name='pacman/index.html'), name="pacman"),
    re_path(r'^easter/?$', TemplateView.as_view(template_name='easter/index.html'), name="easter"),
    re_path(r'^lemonado/?$', TemplateView.as_view(template_name='lemonado/index.html'), name="lemonado"),
    re_path(r'^paris/?$', CountdownView.as_view(template_name='countdown/final_paris.html', name='ParisFinal'), name="paris-final"),
    re_path(r'^paris_old/?$', CountdownView.as_view(template_name='countdown/paris.html', name='Paris'), name="paris"),
    re_path(r'^istanbul/?$', CountdownView.as_view(template_name='countdown/istanbul.html', name='Istanbul'), name="istanbul"),
    re_path(r'^athens/?$', CountdownView.as_view(template_name='countdown/athens.html', name='Athens'), name="athens"),
    re_path(r'^toronto/?$', CountdownView.as_view(template_name='countdown/toronto.html', name='Toronto'), name="toronto"),
    re_path(r'^commerce/?', include('commerce_app.urls', namespace="commerce")),
    re_path(r'^words_api/?', include('word_game_api.urls', namespace="words_api")),
    path('', Portfolio2IndexView.as_view(), name="portfolio2"),
    # captcha
    re_path('^captcha/?', include('captcha.urls')),
    # allauth urls
    re_path('^accounts/?', include('allauth.urls')),
    re_path('^favicon.ico', RedirectView.as_view(url='/static/favicon.ico')),
    # "not found" URL
    re_path(r'^.*$', TemplateView.as_view(template_name='404.html'), name="404"),
]

if os.getenv("LOCAL_DEV"):
    urlpatterns += static(local.MEDIA_URL, document_root=local.MEDIA_ROOT)
    urlpatterns += static(local.STATIC_URL, document_root=local.STATIC_ROOT)

# pylint: disable=invalid-name
handler404 = "master_website.views.page_not_found_view"
