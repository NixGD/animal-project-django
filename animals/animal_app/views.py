from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.forms import inlineformset_factory
from django.template import Library
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied
from guardian.shortcuts import assign_perm

import logging

from .forms import *
from .models import Animal, Part, Measurement, Shape, Collection

logger = logging.getLogger("debugging")

register = Library()

def login_view(request):
    return render(request, 'animal_app/login.html', {})

def logout_view(request):
    logout(request)
    return redirect(login_view)

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

@login_required
def animal(request, animal_id):
    a = get_object_or_404(Animal, pk=animal_id)
    # Check that the owner is actually correct.
    # TODO: change below check to ensure view premission, and add edit perm checks for processing POST data.
    if not request.user.has_perm('edit_animals', a.collection):
        raise PermissionDenied


    MeasurementsFormSet = inlineformset_factory(Part, Measurement, \
        fields=('value',), can_delete=False, extra=0)

    if request.method == "POST":
        if 'update_notes' in request.POST:
            notesform = AnimalNotesForm(request.POST, instance=a)
            if notesform.is_valid():
                notesform.save()

        if 'state_form' in request.POST:
            p = get_object_or_404(Part, pk=request.POST["part_pk"])
            stateform = StateSelectForm(request.POST, instance=p)
            if stateform.is_valid():
                stateform.save()

        if 'initially_correct_toggle' in request.POST:
            p = get_object_or_404(Part, pk=request.POST["part_pk"])
            p.initiallycorrect = not p.initiallycorrect
            p.save()

        if 'edit_part' in request.POST:
            p = get_object_or_404(Part, pk=request.POST["part_pk"])
            formset = MeasurementsFormSet(request.POST, request.FILES, instance=p)
            partform = PartForm(request.POST, instance=p)
            if formset.is_valid() and partform.is_valid():
                formset.save()
                partform.save()

        if 'overwrite_part' in request.POST:
            p = get_object_or_404(Part, pk=request.POST["part_pk"])
            overwriteform = OverwriteForm(request.POST, instance=p)
            if overwriteform.is_valid():
                overwriteform.save()

        else:
            newPartForm = NewPartForm(request.POST)
            if newPartForm.is_valid():
                newpart = newPartForm.save(commit=False)
                newpart.animal = a
                newpart.save()
        return redirect(animal, animal_id=animal_id)

    else:
        newPartForm = NewPartForm()
        formsets =  {p.pk: MeasurementsFormSet(instance=p) for p in a.part_set.all()}
        partforms = {p.pk: PartForm(instance=p) for p in a.part_set.all()}
        overwrite_forms = {p.pk: OverwriteForm(instance=p) for p in a.part_set.all()}
        stateforms = {p.pk: StateSelectForm(instance=p) for p in a.part_set.all()}
        notesform = AnimalNotesForm(instance=a)

    return render(request, 'animal_app/animal.html',
        {'user': request.user, 'animal': a, 'newPartForm': newPartForm,
        'partforms': partforms, 'formsets': formsets, 'notesform': notesform,
        'overwrite_forms': overwrite_forms, 'stateforms': stateforms})

@login_required
def delete_part(request, part_id):
    p = get_object_or_404(Part, pk=part_id)

    if request.user.has_perm('edit_animals', p.animal.collection):
        p.delete()

    return redirect(animal, animal_id=p.animal.pk)


@login_required
def user_home(request):
    default_collection = Collection.objects.filter(name='default').first()
    if not request.user.has_perm('edit_animals', default_collection):
        assign_perm('edit_animals', request.user, default_collection)

    if request.method == "POST":
        newAnimalForm = AnimalForm(request.POST)
        if newAnimalForm.is_valid():
            newAnimal = newAnimalForm.save(commit=False)
            newAnimal.user = request.user
            newAnimal.save()

    else:
        newAnimalForm = AnimalForm()

    return render(request, 'animal_app/user_home.html',
        {'user': request.user, 'newAnimalForm': newAnimalForm})

@login_required
def delete_animal(request, animal_id):
    a = get_object_or_404(Animal, pk=animal_id)
    if request.user.has_perm('edit_animals', a.collection):
        a.delete()

    return redirect(user_home)
