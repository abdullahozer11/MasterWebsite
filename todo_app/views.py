"""views.py. Create your views here."""
# pylint: disable=too-many-ancestors
# pylint: disable=no-member
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, TemplateView

from todo_app.forms import ListForm, ItemForm
from todo_app.models import ToDoList, ToDoItem


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """
    CustomLoginRequiredMixin
    This class handles the checks and controls of a non-authenticated user trying to access urls.
    """
    login_url = "todo:login"


class IndexView(CustomLoginRequiredMixin, ListView):
    """
    IndexView
    This view class views index page of todo_app.
    """
    model = ToDoList
    template_name = "todo_app/index.html"

    def get_queryset(self):
        """
        Get _todo lists of the authenticated user.
        :return:
        """
        return ToDoList.objects.filter(user=self.request.user)


class ItemListView(CustomLoginRequiredMixin, ListView):
    """
    ItemListView
    This view class views the detailed page of a _todo list.
    """
    model = ToDoItem
    template_name = "todo_app/list-detail.html"

    def get_queryset(self):
        """
        this method returns tasks of the selected _todo list.
        :return:
        """
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        """
        this method is overwritten to pass _todo_list as a context.
        """
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["pk"])
        return context


class ListAddView(CustomLoginRequiredMixin, CreateView):
    """
    ListAddView
    This view class views the form to create a new _todo list.
    """
    form_class = ListForm
    template_name = "todo_app/list-add.html"
    success_url = reverse_lazy("todo:index")

    def form_valid(self, form):
        """
        this method is overwritten in order to redirect error message if a list with the same name exists.
        :param form:
        :return:
        """
        form.instance.user = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            return HttpResponse("ERROR: List with this name already exists!")


class ItemAddView(CustomLoginRequiredMixin, CreateView):
    """
    ItemAddView
    This view class views the form to create a new _todo task.
    """
    form_class = ItemForm
    template_name = "todo_app/item-add.html"
    todo_list = None

    def dispatch(self, request, *args, **kwargs):
        """
        This method is overwritten to set todo_list class variable.
        :param request:
        :return:
        """
        self.todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        this method is overwritten to return _todo list title in the context.
        :return:
        """
        context = super().get_context_data()
        context["title"] = self.todo_list.title
        return context

    def get_success_url(self):
        """
        If successful detailed item page will be redirected.
        :return:
        """
        return reverse_lazy("todo:item-view", args=[self.kwargs["list_id"]])

    def get_initial(self):
        """
        todo_list initial data is set.
        :return:
        """
        initial = super().get_initial()
        initial["todo_list"] = self.todo_list
        return initial

    def form_valid(self, form):
        """
        form_valid is overwritten to save form with additional default data.
        :param form:
        :return:
        """
        model_instance = form.save(commit=False)
        model_instance.todo_list = self.todo_list
        model_instance.save()
        return HttpResponseRedirect(self.get_success_url())


class ItemUpdateView(CustomLoginRequiredMixin, UpdateView):
    """
    ItemUpdateView
    This view class views the form to update the _todo task.
    """
    form_class = ItemForm
    model = ToDoItem
    template_name = "todo_app/item-update.html"

    def get_context_data(self, **kwargs):
        """
        this method is overwritten to add task to the context.
        :return:
        """
        context = super().get_context_data()
        context["task"] = ToDoItem.objects.get(id=self.kwargs["pk"])
        return context

    def get_success_url(self):
        """
        if successful redirect to _todo_item details page.
        :return:
        """
        return reverse_lazy("todo:item-view", args=[self.kwargs["list_id"]])


class ListDeleteView(CustomLoginRequiredMixin, DeleteView):
    """
    ListDeleteView
    This view class deletes the _todo list.
    """
    model = ToDoList
    template_name = "todo_app/list-delete.html"

    def get_context_data(self, **kwargs):
        """
        this method is overwritten add toto_list to the context.
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context["todo_list"] = self.object
        return context

    def get_success_url(self):
        """
        if successful redirect to todo_app's index page.
        :return:
        """
        return reverse_lazy("todo:index")


class ItemDeleteView(CustomLoginRequiredMixin, DeleteView):
    """
    ItemDeleteView
    This view class deletes todo_item.
    """
    model = ToDoItem
    template_name = "todo_app/item-delete.html"

    def get_context_data(self, **kwargs):
        """
        this method is overwritten to add task to the context.
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context["task"] = self.object
        return context

    def get_success_url(self):
        """
        if successful redirect to _todo_item details page.
        :return:
        """
        return reverse_lazy("todo:item-view", args=[self.kwargs["list_id"]])


class NotLoggedAllow(UserPassesTestMixin):
    """
    NotLoggedAllow
    This class manages the checks if the user is authenticated.
    """
    login_url = reverse_lazy('todo:login')

    def test_func(self):
        """
        Check if user is authenticated.
        :return:
        """
        return not self.request.user.is_authenticated


class LoginPageView(NotLoggedAllow, LoginView):
    """
    This view class views the login page.
    """
    next_page = 'todo:index'
    template_name = 'todo_app/login.html'


class SignUpView(NotLoggedAllow, CreateView):
    """
    This view class views the sign up page.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy("todo:index")
    template_name = "todo_app/signup.html"


class LogoutView(CustomLoginRequiredMixin, TemplateView):
    """
    This view class logs out the user.
    """
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("todo:index"))


def about_view(request):
    """
    This view method views about page.
    :param request:
    :return:
    """
    return render(request, template_name="todo_app/about.html")
