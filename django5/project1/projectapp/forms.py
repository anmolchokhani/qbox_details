from django import forms
from .models import ClientData

class ClientDataForm(forms.ModelForm):
    class Meta:
        model= ClientData
        fields=['name' ,'boxno', 'qtrack_email', 'qtrack_password', 'sudo_password']
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'boxno': forms.NumberInput(attrs={'class':'form-control'}),
            'qtrack_email': forms.EmailInput(attrs={'class':'form-control'}),
            'qtrack_password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
            'sudo_password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        

        }
