"""views.py. """
from django.urls import reverse_lazy

from commerce_app.views import ContactView
from portfolio.models import Skill


# pylint: disable=too-many-ancestors
class IndexView(ContactView):
    """
    IndexView
    This view class views the index page of portfolio.
    """
    template_name = "portfolio/index.html"
    success_url = reverse_lazy("portfolio")

    # pylint: disable=no-member
    def get_context_data(self, **kwargs):
        """
        get context data method is overwritten to get a list of skill instances
        in order to display in the index page.
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context['object_list'] = Skill.objects.all()
        return context
