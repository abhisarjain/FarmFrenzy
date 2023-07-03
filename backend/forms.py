from django import forms
from .models import * 

class CropForm(forms.ModelForm):
    
    class Meta:
        model = Crop
        exclude = ('seller',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'variety': forms.TextInput(attrs={'class': 'input'}),
            'price_per_kg': forms.TextInput(attrs={'class': 'input'}),
            'shelf_life': forms.TextInput(attrs={'class': 'input'}),
            'type': forms.TextInput(attrs={'class': 'input'}),
            'quantity': forms.TextInput(attrs={'class': 'input'}),
            'description': forms.Textarea(attrs={'class': 'input','style': 'min-height: 400px;'})
        }