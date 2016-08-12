from __future__ import unicode_literals
from django.db import models
from django import forms
from django.forms import ModelForm, HiddenInput

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
    survey_code = models.CharField(
        blank=True,
        null=True,
        max_length=30,
    )
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
    q_concerned_rad = models.CharField(
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
    q_concerned_surg = models.CharField(
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
    q_talk_having_surg = models.CharField(
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

    q_talk_more_screening = models.CharField(
        blank=True,
        null=True,
        max_length=50,
        choices=CHOICES_TALK,
        verbose_name='what happens if the lung cancer screening shows something that may need more testing.'
    )
    
    d_harm_falsealarm_ment = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_harm_falsealarm_disc = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_harm_rad_ment = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_harm_rad_disc = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_harm_overdx_ment = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_harm_overdx_disc = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_harm_surg_ment = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_harm_surg_disc = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_focused_findcancer = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_focused_falsealarm = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_focused_rad = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_focused_overdx = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_focused_surg = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_talkabout_notscreening = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_talkabout_knowresults = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )

    d_talkabout_moretesting = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )    

    d_sure_clearaboutbandh = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )    

    d_sure_knowaboutbandh = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )    

    d_sure_sureaboutbestchoice = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )    

    d_sure_havesupport = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )    

    d_sure_bescreenedtoday = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )    

    d_keymsg_quitsmoking = models.CharField(
        blank=True,
        null=True,
        max_length=50,
    )        

class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = [
            'survey_code',
            'q_concerned_find_cancer',
            'q_concerned_false_alarm',
            'q_concerned_rad',
            'q_concerned_unnecessary_treatment',
            'q_concerned_surg',
            'q_talk_not_screened',
            'q_talk_how_soon',
            'q_talk_more_screening',
            'q_talk_having_surg',
            'q_confirm_quit_smoking',
            'q_confirm_annual_screening',
            'd_harm_falsealarm_ment',
            'd_harm_falsealarm_disc',
            'd_harm_rad_ment',
            'd_harm_rad_disc',
            'd_harm_overdx_ment',
            'd_harm_overdx_disc',
            'd_harm_surg_ment',
            'd_harm_surg_disc',
            'd_focused_findcancer',
            'd_focused_falsealarm',
            'd_focused_rad',
            'd_focused_overdx',
            'd_focused_surg',
            'd_talkabout_notscreening',
            'd_talkabout_knowresults',
            'd_talkabout_moretesting',
            'd_sure_clearaboutbandh',
            'd_sure_knowaboutbandh',
            'd_sure_sureaboutbestchoice',
            'd_sure_havesupport',
            'd_sure_bescreenedtoday',
            'd_keymsg_quitsmoking',
        ]
        widgets = {
            'survey_code': HiddenInput(),
        }