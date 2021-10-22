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
CREATE YOUR OWN SEMICONDUCTOR
'''
class Semiconductor:
   pass

'''
BEGIN ELEMENTAL SEMICONDUCTORS
'''
class Si:
   '''
   Material Properties and Object Parameters for Silicon
   '''

   group = GROUP[3] #Group IV Semiconductor
   crystal_structure = CRYSTAL_STRUCTURE[0] #Diamond
   crystal_orientation = CRYSTAL_ORIENTATION[1] #Face-centered Cubic

   def __init__(self):
      '''
      Silicon material properties at 300 Kelvin
      '''
      self.__abstemp = 300 #Kelvin
      self.__density = 2.329 #g cm^-3
      self.__bandGap = 1.12 #eV
      self.__gapType = 'Indirect'
      self.__debyeTemp = 640 #Kelvin
      self.__intrinsicDebyeLength = 24 #microns
      self.__electronAffinity = 4.05 #eV
      self.__dieletricConstant = 11.7 #Epsilon_R a.k.a K (Kappa)
      self.__latticeConstant = 5.43095 #Angstroms
      self.__boltzmannTemp = 0.0259 #eV
      self.__intrinsicCarrierConcentration = 1E10 #cm^-3
      self.__conductionDensityOfStates = 2.8E19 #cm^-3
      self.__valenceDensityOfStates = 1.0E19 #cm^-3
      self.__intrinsicResistivity = 2.3E5 #Ohm-cm
      self.__opticalPhononEnergy = 0.063 #eV
      self.__electronDriftMobility = 1500 #cm^2 V^-1 s^-1
      self.__holeDriftMobility = 475 #cm^2 V^-1 s^-1
      self.__approxBreakdownField = 3E5 #V cm^-1
      self.__thermalConductivity = 148 #W m^-1 K^-1
      self.__thermalDiffusivity = 0.8 #cm^2 s^-1
      self.__linearThermalExpansion = 2.6E-6 #degC^-1
      self.__tempDependenceOfBandGap = -2.3E-4 #eV K^-1
      self.__refractionIndex = 3.42
      self.__augerRecombinationCoefficientN = 1.1E-30 #cm^6 s^-1
      self.__augerRecombinationCoefficientP = 3.0E-31 #cm^6 s^-1

   def setTemp(self, absTemp):
      self.__abstemp = absTemp
   
   def setDensity(self, density):
      self.__density = density

   def setBandgap(self, eg):
      self.__bandGap = eg
   
   def setGapType(self, gapType):
      self.__gapType = gapType
   
   def setDebyeTemp(self, debyeTemp):
      self.__debyeTemp = debyeTemp
   
   def setIntrinsicDebyeLength(self, debyeLength):
      self.__intrinsicDebyeLength = debyeLength

   def setElectronAffinity(self, electronAffinity):
      self.__electronAffinity = electronAffinity

   def setDieletricConstant(self, k):
      self.__dieletricConstant = k
   
   def setLatticeConstant(self, a):
      self.__latticeConstant = a

   def setBoltzmannTemp(self, kbT):
      self.__boltzmannTemp = kbT
   
   def setIntrinsicCarrierConcentration(self, ni):
      self.__intrinsicCarrierConcentration = ni
   
   def setConductionDensityOfStates(self,Nc):
      self.__conductionDensityOfStates = Nc
   
   def setValenceDensityOfStates(self,Nv):
      self.__valenceDensityOfStates = Nv
   
   def setIntrinsicResistivity(self, rho):
      self.__intrinsicResistivity = rho
   
   def setOpticalPhononEnergy(self, energy):
      self.__opticalPhononEnergy = energy
   
   def setElectronDriftMobility(self, mu_n):
      self.__electronDriftMobility = mu_n

   def setHoleDriftMobility(self, mu_p):
      self.__holeDriftMobility = mu_p

   def setApproxBreakdownField(self, field):
      self.__approxBreakdownField = field

   def setThermalConductivity(self, tc):
      self.__thermalConductivity = tc
   
   def setThermalDiffusivity(self, td):
      self.__thermalDiffusivity = td

   def setLinearThermalExpansion(self, lte):
      self.__linearThermalExpansion = lte

   def setTempDependenceOfBandGap(self, tEg):
      self.__tempDependenceOfBandGap = tEg
   
   def setRefractionIndex(self, n):
      self.__refractionIndex = n
   
   def setAugerRecombinationCoefficientN(self, Cn):
      self.__augerRecombinationCoefficientN = Cn
   
   def setAugerRecombinationCoefficientP(self, Cp):
      self.__augerRecombinationCoefficientP = Cp

class Ge:
   #Crystal_Structure : Diamond
   group = GROUP[3] # Group IV Semiconductor
   crystal_structure = CRYSTAL_STRUCTURE[0] #Diamond
   crystal_orientation = CRYSTAL_ORIENTATION[1] #Face-centered Cubic
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