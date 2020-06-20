from django.forms import ModelForm
from .models import *

class Taskform(forms.ModelForm):
    class Meta:
        model = Taskform
        fields = ["title","status"]
