from .models import Form
from django import forms


class InfoForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = "__all__"
