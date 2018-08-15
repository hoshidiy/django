from django.contrib import admin
from .models import Schedule, Person, HayagaeriPlan, HayagaeriResult

admin.site.register(Schedule)
admin.site.register(Person)
admin.site.register(HayagaeriPlan)
admin.site.register(HayagaeriResult)