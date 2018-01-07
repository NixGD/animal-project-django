from django import forms
from .models import Part, Shape, Animal

class PartForm(forms.ModelForm):

    class Meta:
        model = Part
        fields = ['name']

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
