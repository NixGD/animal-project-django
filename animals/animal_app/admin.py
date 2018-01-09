from django.contrib import admin
from .models import Animal, Part, Measurement, Shape, Dimension

admin.site.register(Animal)
admin.site.register(Part)
admin.site.register(Measurement)
admin.site.register(Shape)
admin.site.register(Dimension)