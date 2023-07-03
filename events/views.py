from django.shortcuts import render
from django.db.models import Count, Avg, F, ExpressionWrapper, DurationField
from django.utils import timezone
from datetime import timedelta
from . models import Event, Speaker, Participant, Payment, Schedule
# ...

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_details(request, title):
    event = Event.objects.get(title=title)
    return render(request, 'events/event_detail.html', {'event': event})

def speaker_list(request):
    speakers = Speaker.objects.all()
    return render(request, 'events/speaker_list.html', {'speakers': speakers})

def speaker_detail(request, name):
    speaker = Speaker.objects.get(name=name)
    return render(request, 'events/speaker_detail.html', {'speaker': speaker})

def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'events/participant_list.html', {'participants': participants})

def participant_detail(request, email):
    participant = Participant.objects.get(email=email)
    return render(request, 'events/participant_detail.html', {'participant': participant})

def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'events/schedule_list.html', {'schedules': schedules})

def event_schedules(request, event_id):
    event = Event.objects.get(id=event_id)
    schedules = event.schedule_set.all()
    return render(request, 'events/event_schedules.html', {'event': event, 'schedules': schedules})


def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'events/payment_list.html', {'payments': payments})

def participant_payments(request, email):
    participant = Participant.objects.get(email=email)
    payments = participant.payments.all()
    return render(request, 'events/participant_payments.html', {'participant': participant, 'payments': payments})

def upcoming_events(request):
    current_date = timezone.now().date()
    upcoming_events = Event.objects.filter(start_date__gte=current_date)
    return render(request, 'events/upcoming_events.html', {'upcoming_events': upcoming_events})

def free_events(request):
    free_events = Event.objects.filter(is_free=True)
    return render(request, 'events/free_events.html', {'free_events': free_events})

def paid_events(request):
    paid_events = Event.objects.filter(is_free=False)
    return render(request, 'events/paid_events.html', {'paid_events': paid_events})

def event_participant_count(request):
    event_participant_counts = Event.objects.annotate(participant_count=Count('participants'))
    return render(request, 'events/event_participant_count.html', {'event_participant_counts': event_participant_counts})

def participant_event_count(request):
    participant_event_counts = Participant.objects.annotate(event_count=Count('events_attended'))
    return render(request, 'events/participant_event_count.html', {'participant_event_counts': participant_event_counts})

def event_schedule_count(request):
    event_schedule_counts = Event.objects.annotate(schedule_count=Count('schedules'))
    return render(request, 'events/event_schedule_count.html', {'event_schedule_counts': event_schedule_counts})

def event_total_payment(request, event_id):
    event = Event.objects.get(id=event_id)
    total_payment = event.payments.aggregate(total_payment=Sum('amount_paid'))
    return render(request, 'events/event_total_payment.html', {'event': event, 'total_payment': total_payment})


def average_price_paid_events(request):
    average_price = Event.objects.exclude(price=None).filter(is_free=False).aggregate(average_price=Avg('price'))
    return render(request, 'events/average_price_paid_events.html', {'average_price': average_price})


def event_participants(request, event_id):
    event = Event.objects.get(id=event_id)
    participants = event.participant_set.all()
    return render(request, 'events/event_participants.html', {'event': event, 'participants': participants})



def events_without_speakers(request):
    events = Event.objects.filter(speakers__isnull=True)
    return render(request, 'events/events_without_speakers.html', {'events': events})


def event_speakers(request, event_id):
    event = Event.objects.get(id=event_id)
    speakers = event.speakers.all()
    return render(request, 'events/event_speakers.html', {'event': event, 'speakers': speakers})

def participants_attended_all_events(request):
    participants = Participant.objects.annotate(event_count=Count('events_attended'))
    participants_attended_all = participants.filter(event_count=Event.objects.count())
    return render(request, 'events/participants_attended_all.html', {'participants_attended_all': participants_attended_all})


