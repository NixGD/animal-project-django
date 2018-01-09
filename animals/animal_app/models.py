from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .shapeObjects import *
import logging

logger = logging.getLogger("debugging")

logger.debug("test")


class Animal(models.Model):
    student = models.CharField(max_length = 50)
    animal = models.CharField(max_length = 50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, default="")

    @property
    def unchecked_count(self):
        return self.part_set.filter(checked=True).count()

    def __str__(self):
        return "{} ({})".format(self.animal, self.student)

    @property
    def total_vol(self):
        return sum([p.vol*p.quantity for p in self.part_set.all()])

    @property
    def total_sa(self):
        return sum([p.sa*p.quantity for p in self.part_set.all()])


class ShapeManager(models.Manager):

    def createShape(self, name):
        shape_obj = eval(name)
        created = self.create(class_name=name, name=shape_obj.readable_name)
        for d in shape_obj.dimensions:
            Dimension.objects.create(name=d, shape=created)

class Shape(models.Model):
    class_name = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    shapes = ShapeManager()

    def __str__(self):
        return self.name


class Part(models.Model):
    name = models.CharField(max_length = 50)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    shape = models.ForeignKey(Shape, on_delete=models.PROTECT)
    checked = models.BooleanField(default=False)
    initiallycorrect = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    overwritten_sa  = models.DecimalField(decimal_places = 1, max_digits=8, blank=True, null=True)
    overwritten_vol = models.DecimalField(decimal_places = 1, max_digits=8, blank=True, null=True)

    def get_measurment_dict(self):
        return {m.dimension.name: m.value for m in self.measurments.all()}

    @property
    def calculated_sa(self):
        return eval(self.shape.class_name).get_sa(self.get_measurment_dict())

    @property
    def calculated_vol(self):
        return eval(self.shape.class_name).get_vol(self.get_measurment_dict())

    @property
    def sa(self):
        return self.calculated_sa if self.overwritten_sa is None else self.overwritten_sa

    @property
    def vol(self):
        return self.calculated_vol if self.overwritten_vol is None else self.overwritten_vol

    def __str__(self):
        return "{} ({})".format(self.name, self.animal.student)

    class Meta:
        ordering = ['pk']


class Dimension(models.Model):
    name = models.CharField(max_length = 50)
    shape = models.ForeignKey(Shape, on_delete=models.CASCADE,
        related_name='dimensions')

    def __str__(self):
        return "{} of {}".format(self.name, self.shape)


class MeasurementManager(models.Model):
    @receiver(post_save)
    def create_measurements(sender, instance, created, **kwargs):
        if sender == Part:
            if created:
                for d in instance.shape.dimensions.all():
                    Measurement.objects.create(dimension=d, part=instance, value=0)


class Measurement(models.Model):
    dimension = models.ForeignKey(Dimension, on_delete=models.CASCADE)
    part = models.ForeignKey(Part,
        on_delete=models.CASCADE, related_name = 'measurments')
    value = models.DecimalField(decimal_places = 1, max_digits = 8)
    measurements = MeasurementManager()

    def __str__(self):
        return "{} of {} ({})".format(
            self.dimension.name,
            self.part.name,
            self.part.animal.student)
