from datetime import datetime, timedelta

import pytz
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

    def gmt_to_timedelta(self, gmt_str):
        sign, hours_str = gmt_str[:4], gmt_str[4:]
        hours = int(hours_str)
        if sign == 'GMT+':
            return timedelta(hours=hours)
        elif sign == 'GMT-':
            return timedelta(hours=-hours)
        else:
            return timedelta(0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            target_date_obj = TargetDate.objects.get(name=self.name)
            user_timezone_str = target_date_obj.timezone  # Assuming the timezone field is in the TargetDate model
        except TargetDate.DoesNotExist:
            target_date_obj = TargetDate(date=datetime(2023, 9, 7, tzinfo=pytz.UTC))
            user_timezone_str = 'GMT'
        if target_date_obj:
            # Get the timezone-aware datetime object
            user_timedelta = self.gmt_to_timedelta(user_timezone_str)
            target_date = target_date_obj.date + user_timedelta
            context['year'] = target_date.year
            context['month'] = target_date.month - 1
            context['day'] = target_date.day
            context['hour'] = target_date.hour
            context['minute'] = target_date.minute
        return context
