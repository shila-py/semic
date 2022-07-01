"""
Module docstring
"""
import numpy as np
from scipy.misc import derivative
from semic.constants.constants import value

BOLTZMANN = value('Boltzmann constant in J/K')
CHARGE = value('Elementary charge')

class Diode:
    """Diode class description"""
    def __init__(self,
                 area: float=1.0,
                 temp: float=300.15,
                 i_s: float=1.0e-14,
                 isr: float=0.0,
                 r_s: float=0.0,
                 n: float=1.0,
                 nbv: float=1.0,
                 nbvl: float=1.0,
                 nr: float=2.0,
                 tt: float=0.0,
                 cj0: float=0.0,
                 pb: float=1.0,
                 m: float=0.5,
                 e_g: float=1.11,
                 xti: float=3.0,
                 k_f: float=0.0,
                 a_f: float=1.0,
                 fc: float=0.5,
                 bv: float=np.inf,
                 ibv: float=1.0e-3,
                 ibvl: float=0.0,
                 ikf: float=np.inf,
                 gmin: float=1e-12)-> None:
        """Diode Model Parameters. Based on SPICE model.

        Parameters
        ----------
        area : float, required

        temp : float, optional
            Model temperature at which all input data has been measured, by default 300.15 K
        i_s : float, optional
            Saturation current, by default 1.0e-14 A
        isr : float, optional
            Recombination current parameter, by default 0.0 A
        r_s : float, optional
            Ohmic or series resistance, by default 0.0 Ohms
        n : float, optional
            Emission coefficient, by default 1.0
        nbv : float, optional
            Reverse breakdown ideality factor, by default 1.0
        nbvl : float, optional
            Low-level reverse breakdown ideality factor, by default 1.0
        nr : float, optional
            Emission coefficient for isr, by default 2.0
        tt : float, optional
            Transit Time, by default 0.0 s
        cj0 : float, optional
            Zero-bias junction capacitance, by default 0.0 F
        pb : float, optional
            Junction potential, by default 1.0 V
        m : float, optional
            Grading coefficient, by default 0.5
        e_g : float, optional
            Energy gap, by default 1.11 eV
                        1.11 for Si
                        0.69 for Schottky Barrier Diode (SBD)
                        0.67 for Ge 
        xti : float, optional
            Saturation current temperature exponent, by default 3.0
                                                     3.0 for pn-junction diode
                                                     2.0 for SBD
        k_f : float, optional
            Flicker-noise coefficient, by default 0.0
        a_f : float, optional
            Flicker-noise exponent, by default 1.0
        fc : float, optional
            Forward capacitance, by default 0.5 F
        bv : float, optional
            Reverse breakdown voltage (positive voltage), by default np.inf V
        ibv : float, optional
            Reverse breakdown current (positive voltage), by default 1.0e-3 A
        ibvl : float, optional
            Low-level reverse breakdown knee current, by default 0.0
        ikf : float, optional
            High-injection knee current, by default np.inf
        gmin : float, optional
            Minimal conductance, by default 1.0e-12 S
        """
        self.area = area
        self.temperature = temp
        self.sat_current = i_s
        self.recombination_current_param = isr
        self.ohmic_resistance = r_s
        self.emission_coeff = n
        self.rev_breakdown_IF = nbv
        self.low_level_rev_breakdown_IF = nbvl
        self.isr_emission_coeff = nr
        self.transit_time = tt
        self.zero_bias_junction_cap = cj0
        self.junction_pot = pb
        self.grading_coeff = m
        self.energy_gap = e_g
        self.sat_current_temp_exp = xti
        self.flicker_noise_coeff = k_f
        self.flicker_noise_exp = a_f
        self.forward_capacitance = fc
        self.rev_breakdown_voltage = bv
        self.rev_breakdown_current = ibv
        self.low_level_rev_breakdown_knee_current = ibvl
        self.knee_current = ikf
        self.set_gmin(gmin)
    
    def set_gmin(self,
                 value: float=1.0e-12)-> None:
        """Set GMIN value

        Parameters
        ----------
        value : float, optional
            GMIN value, by default 1.0e-12 S
        """
        if value == 0:
            raise ValueError("GMIN value cannot be 0!")
        else:
            self.gmin = value
    
    def saturation_current(self,
                           tnom: float=300)-> float:
        """_summary_

        Parameters
        ----------
        temp : float, optional
            _description_, by default 300
        tnom : float, optional
            _description_, by default 300

        Returns
        -------
        float
            _description_
        """
        vt = BOLTZMANN * self.temperature / CHARGE
        t_tnom = self.temperature / tnom
        return self.sat_current * np.exp((t_tnom - 1) * self.energy_gap / (self.emission_coeff * vt)) * (t_tnom**(self.sat_current_temp_exp/self.emission_coeff))

    def recombination_current_parameter(self,
                                        tnom: float=300)-> float:
        """_summary_

        Parameters
        ----------
        tnom : float, optional
            _description_, by default 300

        Returns
        -------
        float
            _description_
        """
        vt = BOLTZMANN * self.temperature / CHARGE
        t_tnom = self.temperature / tnom
        return self.recombination_current_param * np.exp((t_tnom - 1) * self.energy_gap / (self.isr_emission_coeff * vt)) * (t_tnom**(self.sat_current_temp_exp/self.isr_emission_coeff))

    def high_injection_knee_current(self,
                                    tnom: float=300,
                                    tikf: float=0.0)-> float:
        """_summary_

        Parameters
        ----------
        tnom : float, optional
            _description_, by default 300
        tikf : float, optional
            _description_, by default 0.0

        Returns
        -------
        float
            _description_
        """
        return self.knee_current * (1 + (tikf * (self.temperature - tnom)))

    def reverse_breakdown_voltage(self,
                                  tnom: float=300,
                                  tbv1: float=0.0,
                                  tbv2: float=0.0)-> float:
        """_summary_

        Parameters
        ----------
        tnom : float, optional
            _description_, by default 300
        tbv1 : float, optional
            _description_, by default 0.0
        tbv2 : float, optional
            _description_, by default 0.0

        Returns
        -------
        float
            _description_
        """
        t_tnom = self.temperature - tnom
        return self.rev_breakdown_voltage * (1 + (tbv1 * t_tnom) + (tbv2 * (t_tnom ** 2)))
    
    def parasitic_resistance(self,
                             tnom: float=300,
                             trs1: float=0.0,
                             trs2: float=0.0)-> float:
        """_summary_

        Parameters
        ----------
        tnom : float, optional
            _description_, by default 300
        trs1 : float, optional
            _description_, by default 0.0
        trs2 : float, optional
            _description_, by default 0.0

        Returns
        -------
        float
            _description_
        """
        t_tnom = self.temperature - tnom
        return self.ohmic_resistance * (1 + (trs1 * t_tnom) + (trs2 * (t_tnom ** 2)))
    
    def junction_potential(self,
                           tnom: float=300)-> float:
        """_summary_

        Parameters
        ----------
        tnom : float, optional
            _description_, by default 300

        Returns
        -------
        float
            _description_
        """
        t_tnom = self.temperature / tnom
        vt = BOLTZMANN * self.temperature / CHARGE
        return self.junction_pot * t_tnom - (3 * vt * np.log(t_tnom)) - (self.__eg(tnom)*t_tnom) + self.__eg(self.temperature)
    
    def junction_capacitance(self,
                             tnom: float=300)-> float:
        """_summary_

        Parameters
        ----------
        tnom : float, optional
            _description_, by default 300

        Returns
        -------
        float
            _description_
        """
        t_tnom = self.temperature - tnom
        return self.zero_bias_junction_cap * (1 + (self.grading_coeff * ((0.0004 * t_tnom) + (1 - (self.junction_potential(tnom) / self.junction_pot)))))

    def __eg(self,
             temp: float=0.0)-> float:
        """_summary_

        Parameters
        ----------
        temp : float, optional
            _description_, by default 0.0 K

        Returns
        -------
        float
            _description_
        """
        return 1.16 - ((7.02e-4 * (temp ** 2)) / (1108 + temp))

    def diode_current(self,
                      vd: float=0.0)-> float:
        i_d = self.area * (self.forward_current() - self.reverse_current())
        return i_d

    def forward_current(self,
                        vd: float=0.0)-> float:
        pass

    def reverse_current(self,
                        vd: float=0.0)-> float:
        pass
    
    def normal_current(self)-> float:
        pass

    def high_injection_factor(self)-> float:
        pass

    def recombination_current(self)-> float:
        pass

    def generation_factor(self)-> float:
        pass

    def diode_capacitance(self)-> float:
        pass

    def transit_time_capacitance(self)-> float:
        pass

    def dc_conductance(self)-> float:
        dqdv = derivative()
        pass

    def junction_capacitance(self)-> float:
        pass

    def parasitic_thermal_noise(self)-> float:
        """Parasitic resistance thermal noise per unit bandwidth. Bandwidth is assumed to be 1.0 Hz.

        Returns
        -------
        float
            Parasitic thermal noise mean-square value
        """
        return 4 * BOLTZMANN * self.temperature / (self.ohmic_resistance / self.area)

    def intrinsic_diode_noise(self,
                              vd: float=0.0,
                              freq: float=1.0)-> float:
        """Intrinsic diode shot and flicker noise per unit bandwidth. Bandwidth is assumed to be 1.0 Hz.

        Parameters
        ----------
        vd : float, optional
            Diode voltage, by default 0.0 V
        freq : float, optional
            Frequency, by default 1.0 Hz

        Returns
        -------
        float
            intrinsic diode noise mean-square value
        """
        return (2 * CHARGE * self.diode_current(vd)) + (self.flicker_noise_coeff * self.diode_current(vd) / freq)

