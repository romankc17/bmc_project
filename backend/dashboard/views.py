from django.shortcuts import render

from association.models import Event

def events(request):
    context = {
        'events':Event.objects.order_by('-date'),
    }
    template_name = 'dashboard/events.html'
    
    return render(request, template_name, context)
