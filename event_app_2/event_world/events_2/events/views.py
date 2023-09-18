from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.template import loader, RequestContext
from .models import Event
from .forms import CreateEventForm, MonitorFilterForm
from .objects import Page

@login_required(login_url='/accounts/login')
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


@login_required(login_url='/accounts/login')
def create(request):
    user = request.user
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
            user_group = form.cleaned_data['user_group']
            created_by = user.username
            event = Event(event_name=event_name, event_description = event_description, event_start_date = event_start_date, event_end_date = event_end_date, lead_person = lead_person, event_ticketed = event_ticketed, event_price = event_price, user_group=user_group, created_by=created_by)
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


@login_required(login_url='/accounts/login')
def monitor(request):
    active_filters = []
    if request.method == "POST":
        f = request.POST
        events = Event.objects.all()
        if f['from_date']:
            events = events.filter(event_start_date__gte=f['from_date'])
            active_filters.append(f"event start from: {f['from_date']}")
        if f['till_date']:
            events = events.filter(event_start_date__lte=f['till_date'])
            active_filters.append(f"event start till: {f['till_date']}")
        if f['lead']:
            events = events.filter(lead_person__icontains=f['lead'])
            active_filters.append(f"lead person: {f['lead']}")
        if f['created_by']:
            events = events.filter(created_by=f['created_by'])
            active_filters.append(f"created by: {f['created_by']}")
        #events.filter(event_start_date__gte=f['from_date'])
        #events = Event.objects.filter(event_start_date__range=(f['from_date'], f['till_date']), lead_person__icontains=f['lead'])
        #HttpResponse(template.render(context, request))
        f = MonitorFilterForm(initial=f)
    else:
        events = Event.objects.all().values().order_by('-id')
        f = MonitorFilterForm()
    total_events = events.count()
    list(messages.get_messages(request))
    template = loader.get_template('monitor.html')
    current_page = request.GET.get('page')
    if current_page:
        page = Page(page=int(current_page), total_events=total_events)
    else:
        page = Page(page=1, total_events=total_events)

    events = Event.objects.all().values()[0+(50*(page.page-1)):50*page.page]
    context = {
        'events': events,
        'total': total_events,
        'form': f,
        'active_filters': active_filters,
        'page': page,
        'events_on_page': f'{1+(50*(page.page-1))} - {50*page.page}'
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login')
def details(request, id):
    user = request.user
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
            return HttpResponse(template.render(context, request))
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
            messages.add_message(request, messages.ERROR, f'Event couldn\'t be saved!')

    form = CreateEventForm(initial=event.__dict__)
    template = loader.get_template("details.html")
    context = {
        'e': event,
        'edit_view': edit_view,
        'form': form,
        'delete_event': delete_event,
    }
    return HttpResponse(template.render(context, request))


#@login_required(login_url='/accounts/login')
def events_help(request):
    template = loader.get_template("events_help.html")
    context = {}
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login')
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


@login_required(login_url='/accounts/login')
def users(request, username):
    opened_user = get_object_or_404(User, username=username)
    created_events = Event.objects.filter(created_by=f'{opened_user.username}')
    created_events = created_events.order_by('-id')[:5]
    context = {
        'created_e': created_events,
        'u': opened_user,
    }
    print(13)
    template = loader.get_template('users.html')
    return HttpResponse(template.render(context, request))

