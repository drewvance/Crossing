from cross.models import Event
from datetime import datetime

def event(request):
    events = Event.objects.filter(datetime__gt=datetime.utcnow())[0:5]
    return {'events':events}
    