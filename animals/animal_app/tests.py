from django.test import TestCase
from .shapeObjects import RectangularPrism, Cylinder
from math import pi
from decimal import Decimal

l = 2
h = 3
w = 5
r = 7

measures = {
    "length": l,
    "height": h,
    "width": w,
    "radius": r
}

class ShapeCalculationTests(TestCase):

    def sa_and_vol(self, shape, vol=None, sa=None):
        self.assertAlmostEqual(shape.get_vol(measures), Decimal(vol))
        self.assertAlmostEqual(shape.get_sa(measures),  Decimal(sa))

    def testRectangularPrism(self):
        self.sa_and_vol(RectangularPrism,
            vol=l*w*h,
            sa= 2*(l*w + w*h + h*l))

    def testCylinder(self):
        self.sa_and_vol(Cylinder,
            vol=pi*r*r*h,
            sa= 2*pi*r * h + pi*r*r*2
            )
