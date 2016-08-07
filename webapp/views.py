from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from webapp.models import Survey, SurveyForm


def index(request):
    if request.method == 'POST':
        request.session['survey_code'] = request.POST['survey_code']
        formset = SurveyForm(request.POST)
        return render(request, 'main.html', {'formset': formset})
    return redirect('start')


def start(request):
    return render(request, 'start.html')


def thanks(request):
    print(request)
    if request.method == 'POST':
        submission = SurveyForm(request.POST)
        submission.save()
        return render(request, 'thanks.html', {'survey_code': request.POST['survey_code']})
    return redirect('start')


def coaching(request, survey_code):
    survey = get_object_or_404(Survey, survey_code=survey_code)

    return render(request, 'dec_coaching.html', {'survey': survey})
