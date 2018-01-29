import logging
logger = logging.getLogger("debugging")
from math import pi, tan
from decimal import Decimal

# Note: all shapes defined in this file must be added to
# animal_app/management/commands/create_shapes.py
# in order to be added to the database.

dpi = Decimal(pi)


def pythag(a, b):
    return (a*a + b*b).sqrt();


def circle_area(r):
    return dpi * r * r


def circle_perimiter(r):
    return 2 * dpi * r


def isosceles_perimiter(h, b):
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

    @staticmethod
    def get_sa(measures):

        return  measures['length'] * measures['height'] * 2 + \
                measures['length'] * measures['width']  * 2 + \
                measures['width']  * measures['height'] * 2

    @staticmethod
    def get_vol(measures):
        return measures['length'] * measures['height'] * measures['width']


class RectangularPyramid:
    dimensions = ["length", "width", "height"]
    readable_name = "Rectangular Pyramid"

    @staticmethod
    def get_sa(measures):
        return  measures['length'] * measures['width'] + \
                measures['width']  * pythag(measures['height'], measures['length']/2) + \
                measures['length'] * pythag(measures['height'], measures['width'] /2)

    @staticmethod
    def get_vol(measures):
        return measures['length'] * measures['height'] * measures['width'] / 3


class Cylinder:
    dimensions = ["radius", "height"]
    readable_name = "Cylinder"

    @staticmethod
    def get_sa(measures):
        return  2 * dpi * measures['radius']**2 + \
                2 * dpi * measures['radius'] * measures['height']

    @staticmethod
    def get_vol(measures):
        return dpi * measures['radius']**2 * measures['height']


class HalfCylinder:
    dimensions = ["radius", "height"]
    readable_name = "Half Cylinder"

    @staticmethod
    def get_sa(measures):
        return  dpi * measures['radius']**2 + \
                dpi * measures['radius'] * measures['height'] + \
                2 * measures['radius'] * measures['height']

    @staticmethod
    def get_vol(measures):
        return dpi * measures['radius']**2 * measures['height'] / 2


class TriangularPrismIsosceles:
    dimensions = ["triangle base", "triangle height", "prism height"]
    readable_name = "Triangular Prism (Isosceles)"

    @staticmethod
    def get_sa(measures):
        return prism_sa(
            p = isosceles_perimiter(
                b = measures['triangle base'],
                h = measures['triangle height']
            ),
            h = measures['prism height'],
            base_a = measures['triangle base'] * measures['triangle height'] / 2
        )

    @staticmethod
    def get_vol(measures):
        return Decimal(0.5) * \
            measures['triangle base'] * \
            measures['triangle height'] * \
            measures['prism height']

class TriangularPrismRight:
    dimensions = ["first leg", "secound leg", "prism height"]
    readable_name = "Triangular Prism (Right)"

    @staticmethod
    def get_sa(measures):
        return prism_sa(
            p = right_perimiter(
                a = measures['first leg'],
                b = measures['secound leg']
            ),
            h = measures['prism height'],
            base_a = measures['first leg'] * measures['secound leg'] / 2
        )

    @staticmethod
    def get_vol(measures):
        return Decimal(0.5) * \
            measures['first leg'] * \
            measures['secound leg'] * \
            measures['prism height']


class Cone:
    dimensions = ["radius", "height"]
    readable_name = "Cone"

    @staticmethod
    def get_sa(measures):
        return  circle_area(measures['radius']) + \
                circle_perimiter(measures['radius']) * \
                pythag(measures['height'], measures['radius']) / 2

    @staticmethod
    def get_vol(measures):
        return circle_area(measures['radius']) * measures['height'] / 3


def right_trapezoidal_perimeter(l, s, w):
    return l+s+w + pythag(w,l-s)


def isosceles_trapezoidal_perimeter(l, s, w):
    return l+s + 2*pythag(w,(l-s)/2)


class TrapezoidalPrismRight:
    readable_name = "Trapezoidal Prism Right"

    dimensions = [
        "short side",
        "long side",
        "trapezoid width",
        "prism height"
    ]

    @staticmethod
    def get_vol(measures):
        return (measures['short side']+measures['long side']) / 2  * \
                measures['trapezoid width'] * measures['prism height']

    @staticmethod
    def get_sa(measures):
        return prism_sa(
            p=right_trapezoidal_perimeter(
                l = measures['long side'],
                s = measures['short side'],
                w = measures['trapezoid width']
            ),
            h = measures['prism height'],
            base_a = (measures['short side']+measures['long side']) / 2  * \
                      measures['trapezoid width']
        )


class TrapezoidalPrismIsosceles:
    readable_name = "Trapezoidal Prism Isosceles"

    dimensions = [
        "short side",
        "long side",
        "trapezoid width",
        "prism height"
    ]

    @staticmethod
    def get_vol(measures):
        return (measures['short side']+measures['long side']) / 2  * \
                measures['trapezoid width'] * measures['prism height']

    @staticmethod
    def get_sa(measures):
        return prism_sa(
            p=isosceles_trapezoidal_perimeter(
                l = measures['long side'],
                s = measures['short side'],
                w = measures['trapezoid width']
            ),
            h = measures['prism height'],
            base_a = (measures['short side']+measures['long side']) / 2  * \
                      measures['trapezoid width']
        )


