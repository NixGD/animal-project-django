from django.test import TestCase
from .shapeObjects import \
    RectangularPrism, RectangularPyramid, \
    Cylinder, Cone, HalfCylinder, \
    TriangularPrismIsosceles, TriangularPrismRight, \
    TrapezoidalPrismRight, TrapezoidalPrismIsosceles, \
    PentagonalPrism, HousePentagonalPrism, \
    RegularPrism, RegularPyramid

from math import pi, sqrt
from decimal import Decimal

l = 2
h = 3
w = 5
r = 7
tri_base = 11
tri_h = 13
ss = 17 #short side
ls = 19 #long side
sw = 3
sl = 4
fh = 21
sh = 19
n = 4
s = 7

measures = {
    "length": l,
    "height": h,
    "width": w,
    "radius": r,
    "triangle base": tri_base,
    "triangle height": tri_h,
    "prism height": h,
    "first leg": tri_base,
    "secound leg": tri_h,
    "short side": ss,
    "long side": ls,
    "trapezoid width": w,
    "short width": sw,
    "short length": sl,
    "full height": fh,
    "short height": sh,
    "side height": sh,
    "base width": w,
    "number of sides": n,
    "side length": s,
    "pyramid height": h
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
            sa= 2*(l*w + w*h + h*l)
        )

    def testRectangularPry(self):
        self.sa_and_vol(RectangularPyramid,
            vol=l*w*h/3,
            sa= l*w + l*pythag(h,w/2) + w*pythag(h, l/2)
        )

    def testCylinder(self):
        self.sa_and_vol(Cylinder,
            vol=pi*r*r*h,
            sa= 2*pi*r * h + pi*r*r*2
            )

    def testTriPrismIsoc(self):
        self.sa_and_vol(TriangularPrismIsosceles,
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

    def testTrapPrismRight(self):
        self.sa_and_vol(TrapezoidalPrismRight,
            vol = ((ss+ls)/2 * w * h),
            sa = (ss+ls)*w   +   h * (ls + ss + w  + pythag(w,ls-ss))
        )

    def testTrapPrismIsos(self):
        self.sa_and_vol(TrapezoidalPrismIsosceles,
            vol = ((ss+ls)/2 * w * h),
            sa  = (ls+ss)*w + h*(ls+ss + 2*pythag(w,(ls-ss)/2) )
        )

    def testPentagonalPrism(self):
        base = l*w - 0.5*(w-sw)*(l-sl)
        p = w+sw+l+sl + pythag(w-sw,l-sl)

        self.sa_and_vol(PentagonalPrism,
            vol = h * base,
            sa  = base*2 + h * p
        )

    def testHousePentagonalPrism(self):
        base = 0.5*w*(fh+sh)
        p = w + 2*sh + 2*pythag(fh-sh, 0.5*w)

        self.sa_and_vol(HousePentagonalPrism,
            vol = h * base,
            sa  = base*2 + h * p
        )

    def testRegularPrism(self):
        assert n == 4
        self.sa_and_vol(RegularPrism,
            vol = s**2 * h,
            sa  = 2*s**2 + 4*s*h
        )

    def testRegularPyr(self):
        assert n == 4
        self.sa_and_vol(RegularPyramid,
            vol = s**2 * h / 3,
            sa  = s**2 + pythag(s/2,h)*s*2
        )

    def testHalfCyl(self):
        self.sa_and_vol(HalfCylinder,
            vol = pi*r**2 * h / 2,
            sa  = (pi*r + 2*r)*h + pi*r**2
        )
        	# HousePentagonalPrism: {
        	# 	name: "House Pentagonal Prism",
        	# 	info: "A rectangle with a triangle on top. House height is measured from apex to base, parallel to side heights.",
        	# 	dimensionNames: [
        	# 	"House Height",
        	# 	"Side Height",
        	# 	"Base Width",
        	# 	"Prism Height"
        	# 	],
        	# 	findVolume: function(hh, sh, b, ph) {
        	# 		return 0.5*b*ph*(hh+sh);
        	# 	},
        	# 	findSurfaceArea: function(hh, sh, b, ph) {
        	# 		var perimeter =
        	# 		baseArea = ;
        	# 		return perimeter*ph + 2*baseArea;
        	# 	}
        	# },
