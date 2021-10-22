##########################################
# Semiconductor Calculations Package
# Author: Nithin Kumar Santha Kumar
# Date: 10/10/2021
##########################################
# Changelog: 
# 4/25/2021 - Started Package
# 10/10/2021 - Started periodic table of elements (materials.py)
# 10/19/2021 - Added more functionality
##########################################

CRYSTAL_ORIENTATION = ['Simple Cubic','Face-centered Cubic', 
                       'Body-centered Cubic', 'Simple Tetragonal',
                       'Body-centered Tetragonal', 'Simple Orthorhombic',
                       'Base-centered Orthorhombic', 'Body-centered Orthorhombic',
                       'Face-centered Orthorhombic', 'Simple Monoclinic',
                       'Base-centered Monoclinic', 'Triclinic', 'Trigonal',
                       'Hexagonal', '']

ALLOYS = ['Binary', 'Ternary', 'Quaternary', '']

GROUP = ['I','II','III','IV','V','VI','VII','VIII',
         'II-VI','III-V','IV-IV','IV-VI',ALLOYS, '']


class Si:

   group = GROUP[3]
   crystal_orientation = CRYSTAL_ORIENTATION[1] #FCC

   def __init__(self):
      self.__abstemp = 300 #Kelvin
      self.__Eg = 123 #eV
      self.__dieletricConstant = 4.6 #Epsilon_R

   def setTemp(self, absTemp):
      self.__abstemp = absTemp
   
   def setBandgap(self, eg):
      self.__Eg = eg
   
   def setDieletricConstant(self, epsilon_r):
      self.__dieletricConstant = epsilon_r

class Ge:
   pass