"""
functions.py
A python package for analyzing and visualizing xyz file. MolSSI Best Practices Workshop

Handles the primary functions
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

#%matplotlib notebook


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "Too cool for this MOLEcool!"
    if with_attribution:
        quote += "\n\t- Aatish's humour 101"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
