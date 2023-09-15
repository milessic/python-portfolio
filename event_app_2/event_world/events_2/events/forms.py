from django import forms


class CreateEventForm(forms.Form):
    event_name = forms.CharField(label='Event Name', max_length=100)
    event_description = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    event_start_date = forms.DateField(label="Event Start")
    event_end_date = forms.DateField(label="Event End", required=False)
    lead_person = forms.CharField(label='Lead Person', max_length=255, required=False)
    event_ticketed = forms.BooleanField(required=False)
    event_price = forms.IntegerField(label='Event Price', required=False)


class MonitorFilterForm(forms.Form):
    from_date = forms.DateField(label="from", required=False)
    till_date = forms.DateField(label="till", required=False)
    lead = forms.CharField(label='Lead Person', max_length=255, required=False)