def events_in_date_range(request, start_date, end_date):
    events = Event.objects.filter(start_date__gte=start_date, end_date__lte=end_date)
    return render(request, 'events/events_in_date_range.html', {'events': events})

# 4 View ntarinakora zari Remaining views ...

def events_longest_gap(request):
    events = Event.objects.annotate(gap=ExpressionWrapper(F('end_date') - F('start_date'), output_field=DurationField())).order_by('-gap')[:10]
    return render(request, 'events/events_longest_gap.html', {'events': events})

def participants_by_location(request, location):
    participants = Participant.objects.filter(events_attended__location=location)
    return render(request, 'events/participants_by_location.html', {'participants': participants, 'location': location})

def speakers_highest_average_rating(request):
    speakers = Speaker.objects.annotate(average_rating=Avg('ratings__rating')).order_by('-average_rating')[:10]
    return render(request, 'events/speakers_highest_average_rating.html', {'speakers': speakers})

def participants_all_payments(request):
    participants = Participant.objects.annotate(payment_count=Count('payments')).filter(payment_count=Event.objects.count())
    return render(request, 'events/participants_all_payments.html', {'participants': participants})

# am going on out with 12 remaing

# 12 remaining

def highest_paid_events(request):
    events = Event.objects.annotate(total_payment=Sum('payments__amount_paid')).order_by('-total_payment')[:10]
    return render(request, 'events/highest_paid_events.html', {'events': events})

def participants_highest_payment(request):
    participants = Participant.objects.annotate(total_payment=Sum('payments__amount_paid')).order_by('-total_payment')[:10]
    return render(request, 'events/participants_highest_payment.html', {'participants': participants})

def speakers_most_scheduled_events(request):
    speakers = Speaker.objects.annotate(scheduled_event_count=Count('events_scheduled')).order_by('-scheduled_event_count')[:10]
    return render(request, 'events/speakers_most_scheduled_events.html', {'speakers': speakers})

def events_longest_duration(request):
    events = Event.objects.annotate(duration=ExpressionWrapper(F('end_date') - F('start_date'), output_field=DurationField())).order_by('-duration')[:10]
    return render(request, 'events/events_longest_duration.html', {'events': events})

def participants_most_events_in_month(request, month):
    participants = Participant.objects.filter(events_attended__start_date__month=month).annotate(event_count=Count('events_attended')).order_by('-event_count')
    return render(request, 'events/participants_most_events_in_month.html', {'participants': participants, 'month': month})

def events_with_overlapping_schedules(request):
    events = Event.objects.filter(schedules__overlap=F('schedules')).distinct()
    return render(request, 'events/events_with_overlapping_schedules.html', {'events': events})

def participants_recent_payment(request):
    seven_days_ago = timezone.now() - timedelta(days=7)
    participants = Participant.objects.filter(payments__date_paid__gte=seven_days_ago).distinct()
    return render(request, 'events/participants_recent_payment.html', {'participants': participants})

def participants_attended_consecutive_events(request):
    participants = Participant.objects.annotate(consecutive_events=Count('events_attended__id')).filter(consecutive_events__gt=1)
    return render(request, 'events/participants_attended_consecutive_events.html', {'participants': participants})

def speakers_without_events(request):
    speakers = Speaker.objects.filter(events_scheduled__isnull=True)
    return render(request, 'events/speakers_without_events.html', {'speakers': speakers})

def events_highest_total_payment(request):
    events = Event.objects.annotate(total_payment=Sum('payments__amount_paid')).order_by('-total_payment')[:10]
    return render(request, 'events/events_highest_total_payment.html', {'events': events})

def participants_multiple_locations(request):
    participants = Participant.objects.annotate(location_count=Count('events_attended__location')).filter(location_count__gt=1)
    return render(request, 'events/participants_multiple_locations.html', {'participants': participants})

def speakers_different_topics(request):
    speakers = Speaker.objects.annotate(topic_count=Count('topics_presented', distinct=True)).filter(topic_count__gt=1)
    return render(request, 'events/speakers_different_topics.html', {'speakers': speakers})