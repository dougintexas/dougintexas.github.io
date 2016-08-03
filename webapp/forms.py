from django.forms import ModelForm
from webapp.models import Survey


class SurveyForm(ModelForm):

    class Meta:
        model = Survey

        fields = [
            'q_imporant_find_cancer',
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