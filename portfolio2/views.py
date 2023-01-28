from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail, BadHeaderError
from django.urls import reverse_lazy
from django.views.generic import CreateView
from portfolio2.forms import CustomerForm


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
            messages.add_message(self.request, messages.SUCCESS, "Your customer contact form is saved successfully!")
        except BadHeaderError:
            messages.add_message(self.request, messages.ERROR, "Bad Header Error")
        response = super().form_valid(form)
        return response


# Create your views here.
class IndexView2(ContactView):
    """
    IndexView
    This view class views the index page of the new portfolio design.
    """
    template_name = "portfolio2/index.html"
    success_url = reverse_lazy("portfolio2")
