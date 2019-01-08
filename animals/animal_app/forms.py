from django import forms
from django.contrib.auth.models import User
from .models import Part, Shape, Animal, Collection

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

class CollectionForm(forms.ModelForm):

    class Meta:
        model = Collection
        fields = ['name']

class CollectionShareForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        users = User.objects.filter(email=self.cleaned_data["email"])
        if not users.exists():
            raise forms.ValidationError("No such user")

        return users.first()
