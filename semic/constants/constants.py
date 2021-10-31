##########################################
# Semiconductor Calculations Package
# Author: Nithin Kumar Santha Kumar
# Date: 10/30/2021
##########################################
# Changelog: 
# 4/25/2021 - Started Package
# 10/30/2021 - Started constants (constants.py)
# 10/30/2021 - Added more functionality
##########################################
"""
All constant values are from the 2018 CODATA publication.
More information on CODATA and their publication can be found at:
   https://physics.nist.gov/cuu/Constants/index.html and
   https://www.nist.gov/programs-projects/codata-values-fundamental-physical-constants

Any fundamental adjustments of constants will be made after the 2022 CODATA publication of 
fundamental constants.

Errors will be corrected on a more frequent basis.
"""


constants = {
            "Speed of light in vacuum" : [299792548, "m s^-1"],
            "Planck constant in J s" : [6.62607015e-34, "J s"],
            "Planck constant in eV s" : [4.135667696e-15, "eV s"],
            "Reduced Planck constant in J s" : [1.054571817e-34, "J s"],
            "Reduced Planck constant in eV s" : [6.582119569e-16, "eV s"],
            "Elementary charge" : [1.602176634e-19, "C"],
            "Vacuum magnetic permeability" : [1.25663706212e-6, "H m^-1"],
            "Vacuum electric permittivity" : [8.8541878128e-12, "F m^-1"],
            "Boltzmann constant in eV/K" : [8.617333262e-5, "eV K^-1"],
            "Boltzmann constant in J/K" : [1.380649e-23, "J K^-1"],
            "Atomic mass constant" : [1.66053906660e-27, "kg"],
            "Fine structure constant" : [7.2973525693e-3, ""],
            "Electron mass" : [9.1093837015e-31, "kg"],
            "Stefan-Boltzmann constant" : [5.670374419e-8, "W m^-2 K^-4"],
            "Rydberg constant" : [10973731.568160, "m^-1"],
            "Rydberg constant times hc in eV" : [13.605693122994, "eV"],
            "Rydberg constant times hc in J" : [2.1798723611035e-18, "J"],
            "Rydberg constant times c in Hz" : [3.2898419602508e+15, "Hz"],
            "Compton wavelength" : [2.42631023867e-12, "m"],
            "Classical electron wavelength" : [2.8179403262e-15, "m"],
            "Characteristic impedance of vacuum" : [376.730313668, "ohm"],
            "Bohr radius" : [5.29177210903e-11, "m"],
            "Electron volt in J" : [1.602176634e-19, "J"],
            "Proton mass" : [1.67262192369e-27, "kg"],
            "Neutron mass" : [1.67492749804e-27, "kg"], 
}

def value(key):
   """
   Value of constants given by key
   """
   return constants[key][0]

def units(key):
   """
   Unit of constants given by key
   """
   return constants[key][1]

def list_constants():
   """
   Lists all the constants in the constants dictionary
   """
   lst = list(constants.keys())
   print(lst)

def find_constants(search_term):
   """
   Finds constants based on search term
   """
   if search_term is None:
      list_constants()
   else:
      for key in constants:
         if search_term.lower() in key.lower():
            print(key)
