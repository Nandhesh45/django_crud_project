from django import forms

from new_app.models import Furniture


class FurnitureForm(forms.ModelForm):
    class Meta:
        model=Furniture
        fields=('__all__')