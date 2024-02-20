#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tues Mar 28 13:56:18 2023
@author: ashutosh
"""

from pymatgen.core import Structure

# Load the structure from POSCAR
structure = Structure.from_file("POSCAR")

# Open the original POSCAR to read header information
# and the new POSCAR_Cart file to write the modified structure
with open('POSCAR', 'r') as f1, open('POSCAR_cart', 'w') as f2:
    # Copy the header from the original POSCAR: first 7 lines
    for _ in range(7):
        f2.write(f1.readline())

    # Write the line indicating that the coordinates following are in Cartesian format
    f2.write('Cartesian\n')

    # Write the Cartesian coordinates for each site
    for site in structure:
        coords = site.coords  # pymatgen already handles coordinates as Cartesian by default in the Structure object
        f2.write("{:14f} {:14f} {:14f}\n".format(coords[0], coords[1], coords[2]))

print("Conversion complete. Cartesian coordinates saved in POSCAR_cart.")
