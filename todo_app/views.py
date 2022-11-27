# Create your views here.
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


class IndexView(LoginRequiredMixin, ListView):
    model = ToDoList
    template_name = "todo_app/index.html"
    login_url = "todo:login"

    def get_queryset(self):
        return ToDoList.objects.filter(user=self.request.user)


class ItemListView(LoginRequiredMixin, ListView):
    model = ToDoItem
    template_name = "todo_app/list-detail.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["pk"])

    def get_context_data(self):
        context = super(ItemListView, self).get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["pk"])
        return context


class ListAddView(LoginRequiredMixin, CreateView):
    form_class = ListForm
    template_name = "todo_app/list-add.html"
    success_url = reverse_lazy("todo:index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        try:
            return super(ListAddView, self).form_valid(form)
        except IntegrityError:
            return HttpResponse("ERROR: List with this name already exists!")


class ItemAddView(LoginRequiredMixin, CreateView):
    form_class = ItemForm
    template_name = "todo_app/item-add.html"

    def dispatch(self, request, *args, **kwargs):
        self.todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        return super(ItemAddView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self):
        context = super(ItemAddView, self).get_context_data()
        context["title"] = self.todo_list.title
        return context

    def get_success_url(self):
        return reverse_lazy("todo:item-view", args=[self.kwargs["list_id"]])

    def get_initial(self):
        initial = super(ItemAddView, self).get_initial()
        initial["todo_list"] = self.todo_list
        return initial

    def form_valid(self, form):
        model_instance = form.save(commit=False)
        model_instance.todo_list = self.todo_list
        model_instance.save()
        return HttpResponseRedirect(self.get_success_url())


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ItemForm
    template_name = "todo_app/item-update.html"

    def get_context_data(self):
        context = super(ItemUpdateView, self).get_context_data()
        context["task"] = ToDoItem.objects.get(id=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse_lazy("todo:item-view", args=[self.kwargs["list_id"]])

    def get_queryset(self):
        return ToDoItem.objects.all()


class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = ToDoList
    template_name = "todo_app/list-delete.html"

    def get_context_data(self, **kwargs):
        context = super(ListDeleteView, self).get_context_data(**kwargs)
        context["todo_list"] = self.object
        return context

    def get_success_url(self):
        return reverse_lazy("todo:index")


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = ToDoItem
    template_name = "todo_app/item-delete.html"

    def get_context_data(self, **kwargs):
        context = super(ItemDeleteView, self).get_context_data(**kwargs)
        context["task"] = self.object
        return context

    def get_success_url(self):
        return reverse_lazy("todo:item-view", args=[self.kwargs["list_id"]])


class NotLoggedAllow(UserPassesTestMixin):
    login_url = reverse_lazy('todo:login')

    def test_func(self):
        return not self.request.user.is_authenticated


class LoginPageView(NotLoggedAllow, LoginView):
    next_page = 'todo:index'
    template_name = 'todo_app/login.html'


class SignUpView(NotLoggedAllow, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("todo:index")
    template_name = "todo_app/signup.html"


class LogoutView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse("todo:index"))


def AboutView(request):
    return render(request, template_name="todo_app/about.html")
