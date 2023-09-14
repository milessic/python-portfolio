from django.shortcuts import render
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import Event
from .forms import CreateEventForm


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def create(request):
    list(messages.get_messages(request))
    form_filled = False
    if request.method == 'POST':
        form = CreateEventForm(request.POST or None)
        if form.is_valid():
            event_name = form.cleaned_data['event_name']
            event_description = form.cleaned_data['event_description']
            event_start_date = form.cleaned_data['event_start_date']
            event_end_date = form.cleaned_data['event_end_date']
            lead_person = form.cleaned_data['lead_person']
            event_ticketed = form.cleaned_data['event_ticketed']
            event_price = form.cleaned_data['event_price']
            event = Event(event_name=event_name, event_description = event_description, event_start_date = event_start_date, event_end_date = event_end_date, lead_person = lead_person, event_ticketed = event_ticketed, event_price = event_price)
            event.save()
            messages.info(request, mark_safe(f'Event id <a href="/monitor/details/{event.pk}">{event.pk}</a> has been created'))
            form_filled = False
        else:
            messages.add_message(request, messages.ERROR, f'Event couldn\'t be created!')
            form_filled = True

    template = loader.get_template('create.html')
    if not form_filled:
        form = CreateEventForm()
    else:
        form = CreateEventForm(request.POST or None)
    c = {
        'form': form,
    }
    return render(request, 'create.html', c)


def monitor(request):
    list(messages.get_messages(request))
    events = Event.objects.all().values()
    template = loader.get_template('monitor.html')
    context = {
        'events': events
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    event = Event.objects.get(id=id)
    delete_event = False
    list(messages.get_messages(request))
    edit_view = request.GET.get('edit_view')
    delete_view = request.GET.get('delete')
    if delete_view == "True":
        delete_event = True


    if edit_view == "True":
        edit_view = True
    else:
        edit_view = False

    if request.method == 'POST':
        if delete_event == True:
            event.delete()
            template = loader.get_template("event_deleted.html")
            context = {
                'id_name': f'{id} {event.event_name}'
            }
            return HttpResponse(template.render(context))
        form = CreateEventForm(request.POST or None)
        if form.is_valid():
            #event = Event.objects.all().get(event_name=event_name, event_description = event_description, event_start_date = event_start_date, event_end_date = event_end_date, lead_person = lead_person, event_ticketed = event_ticketed, event_price = event_price)
            event.event_name = form.cleaned_data['event_name']
            event.event_description = form.cleaned_data['event_description']
            event.event_start_date = form.cleaned_data['event_start_date']
            event.event_end_date = form.cleaned_data['event_end_date']
            event.lead_person = form.cleaned_data['lead_person']
            event.event_ticketed = form.cleaned_data['event_ticketed']
            event.event_price = form.cleaned_data['event_price']
            event.save()
        else:
            messages.add_message(request, messages.ERROR, f'Event couldn\'t be created!')

    form = CreateEventForm(initial=event.__dict__)
    template = loader.get_template("details.html")
    context = {
        'e': event,
        'edit_view': edit_view,
        'form': form,
        'delete_event': delete_event,
    }
    return HttpResponse(template.render(context, request))


def help(request):
    template = loader.get_template("help.html")
    return HttpResponse(template.render())


def search(request):
    if request.method == "POST":
        formx = request.POST
        query = formx['search']
        query_results = Event.objects.filter(event_name__icontains=query)
        #query_results.append(Event.objects.filter(id__icontains=query))
        events = query_results
    else:
        events = None

    context = {
        'events': events
    }

    template = loader.get_template("search.html")
    return HttpResponse(template.render(context, request))