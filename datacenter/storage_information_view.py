from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from django.utils.timezone import localtime
from datetime import timedelta, datetime


def get_duration(visit: Visit) -> int:
    """Get duration of visit in seconds from vizit.entered_at to timezone.now()."""
    entered = visit.entered_at
    delta = timezone.now() - entered
    return delta.total_seconds()


def format_duration(duration: int) -> str:
    hours, minutes_and_seconds = divmod(duration, 3600)
    minutes, seconds = divmod(minutes_and_seconds, 60)
    return f'{int(hours)}ч {int(minutes)}мин'


def storage_information_view(request):
    non_closed_visits = []
    for visit in Visit.objects.filter(leaved_at=None):
        non_closed_visits.append(
            {
                "who_entered": visit.passcard.owner_name,
                "entered_at": visit.entered_at,
                "duration": format_duration(get_duration(visit))
            }
        )

    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
