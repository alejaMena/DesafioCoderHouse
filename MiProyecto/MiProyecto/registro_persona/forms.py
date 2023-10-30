from django.forms import ModelForm
from .models import familia 

class reg_familia_form(ModelForm):
    class Meta:
        model = familia
        fields = ['Apellido', 'Pareja']
