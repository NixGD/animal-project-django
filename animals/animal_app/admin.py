from django.contrib import admin
from .models import Animal, Part, Measurement, Shape, Dimension, Collection
from guardian.admin import GuardedModelAdmin

class AnimalAdmin(GuardedModelAdmin):
    pass

class CollectionAdmin(GuardedModelAdmin):
    pass

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Collection, CollectionAdmin)

admin.site.register(Part)
admin.site.register(Measurement)
admin.site.register(Shape)
admin.site.register(Dimension)
