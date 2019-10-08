from django import forms
from django.forms import widgets

from webapp.models import Issue, Status, Type, Project


class IssueForm(forms.Form):
    summary = forms.CharField(max_length=200, label='Summary', required=True)
    description = forms.CharField(max_length=3000, label='Description', required=True,
                           widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False, label='Status',
                                      empty_label=None)
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=False, label='Type',
                                    empty_label=None)
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False, label='Project',
                                  empty_label=None)


class StatusForm(forms.Form):
    name = forms.CharField(max_length=20, label='Статус', required=True)

class TypeForm(forms.Form):
    name = forms.CharField(max_length=20, label='Тип', required=True)

class ProjectForm(forms.Form):
    name = forms.CharField(max_length=20, label='Проект', required=True)
