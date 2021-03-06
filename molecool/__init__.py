"""
molecool
A python package for analyzing and visualizing xyz file. MolSSI Best Practices Workshop
"""

# Add imports here
from .functions import *
from .measure import calculate_angle, calculate_distance
from .visualize import draw_bond_histogram,draw_molecule
from .molecule import build_bond_list
from .atom_data import atom_colors, atomic_weights

import molecool.io


# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
