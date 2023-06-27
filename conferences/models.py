# import datetime
# from datetime import timedelta

from speakers.models import Speaker

# https://djangoproject.com

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


#  1 cat -------> Many conf
#  1 conf ------> 1 cat:


class Conference(models.Model):
    tittle = models.CharField(max_length=200)
    date = models.DateTimeField()
    # category = models.CharField(max_length=100, choices=CONF_CATEGORIES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    venue = models.CharField(max_length=255 ,blank=True, null=True)
    theme = models.CharField(max_length=255 ,blank=True, null=True)

    def __str__(self):
        return f"{self.tittle} - {self.tittle}"


class Schedule(models.Model):
    conference = models.ForeignKey(Conference, related_name='schedules', on_delete=models.CASCADE)
    time_slot = models.DateTimeField()
    session_duration = models.DurationField()
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)

class Attendee(models.Model):
    conference = models.ForeignKey(Conference, related_name='attendees', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    sessions = models.ManyToManyField(Schedule)

class Reminder(models.Model):
    attendee = models.ForeignKey(Attendee, related_name='reminders', on_delete=models.CASCADE)
    session = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    reminder_time = models.DateTimeField()

class Report(models.Model):
    conference = models.ForeignKey(Conference, related_name='reports', on_delete=models.CASCADE)
    attendance = models.PositiveIntegerField()
    session_popularity = models.PositiveIntegerField()
    speaker_ratings = models.PositiveIntegerField()
