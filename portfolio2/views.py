from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from portfolio2.forms import CustomerForm
from portfolio2.models import App


class ContactView(SuccessMessageMixin, CreateView):
    form_class = CustomerForm

    def form_valid(self, form):
        """
        form_valid method is overwritten to send emails

        :param form:
        :return:
        """
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
            messages.add_message(self.request, messages.SUCCESS, "Your message is sent!")
        except:
            messages.add_message(self.request, messages.ERROR, "An error happened :(")
        response = super().form_valid(form)
        return response


# Create your views here.
class Portfolio2IndexView(ContactView):
    """
    IndexView
    This view class views the index page of the new portfolio design.
    """
    template_name = "portfolio2/index.html"
    success_url = reverse_lazy("portfolio2")
    failure_url = reverse_lazy("portfolio2")
    extra_context = {
        "apps": App.objects.all(),
        "apps_length": len(App.objects.all())
    }

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            messages.add_message(self.request, messages.ERROR, "Invalid Email :(")
            return HttpResponseRedirect(self.failure_url)
