"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

    :param data: 2d numpy data array (each column is a measurement occasion, each row
    row is a day)
    :returns: column-wise mean of data points
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: 2d numpy data array (each column is a measurement occasion,
    each row is a day)
    :returns: column-wise maximum of data points
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: 2d numpy data array (each column is a measurement occasion,
    each row is a day)
    :returns: column-wise minimum of data points
    """
    return np.min(data, axis=0)


# TODO(lesson-design) Add Patient class
# TODO(lesson-design) Implement data persistence
# TODO(lesson-design) Add Doctor class
