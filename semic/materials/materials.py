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

CRYSTAL_ORIENTATION = ['Simple Cubic','Face-centered Cubic', #1
                       'Body-centered Cubic', 'Simple Tetragonal', #3
                       'Body-centered Tetragonal', 'Simple Orthorhombic', #5
                       'Base-centered Orthorhombic', 'Body-centered Orthorhombic', #7
                       'Face-centered Orthorhombic', 'Simple Monoclinic', #9
                       'Base-centered Monoclinic', 'Triclinic', 'Trigonal', #12
                       'Hexagonal', ''] #14

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
      All properties are initialized to 0 or empty string. 
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
   '''
   Material Properties and Object Parameters for Silicon Carbide Polytypes (3C,4H,6H)
   Properties will be displayed as so: [3C value, 4H value, 6H value]

   '''
   group = GROUP[10] # IV-IV Semiconductor
   crystal_structure = [CRYSTAL_STRUCTURE[1],CRYSTAL_STRUCTURE[2],CRYSTAL_STRUCTURE[2]] #Zincblende,Wurtzite,Wurtzite
   crystal_orientation = [CRYSTAL_ORIENTATION[1],CRYSTAL_ORIENTATION[14],CRYSTAL_ORIENTATION[14]] #Cubic, Hexagonal, Hexagonal

   def __init__(self):
      '''
      Silicon Carbide material properties at 300 Kelvin for 3C,4H,6H
      '''
      self.abstemp = 300 #Kelvin
      self.density = [3.21,3.211,3.211] #g cm^-3
      self.bandGap = 0 #eV
      self.gapType = ''
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
      self.thermalConductivity = 0 #W cm^-1 K^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
      self.refractionIndex = 0
      self.augerRecombinationCoefficientN = 0 #cm^6 s^-1
      self.augerRecombinationCoefficientP = 0 #cm^6 s^-1
'''
III-V
'''
class AlN:
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

class AlP:
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

class AlAs:
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

class AlSb:
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

class BN:
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

class GaN:
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

class GaP:
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

class GaAs:
   #Crystal Structure : Zincblende
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

class GaSb:
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

class InN:
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

class InP:
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

class InAs:
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

class InSb:
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
II-VI
'''
class ZnO:
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

class ZnS:
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

class ZnSe:
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

class ZnTe:
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

class CdS:
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

class CdSe:
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

class CdTe:
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

class HgS:
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
IV-VI
'''
class PbS:
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

class PbSe:
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

class PbTe:
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
Ternary
'''
class AlGaAs:
   # x : 1-x : 1
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

class AlGaN:
   # x : 1-x : 1
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

class AlGaSb:
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

class CdMnTe:
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

class GaAsP:
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

class HgCdTe:
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

class InAlAs:
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

class InGaAs:
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

class InGaN:
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
Quaternary
'''
class AlGaAsSb:
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

class GaInAsP:
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
END ALLOY SEMICONDUCTORS
'''