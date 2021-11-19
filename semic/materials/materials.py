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

from semic.constants.constants import *

CRYSTAL_ORIENTATION = ['Simple Cubic','Face-centered Cubic', #1
                       'Body-centered Cubic', 'Simple Tetragonal', #3
                       'Body-centered Tetragonal', 'Simple Orthorhombic', #5
                       'Base-centered Orthorhombic', 'Body-centered Orthorhombic', #7
                       'Face-centered Orthorhombic', 'Simple Monoclinic', #9
                       'Base-centered Monoclinic', 'Triclinic', 'Trigonal', #12
                       'Hexagonal', ''] #14

CRYSTAL_STRUCTURE = ['Diamond', 'Zincblende', 'Wurtzite', 'Rock-Salt', '', 'Hexagonal']

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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1   
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
      self.dielectricConstant = 11.7 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 5.43095 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 1E10 #cm^-3
      self.conductionDensityOfStates = 2.8E19 #cm^-3
      self.valenceDensityOfStates = 1.0E19 #cm^-3
      self.intrinsicResistivity = 2.3E5 #Ohm-cm
      self.opticalPhononEnergy = 0.063 #eV
      self.electronDriftMobility = 1500 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 475 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 3E5 #V cm^-1
      self.thermalConductivity = 148 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0.8 #cm^2 s^-1
      self.linearThermalExpansion = 2.6E-6 #degC^-1
      self.refractionIndex = 3.42
      self.augerRecombinationCoefficientN = 1.1E-30 #cm^6 s^-1
      self.augerRecombinationCoefficientP = 3.0E-31 #cm^6 s^-1

   def tempDependence(self,temp):
      pass

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
      self.dielectricConstant = 16.0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 5.658 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 2.4E13 #cm^-3
      self.conductionDensityOfStates = 1.04E19 #cm^-3
      self.valenceDensityOfStates = 6.0E18 #cm^-3
      self.intrinsicResistivity = 46 #Ohm-cm
      self.opticalPhononEnergy = 0.037 #eV
      self.electronDriftMobility = 3900 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 1900 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 1E5 #V cm^-1
      self.thermalConductivity = 0.6 #W cm^-1 degC^-1
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
   Material Properties and Object Parameters for Silicon Carbide [Polytypes:(3C,4H,6H)]
   '''
   group = GROUP[10] # IV-IV Semiconductor
   crystal_structure = {"3C":CRYSTAL_STRUCTURE[1],"4H":CRYSTAL_STRUCTURE[2],"6H":CRYSTAL_STRUCTURE[2]} #Zincblende,Wurtzite,Wurtzite
   crystal_orientation = {"3C":CRYSTAL_ORIENTATION[1],"4H":CRYSTAL_ORIENTATION[13],"6H":CRYSTAL_ORIENTATION[13]} #Cubic, Hexagonal, Hexagonal

   def __init__(self):
      '''
      Silicon Carbide material properties at 300 Kelvin for 3C,4H,6H
      '''
      self.abstemp = 300 #Kelvin
      self.density = {"3C":3.21,"4H":3.211,"6H":3.211} #g cm^-3
      self.bandGap = {"3C":2.36,"4H":3.23,"6H":3.00} #eV
      self.gapType = {"3C":"Indirect","4H":"Indirect","6H":"Indirect"}
      self.debyeTemp = {"3C":1200,"4H":1300,"6H":1200} #Kelvin
      self.intrinsicDebyeLength = "unknown" #microns
      self.electronAffinity = "unknown" #eV
      self.dielectricConstant = {"3C":{"static":9.72,"high frequency":6.52},
                                 "4H":{"static":{"\u2225 to c axis":10.03,"\u27c2 to c axis":9.66},
                                       "high frquency":{"\u2225 to c axis":6.70,"\u27c2 to c axis":6.52}},
                                 "6H":{"static":{"\u2225 to c axis":10.03,"\u27c2 to c axis":9.66},
                                       "high frquency":{"\u2225 to c axis":6.70,"\u27c2 to c axis":6.52}}} #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = {"3C":4.3596,"4H":{"a":3.0730,"c":10.053},"6H":{"a":3.0806,"c":15.1173}} #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = {"3C":"","4H":"","6H":""} #cm^-3
      self.conductionDensityOfStates = {"3C":1.5e19,"4H":1.7e19,"6H":8.9e19} #cm^-3
      self.valenceDensityOfStates = {"3C":1.2e19,"4H":2.5e19,"6H":2.5e19} #cm^-3
      self.intrinsicResistivity = "unknown" #Ohm-cm
      self.opticalPhononEnergy = {"3C":102.8,"4H":104.2,"6H":104.2} #eV
      self.electronDriftMobility = {"3C":800,"4H":900,"6H":400} #cm^2 V^-1 s^-1
      self.holeDriftMobility = {"3C":320,"4H":120,"6H":90} #cm^2 V^-1 s^-1
      self.approxBreakdownField = {"3C":1e6,"4H":{"min":3e6,"max":5e6},"6H":{"min":3e6,"max":5e6}} #V cm^-1
      self.thermalConductivity = {"3C":3.6,"4H":3.7,"6H":4.9} #W cm^-1 degC^-1
      self.thermalDiffusivity = {"3C":1.6,"4H":1.7,"6H":2.2} #cm^2 s^-1
      self.linearThermalExpansion = {"3C":3.8e-6,"4H":"unknown",
                                     "6H":{"\u2225 to c axis":4.7e-6,"\u27c2 to c axis":4.3e-6}} #degC^-1
      self.refractionIndex = {"3C":2.55,"4H":{"\u2225 to c axis":2.59,"\u27c2 to c axis":2.55},
                              "6H":{"\u2225 to c axis":2.59,"\u27c2 to c axis":2.55}}
      self.augerRecombinationCoefficientN = "unknown" #cm^6 s^-1
      self.augerRecombinationCoefficientP = "unknown" #cm^6 s^-1
'''
III-V -> GROUP[9]
'''
class AlN:
   '''
   Material Properties and Object Parameters for a Aluminum Nitride (Hexagonal Polytype)
   '''

   group = GROUP[9] #III-V
   crystal_structure = CRYSTAL_STRUCTURE[2] #Wurtzite
   crystal_orientation = CRYSTAL_ORIENTATION[13] #Hexagonal

   def __init__(self):
      '''
      Aluminum Nitride material properties at 300K
      '''
      self.abstemp = 300 #Kelvin
      self.density = 3.23 #g cm^-3
      self.bandGap = 6.2 #eV
      self.gapType = 'Direct' #Direct/Indirect
      self.debyeTemp = 1150 #Kelvin
      self.intrinsicDebyeLength = "TBD" #microns
      self.electronAffinity = 0.6 #eV
      self.dielectricConstant = {"static":8.5,"high frequency":4.6} #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = {"a":3.112,"c":4.982} #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 4.598e-33 #cm^-3
      self.conductionDensityOfStates = 6.3e18 #cm^-3
      self.valenceDensityOfStates = 4.8e20 #cm^-3
      self.intrinsicResistivity = 4.525e48 #Ohm-cm
      self.opticalPhononEnergy = 0.099 #eV
      self.electronDriftMobility = 300 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 14 #cm^2 V^-1 s^-1
      self.approxBreakdownField = {"min":1.2e6,"max":1.8e6} #V cm^-1
      self.thermalConductivity = 2.85 #W cm^-1 degC^-1
      self.thermalDiffusivity = 1.47 #cm^2 s^-1
      self.linearThermalExpansion = {"\u03b1\u2090":4.2e-6,"\u03b1_c":5.3e-6} #degC^-1
      self.refractionIndex = 2.15
      self.augerRecombinationCoefficientN = "unknown" #cm^6 s^-1
      self.augerRecombinationCoefficientP = "unknown" #cm^6 s^-1

class AlP:
   '''
   Material Properties and Object Parameters for a Custom Semiconductor
   '''

   group = GROUP[9] #III-V
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
      self.refractionIndex = 0
      self.augerRecombinationCoefficientN = 0 #cm^6 s^-1
      self.augerRecombinationCoefficientP = 0 #cm^6 s^-1

class AlAs:
   '''
   Material Properties and Object Parameters for a Custom Semiconductor
   '''

   group = GROUP[9] #III-V
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
      self.refractionIndex = 0
      self.augerRecombinationCoefficientN = 0 #cm^6 s^-1
      self.augerRecombinationCoefficientP = 0 #cm^6 s^-1

class AlSb:
   '''
   Material Properties and Object Parameters for a Custom Semiconductor
   '''

   group = GROUP[9] #III-V
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
      self.refractionIndex = 0
      self.augerRecombinationCoefficientN = 0 #cm^6 s^-1
      self.augerRecombinationCoefficientP = 0 #cm^6 s^-1

class BN:
   '''
   Material Properties and Object Parameters for Boron Nitride
   '''

   group = GROUP[9] #III-V
   crystal_structure = [CRYSTAL_STRUCTURE[2],CRYSTAL_STRUCTURE[1],CRYSTAL_STRUCTURE[5]] #Empty
   crystal_orientation = {"Wurtzite":CRYSTAL_ORIENTATION[13],"Zincblende":CRYSTAL_ORIENTATION[1],"Hexagonal":CRYSTAL_ORIENTATION[13]} #Empty

   def __init__(self):
      '''
      Boron Nitride semiconductor material properties
      '''
      self.abstemp = 300 #Kelvin
      self.density = {"Wurtzite":3.48,"Zincblende":3.450,"Hexagonal":{"min":2.0,"max":2.28}} #g cm^-3
      self.bandGap = {"Wurtzite":{"min":4.5,"max":5.5},
                      "Zincblende":{"min":6.1,"max":6.4},
                      "Hexagonal":{"min":4.0,"max":5.8}} #eV
      self.gapType = {"Wurtzite":"Quasi-direct","Zincblende":"Indirect","Hexagonal":"Indirect"} #Direct/Indirect
      self.debyeTemp = {"Wurtzite": 1400,"Zincblende":1700,"Hexagonal":400} #Kelvin
      self.intrinsicDebyeLength = {"Wurtzite":"unknown","Zincblende":"unknown","Hexagonal":"Unknown"} #microns
      self.electronAffinity = "unknown" #eV
      self.dielectricConstant = {"Wurtzite":{"static":{"\u2225":5.1,"\u27c2":6.8},"high frequency":{"min":4.2,"max":4.5}},
                                 "Zincblende":{"static":7.1,"high frequency":4.86},
                                 "Hexagonal":{"static":{"\u2225":5.06,"\u27c2":6.85},"high frequency":{"\u2225":2.2,"\u27c2":4.3}}} #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = {"Wurtzite":{"a":2.55,"c":4.17},"Zincblende":3.615,
                              "Hexagonal":{"a":{"min":2.5,"max":2.9},"c":6.66}} #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = {"Wurtzite":{"min":3.142e-19,"max":1.252e-27},
                                            "Zincblende":{"min":1.352e-32,"max":4.083e-35},
                                            "Hexagonal":"unknown"} #cm^-3
      self.conductionDensityOfStates = {"Wurtzite":1.5e19,"Zincblende":2.1e19,"Hexagonal":"unknown"} #cm^-3
      self.valenceDensityOfStates = {"Wurtzite":2.6e19,"Zincblende":2.6e19,"Hexagonal":"unknown"} #cm^-3
      self.intrinsicResistivity = "unknown" #Ohm-cm
      self.opticalPhononEnergy = {"Wurtzite":0.13,"Zincblende":0.13,"Hexagonal":"unknown"} #eV
      self.electronDriftMobility = {"Wurtzite":"unknown","Zincblende":200,"Hexagonal":"unknown"} #cm^2 V^-1 s^-1
      self.holeDriftMobility = {"Wurtzite":"unknown","Zincblende":500,"Hexagonal":"unknown"} #cm^2 V^-1 s^-1
      self.approxBreakdownField = {"Wurtzite":"unknown","Zincblende":{"min":2e6,"max":6e6},
                                   "Hexagonal":{"min":1e6,"max":3e6}} #V cm^-1
      self.thermalConductivity = {"Wurtzite":"unknown","Zincblende":7.4,"Hexagonal":"unknown"} #W cm^-1 degC^-1
      self.thermalDiffusivity = "unknown" #cm^2 s^-1
      self.linearThermalExpansion = {"Wurtzite":{"\u2225 to c axis":2.7e-6,"\u27c2 to c axis":2.3e-6},
                                     "Zincblende":1.2e-6,
                                     "Hexagonal":{"\u2225 to c axis":38e-6,"\u27c2 to c axis":-2.7e-6}} #degC^-1
      self.refractionIndex = {"Wurtzite":2.05,"Zincblende":2.1,"Hexagonal":1.8}
      self.augerRecombinationCoefficientN = "unknown" #cm^6 s^-1
      self.augerRecombinationCoefficientP = "unknown" #cm^6 s^-1

class GaN:
   '''
   Material Properties and Object Parameters for Gallium Nitride
   '''

   group = GROUP[9] #III-V
   crystal_structure = [CRYSTAL_STRUCTURE[2],CRYSTAL_STRUCTURE[1]] #Wurtzite and Zincblende
   crystal_orientation = {"Wurtzite":CRYSTAL_ORIENTATION[13],"Zincblende":CRYSTAL_ORIENTATION[1]} #Hexagonal and Face-centered Cubic

   def __init__(self):
      '''
      GaN semiconductor material properties at 300K
      '''
      self.abstemp = 300 #Kelvin
      self.density = 6.15 #g cm^-3
      self.bandGap = {"Wurtzite":3.39,"Zincblende":3.2} #eV
      self.gapType = 'Direct' #Direct/Indirect
      self.debyeTemp = 600 #Kelvin
      self.intrinsicDebyeLength = "unknown" #microns
      self.electronAffinity = 4.1 #eV
      self.dielectricConstant = {"Wurtzite":{"static":8.9,"high frequency":5.35},
                                "Zincblende":{"static":9.7,"high frequency":5.3}} #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = {"Wurtzite":{"a":3.189,"c":5.186},"Zincblende":4.52} #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = {"Wurtzite":3.847e-10,"Zincblende":1.045e-08} #cm^-3
      self.conductionDensityOfStates = {"Wurtzite":2.3e18,"Zincblende":1.2e18} #cm^-3
      self.valenceDensityOfStates = {"Wurtzite":4.6e19,"Zincblende":4.1e19} #cm^-3
      self.intrinsicResistivity = {"Wurtzite":1.622e25,"Zincblende":5.973e23} #Ohm-cm
      self.opticalPhononEnergy = {"Wurtzite":0.0912,"Zincblende":0.0873} #eV
      self.electronDriftMobility = 1000 #cm^2 V^-1 s^-1
      self.holeDriftMobility = {"Wurtzite":200,"Zincblende":350} #cm^2 V^-1 s^-1
      self.approxBreakdownField = 5e6 #V cm^-1
      self.thermalConductivity = 1.3 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0.43 #cm^2 s^-1
      self.linearThermalExpansion = {"\u03b1\u2090":5.59e-6,"\u03b1_c":3.17e-6} #degC^-1
      self.refractionIndex = 2.3 #infrared
      self.augerRecombinationCoefficientN = "unknown" #cm^6 s^-1
      self.augerRecombinationCoefficientP = "unknown" #cm^6 s^-1

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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
      self.refractionIndex = 0
      self.augerRecombinationCoefficientN = 0 #cm^6 s^-1
      self.augerRecombinationCoefficientP = 0 #cm^6 s^-1

class InN:
   '''
   Material Properties and Object Parameters for Indium Nitride (hexagonal polytype)
   '''

   group = GROUP[9] #III-V
   crystal_structure = CRYSTAL_STRUCTURE[2] #Wurtzite
   crystal_orientation = CRYSTAL_ORIENTATION[13] #Hexagonal

   def __init__(self):
      '''
      Indium Nitride material properties at 300K 
      '''
      self.abstemp = 300 #Kelvin
      self.density = 6.81 #g cm^-3
      self.bandGap = {"min":1.9,"max":2.05} #eV
      self.gapType = 'Direct' #Direct/Indirect
      self.debyeTemp = 660 #Kelvin
      self.intrinsicDebyeLength = "unknown" #microns
      self.electronAffinity = "unknown" #eV
      self.dielectricConstant = {"static":15.3,"high frequency":8.4} #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = {"a":3.533,"c":5.693} #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 9e17 #cm^-3
      self.valenceDensityOfStates = 5.3e19 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0.073 #eV
      self.electronDriftMobility = 3200 #cm^2 V^-1 s^-1
      self.holeDriftMobility = "unknown" #cm^2 V^-1 s^-1
      self.approxBreakdownField = "unknown" #V cm^-1
      self.thermalConductivity = 0.45 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0.2 #cm^2 s^-1
      self.linearThermalExpansion = {"\u03b1\u2090":3.8e-6,"\u03b1_c":2.9e-6} #degC^-1
      self.refractionIndex = 2.9
      self.augerRecombinationCoefficientN = "unknown" #cm^6 s^-1
      self.augerRecombinationCoefficientP = "unknown" #cm^6 s^-1

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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
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
      self.dielectricConstant = 0 #Epsilon_R a.k.a K (Kappa)
      self.latticeConstant = 0 #Angstroms
      self.boltzmannTemp = value("Boltzmann constant in eV/K") * self.abstemp #eV
      self.intrinsicCarrierConcentration = 0 #cm^-3
      self.conductionDensityOfStates = 0 #cm^-3
      self.valenceDensityOfStates = 0 #cm^-3
      self.intrinsicResistivity = 0 #Ohm-cm
      self.opticalPhononEnergy = 0 #eV
      self.electronDriftMobility = 0 #cm^2 V^-1 s^-1
      self.holeDriftMobility = 0 #cm^2 V^-1 s^-1
      self.approxBreakdownField = 0 #V cm^-1
      self.thermalConductivity = 0 #W cm^-1 degC^-1
      self.thermalDiffusivity = 0 #cm^2 s^-1
      self.linearThermalExpansion = 0 #degC^-1
      self.refractionIndex = 0
      self.augerRecombinationCoefficientN = 0 #cm^6 s^-1
      self.augerRecombinationCoefficientP = 0 #cm^6 s^-1
'''
END ALLOY SEMICONDUCTORS
'''