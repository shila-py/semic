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

import operator

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
CREATE YOUR OWN SEMICONDUCTOR
"""
class Semiconductor:
    """
    Material Properties and Object Parameters for a Custom Semiconductor
    """
    def __init__(self,
                 group: str="IV",
                 structure: str="Diamond",
                 orientation: str="FCC",
                 temp: (float or int)=300,
                 density: (float or int)=None,
                 bandGap: (float or int)=None,
                 gapType: str=None,
                 debyeTemp: (float or int)=None,
                 debyeLength: (float or int)=None,
                 affinity: (float or int)=None,
                 dielectric: (float or list or dict)=11.8,
                 lattice: (float or list or dict)=5.43,
                 carrierConcentration: float=None,
                 densityOfStatesC: float=None,
                 densityOfStatesV: float=None,
                 resistivity: float=None,
                 phononEnergy: float=None,
                 driftMobE: float=None,
                 driftMobH: float=None,
                 breakdownField: float=None,
                 conductivityTh: float=None,
                 diffusivityTh: float=None,
                 expansionThLin: float=None,
                 refraction: float=None,
                 recombinationAugerN: float=None,
                 recombinationAugerP: float=None):
        """_summary_

        Parameters
        ----------
        group : str, optional
            _description_, by default "IV"
        structure : str, optional
            _description_, by default "Diamond"
        orientation : _type_, optional
            _description_, by default None
        temp : float, optional
            _description_, by default 300
        density : float, optional
            _description_, by default None
        bandGap : float, optional
            _description_, by default None
        gapType : str, optional
            _description_, by default None
        debyeTemp : float, optional
            _description_, by default None
        debyeLength : float, optional
            _description_, by default None
        affinity : float, optional
            _description_, by default None
        dielectric : float, optional
            _description_, by default None
        lattice : float, optional
            _description_, by default None
        carrierConcentration : float, optional
            _description_, by default None
        densityOfStatesC : float, optional
            _description_, by default None
        densityOfStatesV : float, optional
            _description_, by default None
        resistivity : float, optional
            _description_, by default None
        phononEnergy : float, optional
            _description_, by default None
        driftMobE : float, optional
            _description_, by default None
        driftMobH : float, optional
            _description_, by default None
        breakdownField : float, optional
            _description_, by default None
        conductivityTh : float, optional
            _description_, by default None
        diffusivityTh : float, optional
            _description_, by default None
        expansionThLin : float, optional
            _description_, by default None
        refraction : float, optional
            _description_, by default None
        recombinationAugerN : float, optional
            _description_, by default None
        recombinationAugerP : float, optional
            _description_, by default None
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

    group = property(operator.attrgetter('_group'))
    
    @property
    def group(self):
        return self._group

    @group.setter
    def group(self,s):
        if type(s) != str:
            raise Exception("group must be str type!")
        self._group = s
    
    crystalStructure = property(operator.attrgetter('_crystalStructure'))

    @property
    def crystalStructure(self):
        return self._crystalStructure

    @crystalStructure.setter
    def crystalStructure(self,s):
        if type(s) != str:
            raise Exception("crystalStructure must be str type!")
        self._crystalStructure = s
    
    crystalOrientation = property(operator.attrgetter('_crytalOrientation'))

    @property
    def crystalOrientation(self):
        return self._crystalOrientation
    
    @crystalOrientation.setter
    def crystalOrientation(self,s):
        if type(s) != str:
            raise Exception("crystalOrientation must be str type!")
        self._crystalOrientation = s

    abstemp = property(operator.attrgetter('_abstemp'))

    @property
    def abstemp(self):
        return self._abstemp
    
    @abstemp.setter
    def abstemp(self,temp):
        if type(temp) != (int or float):
            raise Exception("abstemp must be int or float types!")
        elif temp < 0:
            raise Exception("abstemp must be greater than or equal to 0!")
        self._abstemp = temp
    
    density = property(operator.attrgetter('_density'))

    @property
    def density(self):
        return self._density
    
    @density.setter
    def density(self,value):
        if type(value) != (int or float):
            raise Exception("density must be int or float types!")
        elif value <= 0:
            raise Exception("density must be non-zero and positive!")
        self._density = value
    
    bandGap = property(operator.attrgetter('_bandGap'))

    @property
    def bandGap(self):
        return self._bandGap
    
    @bandGap.setter
    def bandGap(self,value):
        if type(value) != (int or float):
            raise Exception("bandGap must be int or float")
        if value < 0:
            raise Exception("bandGap must be greater than or equal to 0!")
        self._bandGap = value

    gapType = property(operator.attrgetter('_gapType'))

    @property
    def gapType(self):
        return self._gapType
    
    @gapType.setter
    def gapType(self,s):
        if type(s) != str:
            raise Exception("x must be str type")
        self._gapType = s
    
    debyeTemp = property(operator.attrgetter('_debyeTemp'))

    @property
    def debyeTemp(self):
        return self._debyeTemp
    
    @debyeTemp.setter
    def debyeTemp(self,value):
        if type(value) != (int or float):
            raise Exception("debyeTemp must be int or float")
        if value < 0:
            raise Exception("debyeTemp must be greater than or equal to 0!")
        self._debyeTemp = value
    
    intrinsicDebyeLength = property(operator.attrgetter('_intrinsicDebyeLength'))

    @property
    def intrinsicDebyeLength(self):
        return self._intrinsicDebyeLength
    
    @intrinsicDebyeLength.setter
    def intrinsicDebyeLength(self,value):
        if type(value) != (int or float):
            raise Exception("intrinsicDebyeLength must be int or float")
        if value < 0:
            raise Exception("intrinsicDebyeLength must be greater than or equal to 0!")
        self._intrinsicDebyeLength = value
    
    electronAffinity = property(operator.attrgetter('_electronAffinity'))

    @property
    def electronAffinity(self):
        return self._electronAffinity
    
    @electronAffinity.setter
    def electronAffinity(self,value):
        if type(value) != (int or float):
            raise Exception("electronAffinity must be int or float")
        if value < 0:
            raise Exception("electronAffinity must be greater than or equal to 0!")
        self._electronAffinity = value
    
    dielectricConstant = property(operator.attrgetter('_dielectricConstant'))

    @property
    def dielectricConstant(self):
        return self._dielectricConstant
    
    @dielectricConstant.setter
    def dielectricConstant(self,value):
        if type(value) != (float or list or dict):
            raise Exception("dielectricConstant must be float or list or dict")
        if value < 0:
            raise Exception("dielectricConstant must be greater than or equal to 0!")
        self._dielectricConstant = value
    
    latticeConstant = property(operator.attrgetter('_latticeConstant'))

    @property
    def latticeConstant(self):
        return self._latticeConstant
    
    @latticeConstant.setter
    def latticeConstant(self,value):
        if type(value) != (float or list or dict):
            raise Exception("latticeConstant must be float or list or dict")
        if value <= 0:
            raise Exception("latticeConstant must be greater than 0!")
        self._latticeConstant = value
    
    intrinsicCarrierConcentration = property(operator.attrgetter('_intrinsicCarrierConcentration'))

    @property
    def intrinsicCarrierConcentration(self):
        return self._intrinsicCarrierConcentration
    
    @intrinsicCarrierConcentration.setter
    def intrinsicCarrierConcentration(self,value):
        if type(value) != float:
            raise Exception("intrinsicCarrierConcentration must be float")
        if value < 0:
            raise Exception("intrinsicCarrierConcentration must be greater than or equal to 0!")
        self._intrinsicCarrierConcentration = value
    
    conductionDensityOfStates = property(operator.attrgetter('_conductionDensityOfStates'))

    @property
    def conductionDensityOfStates(self):
        return self._conductionDensityOfStates
    
    @conductionDensityOfStates.setter
    def conductionDensityOfStates(self,value):
        if type(value) != float:
            raise Exception("conductionDensityOfStates must be float")
        if value < 0:
            raise Exception("conductionDensityOfStates must be greater than or equal to 0!")
        self._conductionDensityOfStates = value
    
    valenceDensityOfStates = property(operator.attrgetter('_valenceDensityOfStates'))

    @property
    def valenceDensityOfStates(self):
        return self._valenceDensityOfStates
    
    @valenceDensityOfStates.setter
    def valenceDensityOfStates(self,value):
        if type(value) != float:
            raise Exception("valenceDensityOfStates must be float")
        if value < 0:
            raise Exception("valenceDensityOfStates must be greater than or equal to 0!")
        self._valenceDensityOfStates = value
    
    intrinsicResistivity = property(operator.attrgetter('_intrinsicResistivity'))

    @property
    def intrinsicResistivity(self):
        return self._intrinsicResistivity
    
    @intrinsicResistivity.setter
    def intrinsicResistivity(self,value):
        if type(value) != float:
            raise Exception("intrinsicResistivity must be float")
        if value < 0:
            raise Exception("intrinsicResistivity must be greater than or equal to 0!")
        self._intrinsicResistivity = value
    
    opticalPhononEnergy = property(operator.attrgetter('_opticalPhononEnergy'))

    @property
    def opticalPhononEnergy(self):
        return self._opticalPhononEnergy
    
    @opticalPhononEnergy.setter
    def opticalPhononEnergy(self,value):
        if type(value) != float:
            raise Exception("opticalPhononEnergy must be float")
        if value < 0:
            raise Exception("opticalPhononEnergy must be greater than or equal to 0!")
        self._opticalPhononEnergy = value
    
    electronDriftMobility = property(operator.attrgetter('_electronDriftMobility'))

    @property
    def electronDriftMobility(self):
        return self._electronDriftMobility
    
    @electronDriftMobility.setter
    def electronDriftMobility(self,value):
        if type(value) != float:
            raise Exception("electronDriftMobility must be float")
        if value < 0:
            raise Exception("electronDriftMobility must be greater than or equal to 0!")
        self._electronDriftMobility = value
    
    holeDriftMobility = property(operator.attrgetter('_holeDriftMobility'))

    @property
    def holeDriftMobility(self):
        return self._holeDriftMobility
    
    @holeDriftMobility.setter
    def holeDriftMobility(self,value):
        if type(value) != float:
            raise Exception("holeDriftMobility must be float")
        if value < 0:
            raise Exception("holeDriftMobility must be greater than or equal to 0!")
        self._holeDriftMobility = value
    
    approxBreakdownField = property(operator.attrgetter('_approxBreakdownField'))

    @property
    def approxBreakdownField(self):
        return self._approxBreakdownField
    
    @approxBreakdownField.setter
    def approxBreakdownField(self,value):
        if type(value) != float:
            raise Exception("approxBreakdownField must be float")
        if value < 0:
            raise Exception("approxBreakdownField must be greater than or equal to 0!")
        self._approxBreakdownField = value
    
    thermalConductivity = property(operator.attrgetter('_thermalConductivity'))

    @property
    def thermalConductivity(self):
        return self._thermalConductivity
    
    @thermalConductivity.setter
    def thermalConductivity(self,value):
        if type(value) != float:
            raise Exception("thermalConductivity must be float")
        if value < 0:
            raise Exception("thermalConductivity must be greater than or equal to 0!")
        self._thermalConductivity = value
    
    thermalDiffusivity = property(operator.attrgetter('_thermalDiffusivity'))

    @property
    def thermalDiffusivity(self):
        return self._thermalDiffusivity
    
    @thermalDiffusivity.setter
    def thermalDiffusivity(self,value):
        if type(value) != float:
            raise Exception("thermalDiffusivity must be float")
        if value < 0:
            raise Exception("thermalDiffusivity must be greater than or equal to 0!")
        self._thermalDiffusivity = value

    linearThermalExpansion = property(operator.attrgetter('_linearThermalExpansion'))

    @property
    def linearThermalExpansion(self):
        return self._linearThermalExpansion
    
    @linearThermalExpansion.setter
    def linearThermalExpansion(self,value):
        if type(value) != float:
            raise Exception("linearThermalExpansion must be float")
        if value < 0:
            raise Exception("linearThermalExpansion must be greater than or equal to 0!")
        self._linearThermalExpansion = value
    
    refractionIndex = property(operator.attrgetter('_refractionIndex'))

    @property
    def refractionIndex(self):
        return self._refractionIndex
    
    @refractionIndex.setter
    def refractionIndex(self,value):
        if type(value) != float:
            raise Exception("refractionIndex must be float")
        if value < 0:
            raise Exception("refractionIndex must be greater than or equal to 0!")
        self._refractionIndex = value
    
    augerRecombinationCoefficientN = property(operator.attrgetter('_augerRecombinationCoefficientN'))

    @property
    def augerRecombinationCoefficientN(self):
        return self._augerRecombinationCoefficientN
    
    @augerRecombinationCoefficientN.setter
    def augerRecombinationCoefficientN(self,value):
        if type(value) != float:
            raise Exception("augerRecombinationCoefficientN must be float")
        if value < 0:
            raise Exception("augerRecombinationCoefficientN must be greater than or equal to 0!")
        self._augerRecombinationCoefficientN = value
    
    augerRecombinationCoefficientP = property(operator.attrgetter('_augerRecombinationCoefficientP'))

    @property
    def augerRecombinationCoefficientP(self):
        return self._augerRecombinationCoefficientP
    
    @augerRecombinationCoefficientP.setter
    def augerRecombinationCoefficientP(self,value):
        if type(value) != float:
            raise Exception("augerRecombinationCoefficientP must be float")
        if value < 0:
            raise Exception("augerRecombinationCoefficientP must be greater than or equal to 0!")
        self._augerRecombinationCoefficientP = value

