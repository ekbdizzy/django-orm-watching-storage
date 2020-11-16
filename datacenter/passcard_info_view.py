from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from .utils import format_duration
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)

    this_passcard_visits = []
    for visit in Visit.objects.filter(passcard__passcode=passcode):
        this_passcard_visits.append(
            {
                "entered_at": localtime(visit.entered_at),
                "duration": format_duration(visit.get_duration()),
                "is_strange": visit.is_visit_long()
            }
        )

    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
