from __future__ import unicode_literals
from django.db import models
from django import forms
from django.forms import ModelForm, RadioSelect

CHOICES_CONCERNED = (
    ('Very Concerned', 'Very Concerned'),
    ('Somewhat Concerned', 'Somewhat Concerned'),
    ('Not Concerned', 'Not Concerned'),
)

CHOICES_TALK = (
    ('Yes', 'Yes, I want to talk about this'),
    ('No', 'No, I don''t want to talk about this'),
)

CHOICES_CONFIRM = (
    ('quit smoking', 'The best thing to lower your risk of dying from lung cancer is to quit smoking or continue to not smoke.'),
    ('annual screening', 'I should return once a year for annual screening.'),
)


class Survey(models.Model):
    date_submitted = models.DateTimeField(auto_now_add=True)
    q_concerned_find_cancer = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=CHOICES_CONCERNED,
        verbose_name='How important is it to you to find lung cancer early when it may be treated more easily treated?'
    )
    q_concerned_false_alarm = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=CHOICES_CONCERNED,
        verbose_name='having a false alarm?'
    )
    q_concerned_radiation = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=CHOICES_CONCERNED,
        verbose_name='being exposed to radiation from lung cancer?'
    )
    q_concerned_unnecessary_treatment = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=CHOICES_CONCERNED,
        verbose_name='being treated for lung cancer that never would have harmed you?'
    )
    q_concerned_surgery = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=CHOICES_CONCERNED,
        verbose_name='having surgery if lung cancer is found?'
    )
    q_talk_not_screened = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=CHOICES_TALK,
        verbose_name='what happens if I decide NOT to be screened for lung cancer.'
    )
    q_talk_how_soon = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=CHOICES_TALK,
        verbose_name='how soon I will know the results of screening.'
    )
    q_talk_more_screening = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=CHOICES_TALK,
        verbose_name='what happens if the lung cancer screening shows something that may need more testing.'
    )
    q_talk_having_surgery = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=CHOICES_TALK,
        verbose_name='having surgery if lung cancer is found?'
    )
    q_confirm_quit_smoking = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )
    q_confirm_annual_screening = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )


class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = [
            'q_concerned_find_cancer',
            'q_concerned_false_alarm',
            'q_concerned_radiation',
            'q_concerned_unnecessary_treatment',
            'q_concerned_surgery',
            'q_talk_not_screened',
            'q_talk_how_soon',
            'q_talk_more_screening',
            'q_talk_having_surgery',
            'q_confirm_quit_smoking',
            'q_confirm_annual_screening',
        ]
        # widgets = {'q_imporant_find_cancer': RadioSelect, 'q_concerned_false_alarm': RadioSelect}

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    test = forms.RadioSelect()