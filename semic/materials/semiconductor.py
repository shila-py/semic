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

"""
CRYSTAL_ORIENTATION = ['Simple Cubic','Face-centered Cubic', #1
                       'Body-centered Cubic', 'Simple Tetragonal', #3
                       'Body-centered Tetragonal', 'Simple Orthorhombic', #5
                       'Base-centered Orthorhombic', 'Body-centered Orthorhombic', #7
                       'Face-centered Orthorhombic', 'Simple Monoclinic', #9
                       'Base-centered Monoclinic', 'Triclinic', 'Trigonal', #12
                       'Hexagonal', ''] #14

CRYSTAL_STRUCTURE = ['Diamond', 'Zincblende', 'Wurtzite',
                     'Rock-Salt', '', 'Hexagonal']

ALLOYS = ['Binary', 'Ternary', 'Quaternary', '']

GROUP = ['I','II','III','IV','V','VI','VII','VIII',
         'II-VI','III-V','IV-IV','IV-VI',ALLOYS, '']
"""
"""
CREATE YOUR OWN SEMICONDUCTOR
"""
class Semiconductor:
    """
    Material Properties and Object Parameters for a Custom Semiconductor
    """
    def __init__(self,group=None,structure=None,orientation=None,temp=None,
                 density=None,bandGap=None,gapType=None,debyeTemp=None,
                 debyeLength=None,affinity=None,dielectric=None,lattice=None,
                 carrierConcentration=None,densityOfStatesC=None,
                 densityOfStatesV=None,resistivity=None,phononEnergy=None,
                 driftMobE=None,driftMobH=None,breakdownField=None,
                 conductivityTh=None,diffusivityTh=None,expansionThLin=None,
                 refraction=None,recombinationAugerN=None,
                 recombinationAugerP=None):
        """

        Parameters
        ----------
        group : TYPE
            DESCRIPTION.
        structure : TYPE
            DESCRIPTION.
        orientation : TYPE
            DESCRIPTION.
        temp : TYPE
            DESCRIPTION.
        density : TYPE
            DESCRIPTION.
        bandGap : TYPE
            DESCRIPTION.
        gapType : TYPE
            DESCRIPTION.
        debyeTemp : TYPE
            DESCRIPTION.
        debyeLength : TYPE
            DESCRIPTION.
        affinity : TYPE
            DESCRIPTION.
        dielectric : TYPE
            DESCRIPTION.
        lattice : TYPE
            DESCRIPTION.
        carrierConcentration : TYPE
            DESCRIPTION.
        densityOfStatesC : TYPE
            DESCRIPTION.
        densityOfStatesV : TYPE
            DESCRIPTION.
        resistivity : TYPE
            DESCRIPTION.
        phononEnergy : TYPE
            DESCRIPTION.
        driftMobE : TYPE
            DESCRIPTION.
        driftMobH : TYPE
            DESCRIPTION.
        breakdownField : TYPE
            DESCRIPTION.
        conductivityTh : TYPE
            DESCRIPTION.
        diffusivityTh : TYPE
            DESCRIPTION.
        expansionThLin : TYPE
            DESCRIPTION.
        refraction : TYPE
            DESCRIPTION.
        recombinationAugerN : TYPE
            DESCRIPTION.
        recombinationAugerP : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.group = group #Group Number
        self.crystalStructure = structure #crystal structure
        self.crystalOrientation = orientation #crystal orientation
        self.abstemp = temp #Kelvin
        self.density = density #g cm^-3
        self.bandGap = bandGap #eV
        self.gapType = gapType #Direct/Indirect
        self.debyeTemp = debyeTemp #Kelvin
        self.intrinsicDebyeLength = debyeLength #microns
        self.electronAffinity = affinity #eV
        self.dielectricConstant = dielectric #Epsilon_R a.k.a K (Kappa)
        self.latticeConstant = lattice #Angstroms
        self.intrinsicCarrierConcentration = carrierConcentration #cm^-3
        self.conductionDensityOfStates = densityOfStatesC #cm^-3
        self.valenceDensityOfStates = densityOfStatesV #cm^-3
        self.intrinsicResistivity = resistivity #Ohm-cm
        self.opticalPhononEnergy = phononEnergy #eV
        self.electronDriftMobility = driftMobE #cm^2 V^-1 s^-1
        self.holeDriftMobility = driftMobH #cm^2 V^-1 s^-1
        self.approxBreakdownField = breakdownField #V cm^-1
        self.thermalConductivity = conductivityTh #W cm^-1 degC^-1
        self.thermalDiffusivity = diffusivityTh #cm^2 s^-1
        self.linearThermalExpansion = expansionThLin #degC^-1
        self.refractionIndex = refraction
        self.augerRecombinationCoefficientN = recombinationAugerN #cm^6 s^-1
        self.augerRecombinationCoefficientP = recombinationAugerP #cm^6 s^-1
