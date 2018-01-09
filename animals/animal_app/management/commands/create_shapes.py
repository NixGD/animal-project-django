from ...models import Shape
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "initializes any added shapes"

    def handle(self, *args, **options):
        shapes = ["RectangularPrism",
                  "RectangularPyramid",
                  "Cylinder",
                  "HalfCylinder",
                  "TriangularPrismIsosceles",
                  "TriangularPrismRight",
                  "Cone",
                  "TrapezoidalPrismRight",
                  "TrapezoidalPrismIsosceles",
                  "PentagonalPrism",
                  "HousePentagonalPrism",
                  "RegularPrism",
                  "RegularPyramid"]

        added_shape = False
        for s in shapes:
            if not Shape.shapes.filter(class_name=s).exists():
                Shape.shapes.createShape(s)
                self.stdout.write(self.style.SUCCESS('Added %s' % s))
                added_shape = True

        if not added_shape:
            self.stdout.write('No shapes to add')
