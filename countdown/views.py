from datetime import datetime

from django.views.generic import TemplateView
from countdown.models import TargetDate


class CountdownView(TemplateView):
    model = TargetDate
    name = None
    template_name = None

    def __init__(self, template_name, name, **kwargs):
        super().__init__(**kwargs)
        self.template_name = template_name
        self.name = name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            target_date = TargetDate.objects.get(name=self.name)
        except TargetDate.DoesNotExist:
            target_date = TargetDate(date=datetime(2023, 9, 7))
        except Exception:
            target_date = None
        if target_date:
            context['year'] = target_date.date.year
            context['month'] = target_date.date.month
            context['day'] = target_date.date.day
            context['hour'] = target_date.date.hour
            context['minute'] = target_date.date.minute
        return context
