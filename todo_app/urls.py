"""This is _todo app urls file"""
from django.urls import path

from todo_app.views import IndexView, ItemListView, ListAddView, ItemAddView, ItemUpdateView, ListDeleteView, \
    ItemDeleteView, SignUpView, about_view, LoginPageView, LogoutView

app_name = 'todo'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about', about_view, name="about"),
    path('list/add/', ListAddView.as_view(), name="list-add"),
    path('list/<pk>/', ItemListView.as_view(), name="item-view"),
    path('list/<pk>/delete/', ListDeleteView.as_view(), name="list-delete"),
    path('list/<int:list_id>/item/add/', ItemAddView.as_view(), name="item-add"),
    path('list/<int:list_id>/item/<pk>/update/', ItemUpdateView.as_view(), name="item-update"),
    path('list/<int:list_id>/item/<pk>/delete/', ItemDeleteView.as_view(), name="item-delete"),
    path('login/', LoginPageView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
