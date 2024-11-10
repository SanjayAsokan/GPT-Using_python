from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from django import forms

class ChatForm(forms.Form):
    question = forms.CharField(label='', widget=forms.TextInput(attrs={'id': 'voice-input'}))  # Customize label (optional)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'question',
            HTML('<button type="button" id="voice-button" class="btn btn-primary">Speak</button>  '),
            Submit('Ask', css_class='btn-primary', value='Ask ')
        )
