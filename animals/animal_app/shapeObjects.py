import logging
logger = logging.getLogger("debugging")
from math import pi
from decimal import Decimal

dpi = Decimal(pi)

def pythag(a, b):
    return (a*a + b*b).sqrt();

def circle_area(r):
    return dpi * r * r

def circle_perimiter(r):
    return 2 * dpi * r

def isosoles_perimiter(h, b):
    side_len = pythag(b / 2, h)
    return 2 * side_len + b

def right_perimiter(a, b):
    c = pythag(a, b)
    return a + b + c

def prism_sa(p, h, base_a):
    return p*h + base_a*2

class RectangularPrism:
    dimensions = ["length", "width", "height"]
    readable_name = "Rectangular Prism"
    def get_sa(measures):

        return  measures['length'] * measures['height'] * 2 + \
                measures['length'] * measures['width']  * 2 + \
                measures['width']  * measures['height'] * 2

    def get_vol(measures):
        return measures['length'] * measures['height'] * measures['width']

class Cylinder:
    dimensions = ["radius", "height"]
    readable_name = "Cylinder"

    def get_sa(measures):
        return  2 * dpi * measures['radius']**2 + \
                2 * dpi * measures['radius'] * measures['height']

    def get_vol(measures):
        return dpi * measures['radius']**2 * measures['height']

class TriangularPrismIsosoles:
    dimensions = ["triangle base", "triangle height", "prism height"]
    readable_name = "Triangular Prism (Isosoles)"

    def get_sa(measures):
        return prism_sa(
            p = isosoles_perimiter(
                b = measures['triangle base'],
                h = measures['triangle height']
            ),
            h = measures['prism height'],
            base_a = measures['triangle base'] * measures['triangle height'] / 2
        )

    def get_vol(measures):
        return Decimal(0.5) * \
            measures['triangle base'] * \
            measures['triangle height'] * \
            measures['prism height']

class TriangularPrismRight:
    dimensions = ["first leg", "secound leg", "prism height"]
    readable_name = "Triangular Prism (Right)"

    def get_sa(measures):
        return prism_sa(
            p = right_perimiter(
                a = measures['first leg'],
                b = measures['secound leg']
            ),
            h = measures['prism height'],
            base_a = measures['first leg'] * measures['secound leg'] / 2
        )

    def get_vol(measures):
        return Decimal(0.5) * \
            measures['first leg'] * \
            measures['secound leg'] * \
            measures['prism height']

