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
   '''
   Material Properties and Object Parameters for a Custom Semiconductor
   '''

   group = GROUP[13] #Empty
   crystal_structure = CRYSTAL_STRUCTURE[4] #Empty
   crystal_orientation = CRYSTAL_ORIENTATION[14] #Empty

   def __init__(self):
      '''
      Custom semiconductor material properties
      All properties are initialized to 0. 
      '''
      self.abstemp = 0 #Kelvin
      self.density = 0 #g cm^-3
      self.bandGap = 0 #eV
      self.gapType = '' #Direct/Indirect
      self.debyeTemp = 0 #Kelvin
      self.intrinsicDebyeLength = 0 #microns
      self.electronAffinity = 0 #eV
      self.dieletricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = 0 #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W m^-1 K^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
      self.tempDependenceOfBandGap = 0 #eV K^-1
      self.refractionIndex = 0
      self.augerRecombinationCoefficientN = 0 #cm^6 s^-1
      self.augerRecombinationCoefficientP = 0 #cm^6 s^-1

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
      self.abstemp = 300 #Kelvin
      self.density = 2.329 #g cm^-3
      self.bandGap = 1.12 #eV
      self.gapType = 'Indirect'
      self.debyeTemp = 640 #Kelvin
      self.intrinsicDebyeLength = 24 #microns
      self.electronAffinity = 4.05 #eV
      self.dieletricConstant = 11.7 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 5.43095 #Angstroms
      self.boltzmannTemp = 0.0259 #eV
      self.intrinsicCarrierConcentration = 1E10 #cm^-3
      self.conductionDensityOfStates = 2.8E19 #cm^-3
      self.valenceDensityOfStates = 1.0E19 #cm^-3
      self.intrinsicResistivity = 2.3E5 #Ohm-cm
      self.opticalPhononEnergy = 0.063 #eV
      self.electronDriftMobility = 1500 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 475 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 3E5 #V cm^-1
      self.thermalConductivity = 148 #W m^-1 K^-1
      self.thermalDiffusivity = 0.8 #cm^2 s^-1
      self.linearThermalExpansion = 2.6E-6 #degC^-1
      self.refractionIndex = 3.42
      self.augerRecombinationCoefficientN = 1.1E-30 #cm^6 s^-1
      self.augerRecombinationCoefficientP = 3.0E-31 #cm^6 s^-1
   
   '''
   def setTemp(self, absTemp):
      self.abstemp = absTemp
   
   def setDensity(self, density):
      self.density = density

   def setBandgap(self, eg):
      self.bandGap = eg
   
   def setGapType(self, gapType):
      self.gapType = gapType
   
   def setDebyeTemp(self, debyeTemp):
      self.debyeTemp = debyeTemp
   
   def setIntrinsicDebyeLength(self, debyeLength):
      self.intrinsicDebyeLength = debyeLength

   def setElectronAffinity(self, electronAffinity):
      self.electronAffinity = electronAffinity

   def setDieletricConstant(self, k):
      self.dieletricConstant = k
   
   def setLatticeConstant(self, a):
      self.latticeConstant = a

   def setBoltzmannTemp(self, kbT):
      self.boltzmannTemp = kbT
   
   def setIntrinsicCarrierConcentration(self, ni):
      self.intrinsicCarrierConcentration = ni
   
   def setConductionDensityOfStates(self,Nc):
      self.conductionDensityOfStates = Nc
   
   def setValenceDensityOfStates(self,Nv):
      self.valenceDensityOfStates = Nv
   
   def setIntrinsicResistivity(self, rho):
      self.intrinsicResistivity = rho
   
   def setOpticalPhononEnergy(self, energy):
      self.opticalPhononEnergy = energy
   
   def setElectronDriftMobility(self, mu_n):
      self.electronDriftMobility = mu_n

   def setHoleDriftMobility(self, mu_p):
      self.holeDriftMobility = mu_p

   def setApproxBreakdownField(self, field):
      self.approxBreakdownField = field

   def setThermalConductivity(self, tc):
      self.thermalConductivity = tc
   
   def setThermalDiffusivity(self, td):
      self.thermalDiffusivity = td

   def setLinearThermalExpansion(self, lte):
      self.linearThermalExpansion = lte
   
   def setRefractionIndex(self, n):
      self.refractionIndex = n
   
   def setAugerRecombinationCoefficientN(self, Cn):
      self.augerRecombinationCoefficientN = Cn
   
   def setAugerRecombinationCoefficientP(self, Cp):
      self.augerRecombinationCoefficientP = Cp
   '''

class Ge:
   '''
   Material Properties and Object Parameters for Germanium
   '''
   group = GROUP[3] # Group IV Semiconductor
   crystal_structure = CRYSTAL_STRUCTURE[0] #Diamond
   crystal_orientation = CRYSTAL_ORIENTATION[1] #Face-centered Cubic

   def __init__(self):
      '''
      Germanium material properties at 300 Kelvin
      '''
      self.abstemp = 300 #Kelvin
      self.density = 5.3267 #g cm^-3
      self.bandGap = 0.661 #eV
      self.gapType = 'Indirect'
      self.debyeTemp = 374 #Kelvin
      self.intrinsicDebyeLength = 0.68 #microns
      self.electronAffinity = 4.0 #eV
      self.dieletricConstant = 16.0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 5.658 #Angstroms
      self.boltzmannTemp = 0.0259 #eV
      self.intrinsicCarrierConcentration = 2.4E13 #cm^-3
      self.conductionDensityOfStates = 1.04E19 #cm^-3
      self.valenceDensityOfStates = 6.0E18 #cm^-3
      self.intrinsicResistivity = 46 #Ohm-cm
      self.opticalPhononEnergy = 0.037 #eV
      self.electronDriftMobility = 3900 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 1900 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 1E5 #V cm^-1
      self.thermalConductivity = 0.6 #W cm^-1 K^-1
      self.thermalDiffusivity = 0.36 #cm^2 s^-1
      self.linearThermalExpansion = 5.8E-6 #degC^-1
      self.refractionIndex = 4.00
      self.augerRecombinationCoefficientN = 1E-30 #cm^6 s^-1
      self.augerRecombinationCoefficientP = 1E-30 #cm^6 s^-1
   

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