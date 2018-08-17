from django.urls import path
from . import views

urlpatterns = [
    path(
        'month_with_schedule/',
        views.MonthCalendarMixin.as_view(), name='month_with_schedule'
    ),
    path(
        'month_with_schedule/<int:year>/<int:month>/',
        views.MonthCalendarMixin.as_view(), name='month_with_schedule'
    ),
    path(
        'create_person/', views.create_person, name='create_person'
    ),
    path(
        'create_schedule/', views.create_schedule, name='create_schedule'
    ),
    path(
        'delete/<int:num>', views.delete, name='delete'
    ),
    path(
        'update/<int:num>', views.update, name='update'
    ),
    path(
        'ryouhou/<int:num>', views.ryouhou, name='ryouhou'
    ),
    path(
        'img/', views.img, name='img'
    ),
]