class Cone:
    dimensions = ["radius", "height"]
    readable_name = "Cone"

    def get_sa(measures):
        return  circle_area(measures['radius']) + \
                circle_perimiter(measures['radius']) * \
                pythag(measures['height'], measures['radius']) / 2

    def get_vol(measures):
        return circle_area(measures['radius']) * measures['height'] / 3

	# RectangularPyramid: {
	# 	name: "Rectangular Pyramid",
	# 	dimensionNames: [
	# 	"Width",
	# 	"Length",
	# 	"Height"
	# 	],
	# 	findVolume: function(w,l,h) {
	# 		return (h*w*l/3);
	# 	},
	# 	findSurfaceArea: function(w,l,h) {
	# 		return (w*l + w*app.pythag(l/2, h) + l*app.pythag(w/2,h));
	# 	}
	# },
	# TrapezoidalPrismRight: {
	# 	name: "Trapezoidal Prism (Right)",
	# 	dimensionNames: [
	# 	"Short Side",
	# 	"Long Side",
	# 	"Trapaziod Width",
	# 	"Prism Height"
	# 	],
	# 	findVolume: function(s,l,w,h) {
	# 		return ((s+l)/2 * w * h);
	# 	},
	# 	findSurfaceArea:function(s,l,w,h) {
	# 		return( (s+l)*w + h* (l+s+w + app.pythag(w,l-s)) );
	# 	}
	# },
	# TrapezoidalPrismIsosoles: {
	# 	name: "Trapezoidal Prism (Isosoles)",
	# 	dimensionNames: [
	# 	"Short Side",
	# 	"Long Side",
	# 	"Trapaziod Width",
	# 	"Prism Height"
	# 	],
	# 	findVolume: function(s,l,w,h) {
	# 		return ((l+s)/2 * w * h);
	# 	},
	# 	findSurfaceArea:function(s,l,w,h) {
	# 		return ( (l+s)*w + h*(l+s + 2*app.pythag(w,(l-s)/2) ));
	# 	}
    #
	# },
	# PentagonalPrism: {
	# 	name: "Pentagonal Prism",
	# 	info: "A rectangle with one corner cut off.",
	# 	dimensionNames: [
	# 	"Width",
	# 	"Short Width",
	# 	"Length",
	# 	"Short Length",
	# 	"Height"
	# 	],
	# 	findVolume: function(w, sw, l, sl, h) {
	# 		triangleArea = 0.5*(w-sw)*(l-sl);
	# 		return h* (l*w - triangleArea);
	# 	},
	# 	findSurfaceArea: function(w, sw, l, sl, h) {
	# 		baseArea =  l*w - 0.5*(w-sw)*(l-sl);
	# 		var perimeter = w+sw+l+sl+app.pythag(w-sw,l-sl);
	# 		return baseArea*2 + h*perimeter;
	# 	}
	# },
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
	# 		var perimeter = b + 2*sh + 2*app.pythag(hh-sh, 0.5*b);
	# 		baseArea = 0.5*b*(hh+sh);
	# 		return perimeter*ph + 2*baseArea;
	# 	}
	# },
	# HexagonalPrismRight: {
	# 	name: "Hexagonal Prism (Right)",
	# 	info: "A rectangle with two equal corners cut off.",
	# 	dimensionNames: [
	# 	"Full Width",
	# 	"Side Width",
	# 	"Length",
	# 	"Short Length",
	# 	"Height"
	# 	],
	# 	findVolume: function(w, sw, l, sl, h) {
	# 		return h*(l*w - 0.5*(w-sw)*(l-sl));
	# 	},
	# 	findSurfaceArea: function(w, sw, l, sl, h) {
	# 		var perimeter = 2*sw + l + sl + 2*app.pythag(w-sw, (l-sl)/2);
	# 		return (l*w - 0.5*(w-sw)*(l-sl))*2 + h*perimeter;
	# 	}
	# },
	# HexagonalPrismRegular: {
	# 	name: "Hexagonal Prism (Regular)",
	# 	dimensionNames: [
	# 	"Side length",
	# 	"Height"
	# 	],
	# 	findVolume: function(s, h) {
	# 		return h*3*Math.sqrt(3)*s*s/2;
	# 	},
	# 	findSurfaceArea: function(s, h) {
	# 		return 3*Math.sqrt(3)*s*s + 6*s*h;
	# 	}
	# },
	# OctagonalPrism: {
	# 	name: "Octagonal Prism",
	# 	info: "A rectangle with all its corners cut off equally.  Not necessarily a regular Octagon",
	# 	dimensionNames: [
	# 	"Full Width",
	# 	"Side Width",
	# 	"Full Length",
	# 	"Side Length",
	# 	"Height"
	# 	],
	# 	findVolume: function(w, sw, l, sl, h) {
	# 		return (h*(l*w - 0.5*(w-sw)*(l-sl)));
	# 	},
	# 	findSurfaceArea: function(w, sw, l, sl, h) {
	# 		return ( (l*w - 0.5*(w-sw)*(l-sl))*2 + h*2*(sl+sw+2*app.pythag((w-sw)/2,(l-sl)/2)));
	# 	}
	# },
	# parallelogramPrism: {
	# 	name: "Parallelogram Prism",
	# 	info: "Offset is in the same direction as width.  Height is the height of the parallelogram.",
	# 	dimensionNames: [
	# 	"Width",
	# 	"Offset",
	# 	"Height",
	# 	"Prism Height"
	# 	],
	# 	findVolume: function(w, o, h, ph) {
	# 		return (w*h*ph);
	# 	},
	# 	findSurfaceArea: function(w, o, h, ph) {
	# 		var perimeter = 2*(w+app.pythag(o, h));
	# 		return (perimeter*ph + 2*(w*h));
	# 	}
	# },
	# Other: {
	# 	name: "Other",
	# 	dimensionNames: [
	# 	"Volume",
	# 	"Surface Area"
	# 	],
	# 	findVolume: function(volume, _) {
	# 		return volume;
	# 	},
	# 	findSurfaceArea: function(_, surfaceArea) {
	# 		return surfaceArea;
	# 	}
	# }};
