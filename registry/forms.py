from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    # letters = forms.MultipleChoiceField(
    #     choices=CHOICES, widget=forms.CheckboxSelectMultiple(), label='Test', required=True)

    # inclusion = forms.MultipleChoiceField(
    #     label='hi', widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Patient
        fields = ['hospital_number', 'name',
                  'phone_number', 'inclusion', 'exclusion', ]
