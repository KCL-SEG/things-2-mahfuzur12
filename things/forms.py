"""Forms of the project."""

# Create your forms here.
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    """Form of the Thing model."""
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea(),
            'quantity': forms.NumberInput(),
            }