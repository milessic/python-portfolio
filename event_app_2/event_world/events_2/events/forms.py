from django import forms


class CreateEventForm(forms.Form):
    event_name = forms.CharField(label='Event Name', max_length=100)
    event_description = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    event_start_date = forms.DateField(label="Event Start")
    event_end_date = forms.DateField(label="Event End")
    lead_person = forms.CharField(label='Lead Person', max_length=255)
    event_ticketed = forms.NullBooleanField()
    event_price = forms.IntegerField(label='Event Price')

