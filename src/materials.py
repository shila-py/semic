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

CRYSTAL_STRUCTURE = ['Diamond', 'Zincblende', 'Wurzite', 'Rock-Salt', '']

ALLOYS = ['Binary', 'Ternary', 'Quaternary', '']

GROUP = ['I','II','III','IV','V','VI','VII','VIII',
         'II-VI','III-V','IV-IV','IV-VI',ALLOYS, '']

'''
BEGIN ELEMENTAL SEMICONDUCTORS
'''
class Si:

   group = GROUP[3] #Group IV Semiconductor
   crystal_structure = CRYSTAL_STRUCTURE[0] #Diamond
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
   #Crystal_Structure : Diamond
   group = GROUP[3] # Group IV Semiconductor
   crystal_structure = CRYSTAL_STRUCTURE[0] #Diamond
   crystal_orientation = CRYSTAL_ORIENTATION[1] #
   pass
'''
END OF ELEMENTAL SEMICONDUCTORS
'''

'''
BEGIN COMPOUND SEMICONDUCTORS
'''
'''
IV-IV
'''
class SiC:
   #Group: IV-IV
   pass
'''
III-V
'''
class AlP:
   pass

class AlAs:
   pass

class AlSb:
   pass

class GaN:
   pass

class GaP:
   pass

class GaAs:
   #Crystal Structure : Zincblende
   pass

class GaSb:
   pass

class InP:
   pass

class InAs:
   pass

class InSb:
   pass
'''
II-VI
'''
class ZnO:
   pass

class ZnS:
   pass

class ZnSe:
   pass

class ZnTe:
   pass

class CdS:
   pass

class CdSe:
   pass

class CdTe:
   pass

class HgS:
   pass
'''
IV-VI
'''
class PbS:
   pass

class PbSe:
   pass

class PbTe:
   pass
'''
END COMPOUND SEMICONDUCTORS
'''

'''
BEGIN ALLOY SEMICONDUCTORS
'''
'''
Binary
'''
class SiGe:
   # 1-x : x
   pass
'''
Ternary
'''
class AlGaAs:
   # x : 1-x : 1
   pass

class AlGaN:
   # x : 1-x : 1
   pass

class AlGaSb:
   pass

class CdMnTe:
   pass

class GaAsP:
   pass

class HgCdTe:
   pass

class InAlAs:
   pass

class InGaAs:
   pass

class InGaN:
   pass
'''
Quaternary
'''
class AlGaAsSb:
   pass

class GaInAsP:
   pass
'''
END ALLOY SEMICONDUCTORS
'''