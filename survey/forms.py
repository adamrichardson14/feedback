from django.forms import ModelForm
from .models import Survey 

class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        exclude = ['company', 'site', 'date_submitted', 'arrival_date', 'servicetarget', 'cleanlinesstarget', 'tmexceedtarget']
        labels = {
            'email': ('Please enter your email here'),
            'nps': ('How likely are you to recommend our hotel to your friends and family?'),
            'service': ('How would you rate the quality of service received from team members?'),
            'cleanliness': ('How would you rate the cleanliness of the hotel'),
            'checkin': ('How was your check in experience?'),
            'dinnerqual': ('How would you rate the quality of food served in restaurant at dinner?'),
            'dinnerservice': ('How would you rate the service received from restaurant team at dinner?'),
            'breakfastqual': ('How would you rate the quality of breakfast food?'),
            'breakfastservice': ('How would you rate the service received in the restaurant during breakfast'),
            'tmexceed': ('Did any of our team members exceed your expectations?'),
            'tmexceeddetails': ('Please provide details of team member/s that exceeded your expectations'),
            'anyfeedback': ('Do you have any other feedback or comments?'),
            'sitecode': ('Site code... This will be auto-populated on production')
        }

    def __init__(self, *args, **kwargs):
        super(SurveyForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['nps'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['service'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['cleanliness'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['checkin'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['dinnerqual'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['dinnerservice'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['breakfastqual'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['breakfastservice'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['tmexceed'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['tmexceeddetails'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['anyfeedback'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['sitecode'].widget.attrs.update({
            'class': 'form-control',
        })

