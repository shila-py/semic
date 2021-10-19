##########################################
# Semiconductor Calculations Package
# Author: Nithin Kumar Santha Kumar
# Date: 10/10/2021
##########################################
# Changelog: 
# 4/25/2021 - Started Package
# 10/10/2021 - Started periodic table of elements (materials.py)
# 
##########################################

CRYSTAL_ORIENTATION = ['FCC', 'BCC', '']
GROUP = ['I','II','III','IV','V','VI','VII','VIII',
         'II-VI','III-V']

class Si:

   group = GROUP[3]
   crystal_orientation = CRYSTAL_ORIENTATION[0]

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

class Ga:

   group = GROUP[2]
   crystal_orientation = CRYSTAL_ORIENTATION[1]

   def __init__(self):
      self.__abstemp = 300 #Kelvin
      self.__Eg = 123 #eV

   def setTemp(self, absTemp):
      self.__abstemp = absTemp
   
   def setBandgap(self, eg):
      self.__Eg = eg
