from django import forms
from .models import MemberMotivator

class MemberMotivatorForm(forms.ModelForm):
    class Meta:
        model = MemberMotivator
        fields = ['moving_motivator', 'order']