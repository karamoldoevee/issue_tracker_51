from django import forms

from webapp.models import Issue,Status, Type, Project
from django.forms import Select


class IssueForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(widget=Select, required=False, empty_label=None, queryset=None)

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type', 'project', 'assigned_to']
        exclude = ['created_at', 'created_by']

    def clean_summary(self):
        title = self.cleaned_data['summary']

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
        exclude = ['created_at', 'updated_at']

class SimpleSearchForm(forms.Form):

    search = forms.CharField(max_length=100, required=False, label="Найти")