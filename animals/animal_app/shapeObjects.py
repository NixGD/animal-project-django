import logging
logger = logging.getLogger("debugging")
from math import pi
from decimal import Decimal

dpi = Decimal(pi)

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
        logger.info(measures)
        return  2 * dpi * measures['radius']**2 + \
                2 * dpi * measures['height']

    def get_vol(measures):
        return dpi * measures['radius']**2 * measures['height']
