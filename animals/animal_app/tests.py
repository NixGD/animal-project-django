from django.test import TestCase
from .shapeObjects import \
    RectangularPrism, \
    Cylinder, Cone, \
    TriangularPrismIsosoles, TriangularPrismRight
from math import pi, sqrt
from decimal import Decimal

l = 2
h = 3
w = 5
r = 7
tri_base = 11
tri_h = 13

measures = {
    "length": l,
    "height": h,
    "width": w,
    "radius": r,
    "triangle base": tri_base,
    "triangle height": tri_h,
    "prism height": h,
    "first leg": tri_base,
    "secound leg": tri_h
}

decimal_measures = {key: Decimal(value) for key, value in measures.items()}


def pythag(a, b):
    return sqrt(a*a + b*b);

class ShapeCalculationTests(TestCase):

    def sa_and_vol(self, shape, vol=None, sa=None):
        self.assertAlmostEqual(shape.get_vol(decimal_measures), Decimal(vol))
        self.assertAlmostEqual(shape.get_sa(decimal_measures),  Decimal(sa))

    def testRectangularPrism(self):
        self.sa_and_vol(RectangularPrism,
            vol=l*w*h,
            sa= 2*(l*w + w*h + h*l))

    def testCylinder(self):
        self.sa_and_vol(Cylinder,
            vol=pi*r*r*h,
            sa= 2*pi*r * h + pi*r*r*2
            )

    def testTriPrismIsoc(self):
        self.sa_and_vol(TriangularPrismIsosoles,
            vol = 0.5 * tri_base * tri_h * h,
            sa  = h*(pythag(tri_h, tri_base/2)*2 + tri_base) + 2 * 0.5 * tri_h * tri_base
		)

    def testTriPrismRight(self):
        self.sa_and_vol(TriangularPrismRight,
            vol = 0.5 * tri_base * tri_h * h,
            sa  = h*(pythag(tri_h, tri_base) + tri_base + tri_h) + 2 * 0.5 * tri_h * tri_base
		)

    def testCone(self):
        self.sa_and_vol(Cone,
            vol = pi*r*r*h/3,
            sa  = pi*r*r + pi*r*pythag(r,h)
        )
