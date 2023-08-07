from django.forms import ModelForm
from .models import Portador

class PortadorForm(ModelForm):
    class Meta:
        model = Portador
        fields = '__all__'