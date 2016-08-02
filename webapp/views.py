from django.shortcuts import render
from django.forms import modelformset_factory
from webapp.models import SurveyForm


def index(request):
    if request.method == 'POST':
        submission = SurveyForm(request.POST)
        submission.save()
    SurveyFormSet = SurveyForm
    formset = SurveyForm
    return render(request, 'base.html', {'formset': formset})
