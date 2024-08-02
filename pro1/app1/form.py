from django import  forms
from .models import Voter
from django.core import validators
from datetime import date



class VoterForm(forms.ModelForm):
    class Meta:
        model = Voter
        fields = "__all__"

    def clean_dob(self):
        a = self.cleaned_data.get("dob")
        print(a)
        today = date.today()
        val = (today.year - a.year) - ((today.month, today.day) < (a.month, a.day))
        if val < 18:
            raise validators.ValidationError("Not Eligible for Vote")
        return a