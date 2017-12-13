import logging
logger = logging.getLogger("debugging")
from math import pi

class RectangularPrism:
    dimensions = ["length", "width", "height"]
    readable_name = "Rectangular Prism"
    def get_sa(measures):

        return  measures['length'] * measures['height'] * 2 + \
                measures['length'] * measures['width']  * 2 + \
                measures['width']  * measures['height'] * 2

    def get_vol(measures):
        return measures['length'] * measures['height'] * measures['length']

class Cylinder:
    dimensions = ["radius", "height"]
    readable_name = "Cylinder"

    def get_sa(measures):
        logger.info(measures)
        logger.info(pi*measures['radius'])
        return  2 * pi * measures['radius']**2 + \
                2 * pi * measures['height']

    def get_vol(measures):
        return pi * measures['radius']**2 * measures['height']
