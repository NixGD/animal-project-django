from django import forms
from .models import Part, Shape, Animal

class PartForm(forms.ModelForm):

    class Meta:
        model = Part
        fields = ['name', 'quantity']

class OverwriteForm(forms.ModelForm):

    class Meta:
        model = Part
        fields = ['overwritten_sa', 'overwritten_vol']

class NewPartForm(forms.ModelForm):

    class Meta:
        model = Part
        fields = ['name', 'shape']

class ShapeSelectForm(forms.Form):
    shape = forms.ModelMultipleChoiceField(
        queryset=Shape.shapes.all(),
        label = "Create new")

class AnimalForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = ['student', 'animal']

class AnimalNotesForm(forms.ModelForm):

    class Meta:
        model = Animal
        fields = ['notes']

class StateSelectForm(forms.ModelForm):

    class Meta:
        model = Part
        fields = ['state']
