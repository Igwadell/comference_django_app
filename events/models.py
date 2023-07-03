# # import datetime
# # from datetime import timedelta

# from speakers.models import Speaker

# # https://djangoproject.com

# from django.db import models


# class Category(models.Model):
#     name = models.CharField(max_length=100)

#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'

#     def __str__(self):
#         return self.name


# #  1 cat -------> Many conf
# #  1 conf ------> 1 cat:


# class Event(models.Model):
#     # Category=models.ForeignKey(Category, related_name='speakers', on_delete=models.CASCADE)
#     name =models.CharField(max_length= 255,blank=True, null=True)
#     title = models.CharField(max_length=200)
#     date = models.DateTimeField()
#     # category = models.CharField(max_length=100, choices=CONF_CATEGORIES)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     venue = models.CharField(max_length=255 ,blank=True, null=True)
#     theme = models.CharField(max_length=255 ,blank=True, null=True)
    
# def __str__(self):
#     return f"{self.tittle} - {self.date}"



# class Schedule(models.Model):
#     event = models.ForeignKey(Event, related_name='schedules', on_delete=models.CASCADE)
#     time_slot = models.DateTimeField()
#     session_duration = models.DurationField()
#     speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)

# class Participant(models.Model):
#     event = models.ForeignKey(Event, related_name='Participants', on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     email = models.EmailField()
#     sessions = models.ManyToManyField(Schedule)

# class Reminder(models.Model):
#     Participant = models.ForeignKey(Participant, related_name='reminders', on_delete=models.CASCADE)
#     session = models.ForeignKey(Schedule, on_delete=models.CASCADE)
#     reminder_time = models.DateTimeField()

# class Report(models.Model):
#     event = models.ForeignKey(Event, related_name='reports', on_delete=models.CASCADE)
#     attendance = models.PositiveIntegerField()
#     session_popularity = models.PositiveIntegerField()
#     speaker_ratings = models.PositiveIntegerField()

# class Payment(models.Model):
#     PAYMENT_STATUS_CHOICES = (
#         ('PAID', 'Paid'),
#         ('PENDING', 'Pending'),
#         ('FAILED', 'Failed'),
#     )

#     participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
#     event = models.ForeignKey(Event, on_delete=models.CASCADE)
#     amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_method = models.CharField(max_length=100)
#     payment_date = models.DateField()
#     transaction_id = models.CharField(max_length=100)
#     payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)

#     def __str__(self):
#         return f"{self.participant.name} - {self.event.title} - {self.amount_paid}"




from django.db import models
from speakers.models import Speaker


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    venue = models.CharField(max_length=255, blank=True, null=True)
    theme = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.date}"


class Schedule(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    time_slot = models.DateTimeField()
    session_duration = models.DurationField()
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)


class Participant(models.Model):
    events = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    schedules = models.ManyToManyField(Schedule)


class Reminder(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='reminders')
    session = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    reminder_time = models.DateTimeField()


class Report(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='reports')
    attendance = models.PositiveIntegerField()
    session_popularity = models.PositiveIntegerField()
    speaker_ratings = models.PositiveIntegerField()


class Payment(models.Model):
    PAYMENT_STATUS_CHOICES = (
        ('PAID', 'Paid'),
        ('PENDING', 'Pending'),
        ('FAILED', 'Failed'),
    )

    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=100)
    payment_date = models.DateField()
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES)

    def __str__(self):
        return f"{self.participant.name} - {self.event.title} - {self.amount_paid}"
