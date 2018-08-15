import calendar
from collections import deque
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Schedule, Person
from .forms import PersonForm, ScheduleForm
from django.views import generic


class BaseCalendarMixin:
    """カレンダー関連Mixinの、基底クラス"""
    first_weekday = 0  # 0は月曜から、1は火曜から。6なら日曜日からになります。お望みなら、継承したビューで指定してください。
    week_names = ['月', '火', '水', '木', '金', '土', '日']  # これは、月曜日から書くことを想定します。['Mon', 'Tue'...

    def setup(self):
        """カレンダーのセットアップ処理

        calendar.Calendarクラスの機能を利用するため、インスタンス化します。
        Calendarクラスのmonthdatescalendarメソッドを利用していますが、デフォルトが月曜日からで、
        火曜日から表示したい(first_weekday=1)、といったケースに対応するためのセットアップ処理です。

        """
        self._calendar = calendar.Calendar(self.first_weekday)

    def get_week_names(self):
        """first_weekday(最初に表示される曜日)にあわせて、week_namesをシフトする"""
        week_names = deque(self.week_names)
        week_names.rotate(-self.first_weekday)
        week_names = week_names * 5
        return week_names


class MonthCalendarMixin(BaseCalendarMixin,generic.TemplateView):
    template_name = 'app_month_hayagaeri/month_with_schedule.html'
    """月間カレンダーの機能を提供するMixin"""

    @staticmethod
    def get_previous_month(date):
        """前月を返す"""
        if date.month == 1:
            return date.replace(year=date.year-1, month=12, day=1)
 
        else:
            return date.replace(month=date.month-1, day=1)
 
    @staticmethod
    def get_next_month(date):
        """次月を返す"""
        if date.month == 12:
            return date.replace(year=date.year+1, month=1, day=1)
 
        else:
            return date.replace(month=date.month+1, day=1)

    def get_month_days(self, date):
        """その月の全ての日を返す"""
        return self._calendar.itermonthdates(date.year, date.month)

    def get_current_month(self):
        """現在の月を返す"""
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        if month and year:
            month = datetime.date(year=int(year), month=int(month), day=1)
        else:
            month = datetime.date.today().replace(day=1)
        return month

    model = Schedule
    date_field = 'date'
    order_field = 'start_time'

    def get_month_schedules(self, days):
        """(日付, その日のスケジュール)なリストを返す"""
        schedules = []
        cm = self.get_current_month()
        d = self.get_month_days(cm)
        for day in d:
            lookup = {self.date_field: day}
            queryset = self.model.objects.filter(**lookup)
            if self.order_field:
                queryset = queryset.order_by(self.order_field)
            schedules.append(queryset)
        return schedules
        
    def get_person_list(self):
        p_models = Person.objects.all()
        return p_models

    def get_month_calendar(self):
        """月間カレンダー情報の入った辞書を返す"""
        self.setup()
        current_month = self.get_current_month()
        days_define = self.get_month_days(current_month)
        sche = self.get_month_schedules(days_define)
        p_models_ins = self.get_person_list()
        calendar_data = {
            'now': datetime.date.today(),
            'days': days_define,
            'current': current_month,
            'week_names': self.get_week_names(),
            'schedule_list': sche,
            'p': p_models_ins,
            'previous': self.get_previous_month(current_month),
            'next': self.get_next_month(current_month),
        }
        return calendar_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['month'] = self.get_month_calendar()
        return context

def create_person(request):
    if (request.method == 'POST'):
        obj = Person()
        create_person = PersonForm(request.POST, instance=obj)
        create_person.save()
        return redirect(to='/month_with_schedule')
    params = {
        'title': '人追加',
        'form': PersonForm(),        
    }
    return render(request, 'app_month_hayagaeri/create_person.html', params)
  
def create_schedule(request):
    if (request.method == 'POST'):
        obj = Schedule()
        schedule = ScheduleForm(request.POST, instance=obj)
        schedule.save()
        return redirect(to='/month_with_schedule')
    params = {
        'title': 'スケジュール追加',
        'form': ScheduleForm(),        
    }
    return render(request, 'app_month_hayagaeri/create_schedule.html', params)

def delete(request, num):
    schedule = Schedule.objects.get(id=num)
    if (request.method == 'POST'):
        schedule.delete()
        return redirect(to='/month_with_schedule')
    params = {
        'title': 'スケジュール削除',
        'id':num,
        'obj': schedule,
    }
    return render(request, 'app_month_hayagaeri/delete.html', params)

def update(request, num):
    obj = Schedule.objects.get(id=num)
    if (request.method == 'POST'):
        schedule = ScheduleForm(request.POST, instance=obj)
        schedule.save()
        return redirect(to='/month_with_schedule')
    params = {
        'title': 'スケジュール更新',
        'id':num,
        'form': ScheduleForm(instance=obj),
    }
    return render(request, 'app_month_hayagaeri/update.html', params)

def ryouhou(request, num):
    ob = Schedule.objects.get(id=num)
    if (request.method == 'POST'):
        if 'r_update' in request.POST:
            schedule = ScheduleForm(request.POST, instance=ob)
            schedule.save()
            return redirect(to='/month_with_schedule')
        elif 'r_delete' in request.POST:
            ob.delete()
            return redirect(to='/month_with_schedule')
    params = {
        'title': 'スケジュール更新or削除',
        'title_update': 'スケジュール更新',
        'title_delete': 'スケジュール削除',
        'id':num,
        'form': ScheduleForm(instance=ob),
        'obj': ob,
    }
    return render(request, 'app_month_hayagaeri/ryouhou.html', params)

