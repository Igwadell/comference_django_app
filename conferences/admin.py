from django.contrib import admin
from conferences.models import Conference, Category, Schedule, Attendee, Reminder, Report

# Register your models here.
admin.site.register(Conference)
admin.site.register(Category)
admin.site.register(Schedule)
admin.site.register(Attendee)
admin.site.register(Reminder)
admin.site.register(Report)
