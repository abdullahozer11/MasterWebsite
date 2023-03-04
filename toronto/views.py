from django.views.generic import TemplateView
from toronto.models import TorontoTargetDate


class TorontoView(TemplateView):
    model = TorontoTargetDate
    template_name = 'countdown/toronto.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        target_date = TorontoTargetDate.objects.last()
        if target_date:
            context['year'] = target_date.date.year
            context['month'] = target_date.date.month
            context['day'] = target_date.date.day
            context['hour'] = target_date.date.hour
            context['minute'] = target_date.date.minute
        return context