class PentagonalPrism:
    readable_name = "Pentagonal Prism (Rect. w/o Corner)"

    dimensions = [
        "width",
        "short width",
        "length",
        "short length",
        "prism height"
    ]

    @staticmethod
    def base_area(measures):
        triangleArea = (measures["width"]  - measures["short width"]) * \
                       (measures["length"] - measures["short length"]) / 2
        return measures['length'] * measures['width'] - triangleArea

    @staticmethod
    def get_vol(measures):
        return measures['prism height'] * PentagonalPrism.base_area(measures)

    @staticmethod
    def get_sa(measures):
        perimeter = measures['width'] + \
                    measures['short width'] + \
                    measures['length'] + \
                    measures['short length'] + \
                    pythag(
                        measures['width']  - measures['short width'],
                        measures['length'] - measures['short length']
                    )

        return prism_sa(
            p = perimeter,
            h = measures['prism height'],
            base_a = PentagonalPrism.base_area(measures)
        )


class HousePentagonalPrism:
    readable_name = "Pentagonal Prism (House)"

    dimensions = [
        "full height",
        "side height",
        "base width",
        "prism height"
    ]

    @staticmethod
    def base_area(measures):
        return measures["base width"] * \
                       (measures["full height"] + measures["side height"]) / 2

    @staticmethod
    def get_vol(measures):
        return measures['prism height'] * HousePentagonalPrism.base_area(measures)

    @staticmethod
    def get_sa(measures):
        perimeter = measures['base width'] + \
                    2 * measures['side height'] + \
                    2 * pythag(
                        measures['full height']  - measures['side height'],
                        measures['base width'] / 2
                    )

        return prism_sa(
            p = perimeter,
            h = measures['prism height'],
            base_a = HousePentagonalPrism.base_area(measures)
        )


class RegularPyramid:
    readable_name = "Regular Pyramid"

    dimensions = [
        "number of sides",
        "side length",
        "pyramid height"
    ]

    @staticmethod
    def apothem(measures):
        if (measures['number of sides'] > 0):
            return measures['side length'] / Decimal(2 *
                    tan(pi / int(measures['number of sides'])))
        else:
            return 0

    @staticmethod
    def base_area(measures):
        return measures['number of sides'] * measures['side length'] * \
               RegularPyramid.apothem(measures) / 2

    @staticmethod
    def get_vol(measures):
        return RegularPyramid.base_area(measures) * measures["pyramid height"] / 3

    @staticmethod
    def get_sa(measures):
        apex_to_midpoint = pythag(RegularPyramid.apothem(measures), measures['pyramid height'])
        side_area = apex_to_midpoint * measures['side length'] / 2
        return RegularPyramid.base_area(measures) + side_area * measures['number of sides']


class RegularPrism:
    readable_name = "Regular Prism"

    dimensions = [
        "number of sides",
        "side length",
        "prism height"
    ]

    @staticmethod
    def apothem(measures):
        if (measures['number of sides'] > 0):
            return measures['side length'] / Decimal(2 *
                    tan(pi / int(measures['number of sides'])))
        else:
            return 0

    @staticmethod
    def base_area(measures):
        return measures['number of sides'] * measures['side length'] * \
               RegularPrism.apothem(measures) / 2

    @staticmethod
    def get_vol(measures):
        return RegularPrism.base_area(measures) * measures["prism height"]

    @staticmethod
    def get_sa(measures):
        return prism_sa(
            p = measures['side length'] * measures['number of sides'],
            h = measures['prism height'],
            base_a = RegularPrism.base_area(measures)
        )


class GeneralPrism:
    readable_name = "General Prism"

    dimensions = [
        'base area',
        'perimeter',
        'prism height'
    ]

    @staticmethod
    def get_vol(measures):
        return measures['base area']*measures['prism height']

    @staticmethod
    def get_sa(measures):
        return 2*measures['base area'] + measures['perimeter']*measures['prism height']


class LopRectPrism:
    readable_name = "Lopped-Rectangle Prism"

    dimensions = [
        'length',
        'width',
        'prism height',
        'corner A lengthwise cut',
        'corner A widthwise cut',
        'corner B lengthwise cut',
        'corner B widthwise cut',
        'corner C lengthwise cut',
        'corner C widthwise cut',
        'corner D lengthwise cut',
        'corner D widthwise cut',
    ]

    @staticmethod
    def base_area(measures):
        return measures['width']*measures['length'] \
               - (measures['corner A lengthwise cut']*measures['corner A widthwise cut'])/2 \
               - (measures['corner B lengthwise cut']*measures['corner B widthwise cut'])/2 \
               - (measures['corner C lengthwise cut']*measures['corner C widthwise cut'])/2 \
               - (measures['corner D lengthwise cut']*measures['corner D widthwise cut'])/2

    @staticmethod
    def perimeter(measures):
        return 2*measures['width'] + 2*measures['length'] \
               - measures['corner A lengthwise cut'] - measures['corner A widthwise cut'] \
               - measures['corner B lengthwise cut'] - measures['corner B widthwise cut'] \
               - measures['corner C lengthwise cut'] - measures['corner C widthwise cut'] \
               - measures['corner D lengthwise cut'] - measures['corner D widthwise cut'] \
               + LopRectPrism.diagonal(measures, 'A') \
               + LopRectPrism.diagonal(measures, 'B') \
               + LopRectPrism.diagonal(measures, 'C') \
               + LopRectPrism.diagonal(measures, 'D')

    @staticmethod
    def diagonal(measures, corner):
        return pythag(measures['corner ' + corner + ' lengthwise cut'],measures['corner ' + corner + ' widthwise cut'])

    @staticmethod
    def get_vol(measures):
        return LopRectPrism.base_area(measures) * measures['prism height']

    @staticmethod
    def get_sa(measures):
        return LopRectPrism.base_area(measures)*2 + LopRectPrism.perimeter(measures)*measures['prism height']


class OtherShape:
    readable_name = "Other Shape"

    dimensions = [
        'surface area',
        'volume'
    ]

    @staticmethod
    def get_vol(measures):
        return measures['volume']

    @staticmethod
    def get_sa(measures):
        return measures['surface area']


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
