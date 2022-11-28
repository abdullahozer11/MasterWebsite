# Create your views here.
from django.urls import reverse_lazy

from commerce_app.views import ContactView
from portfolio.models import Skill


class IndexView(ContactView):
    template_name = "portfolio/index.html"
    success_url = reverse_lazy("portfolio")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Skill.objects.all()
        return context
