"""JFET Class Module"""
import numpy as np
from semic.constants.constants import value

CHARGE = value('Elementary charge')
BOLTZMANN = value('Boltzmann constant in eV/K')

class JFET:
    """JFET Class
    """
    def __init__(self,
                 temp: float=0.0,
                 af: float=1.0,
                 alpha: float=0.0,
                 beta: float=1.0e-4,
                 betatce: float=0.0,
                 cgd: float=0.0,
                 cgs: float=0.0,
                 fc: float=0.5,
                 i_s: float=1.0e-14,
                 isr: float=0.0,
                 kf: float=0.0,
                 lamda: float=0.0,
                 m: float=0.5,
                 n: float=1.0,
                 nr: float=2.0,
                 pb: float=1.0,
                 rd: float=0.0,
                 rs: float=0.0,
                 vk: float=0.0,
                 vto: float=-2.0,
                 vtotc: float=0.0,
                 xti: float=3.0)-> None:
        """_summary_

        Parameters
        ----------
        temp : float, optional
            _description_, by default 0.0
        af : float, optional
            _description_, by default 1.0
        alpha : float, optional
            _description_, by default 0.0
        beta : float, optional
            _description_, by default 1.0e-4
        betatce : float, optional
            _description_, by default 0.0
        cgd : float, optional
            _description_, by default 0.0
        cgs : float, optional
            _description_, by default 0.0
        fc : float, optional
            _description_, by default 0.5
        i_s : float, optional
            _description_, by default 1.0e-14
        isr : float, optional
            _description_, by default 0.0
        kf : float, optional
            _description_, by default 0.0
        lamda : float, optional
            _description_, by default 0.0
        m : float, optional
            _description_, by default 0.5
        n : float, optional
            _description_, by default 1.0
        nr : float, optional
            _description_, by default 2.0
        pb : float, optional
            _description_, by default 1.0
        rd : float, optional
            _description_, by default 0.0
        rs : float, optional
            _description_, by default 0.0
        vk : float, optional
            _description_, by default 0.0
        vto : float, optional
            _description_, by default -2.0
        vtotc : float, optional
            _description_, by default 0.0
        xti : float, optional
            _description_, by default 3.0
        """
        self.temperature = temp
        self.flicker_noise_exp = af
        self.ionization_coeff = alpha
        self.transconductance_coeff = beta
        self.beta_exp_temp_coeff = betatce
        self.zero_bias_gate_drain_pn_cap = cgd
        self.zero_bias_gate_source_pn_cap = cgs
        self.fwd_bias_depl_cap_coeff = fc
        self.gate_pn_sat_current = i_s
        self.gate_pn_rec_current_param = isr
        self.flicker_noise_coeff = kf
        self.ch_len_modulation = lamda
        self.gate_pn_grading_coeff = m
        self.gate_pn_emission_coeff = n
        self.emission_coeff_isr = nr
        self.gate_pn_potential = pb
        self.drain_ohmic_resist = rd
        self.source_ohmic_resist = rs
        self.ionization_knee_voltage = vk
        self.threshold_voltage = vto
        self.vto_temp_coeff = vtotc
        self.sat_current_temp_coeff = xti
    
    def gate_current(self,
                     area: float=0.0,
                     vgs: float=0.0,
                     vgd: float=0.0)-> float:
        """_summary_

        Parameters
        ----------
        area : float, optional
            _description_, by default 0.0
        vgs : float, optional
            _description_, by default 0.0
        vgd : float, optional
            _description_, by default 0.0

        Returns
        -------
        float
            _description_
        """
        return area * (self.__gate_source_leakage_current(vgs) + self.__gate_drain_leakage_current(vgd))

    def __gate_source_leakage_current(self,
                                      vgs: float=0.0)-> float:
        """_summary_

        Parameters
        ----------
        vgs : float, optional
            _description_, by default 0.0

        Returns
        -------
        float
            _description_
        """
        return self.__normal_current(vgs) + (self.__recombination_current(vgs) * self.__generation_factor(vgs))
    
    def __gate_drain_leakage_current(self,
                                     vgd: float=0.0,
                                     vgs: float=0.0,
                                     vds: float=0.0)-> float:
        """_summary_

        Parameters
        ----------
        vgd : float, optional
            _description_, by default 0.0

        Returns
        -------
        float
            _description_
        """
        ii = self.__impact_ionization_current(vgs,vds)
        return self.__normal_current(vgd) + (self.__recombination_current(vgd) * self.__generation_factor(vgd)) + ii

    def __normal_current(self,
                         voltage: float=0.0)-> float:
        """_summary_

        Returns
        -------
        float
            _description_
        """
        vt = BOLTZMANN * self.temperature / CHARGE

        i_n = self.gate_pn_sat_current * (np.exp(voltage / (self.gate_pn_emission_coeff * vt) - 1))
        return i_n

    def __recombination_current(self,
                                voltage: float=0.0)-> float:
        """_summary_

        Parameters
        ----------
        voltage : float, optional
            _description_, by default 0.0

        Returns
        -------
        float
            _description_
        """
        vt = BOLTZMANN * self.temperature / CHARGE

        ir = self.gate_pn_rec_current_param * (np.exp(voltage / (self.emission_coeff_isr * vt)) - 1)
        return ir

    def __generation_factor(self,
                            voltage: float=0.0)-> float:
        """_summary_

        Parameters
        ----------
        voltage : float, optional
            _description_, by default 0.0

        Returns
        -------
        float
            _description_
        """
        return (((1 - (voltage / self.gate_pn_potential)) ** 2) + 0.005) ** (self.gate_pn_grading_coeff / 2)
    
    def __impact_ionization_current(self,
                                    vgs: float=0.0,
                                    vds: float=0.0)-> float:
        """_summary_

        Parameters
        ----------
        vgs : float, optional
            _description_, by default 0.0
        vds : float, optional
            _description_, by default 0.0

        Returns
        -------
        float
            _description_
        """
        pass