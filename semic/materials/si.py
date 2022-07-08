"""
Created on Sun Jun  5 23:11:01 2022

@author: Nithin Kumar Santha Kumar

Description:
"""
from semic.constants.constants import value
from semic.materials.semiconductor import Semiconductor
import numpy as np

BOLTZMANN = value("Boltzmann constant in eV/K")

class Si(Semiconductor):
    """
    """
    def bandgap_temp_dependence(self,
                                temperature: float=None)-> float:
        """_summary_

        Parameters
        ----------
        temperature : float
            _description_, by default None

        Returns
        -------
        float
            _description_
        """
        eg_0 = 1.17
        temp = self.abstemp if temperature is None else temperature
        return eg_0 - ((4.73e-4 * temp ** 2) / (temp + 636))

    def intrinsic_carrier_concentration(self,
                                        temperature: float=None)-> float:
        """_summary_

        Parameters
        ----------
        temperature : float, optional
            _description_, by default None

        Returns
        -------
        float
            _description_
        """
        temp = self.abstemp if temperature is None else temperature
        eg = self.bandgap_temp_dependence(temp)
        two_kb_t = 2 * BOLTZMANN * temp
        nc = self.conduction_dos(temp)
        nv = self.valence_dos(temp)

        return np.sqrt(nc * nv) * np.exp(-eg / two_kb_t)

    def conduction_dos(self,
                       temperature: float=None)-> float:
        """_summary_

        Parameters
        ----------
        temperature : float, optional
            _description_, by default None

        Returns
        -------
        float
            _description_
        """
        temp = self.abstemp if temperature is None else temperature
        nc = 6.2e15 * temp ** (3/2) if self.conductionDensityOfStates is None else self.conductionDensityOfStates

        return nc
    
    def valence_dos(self,
                    temperature: float=None)-> float:
        """_summary_

        Parameters
        ----------
        temperature : float, optional
            _description_, by default None

        Returns
        -------
        float
            _description_
        """
        temp = self.abstemp if temperature is None else temperature
        nv = 3.5e15 * temp ** (3/2) if self.valenceDensityOfStates is None else self.valenceDensityOfStates

        return nv

    def bandgap_pressure_dependence(self,
                                    pressure: float=0.0)-> float:
        """Dependence of the Energy Gap on Hydrostatic Pressure

        Parameters
        ----------
        pressure : float, optional
            Hydrostatic Pressure, by default 0.0 kbar

        Returns
        -------
        float
            _description_
        """
        eg_0 = 1.17

        return eg_0 - (1.4e-3 * pressure)
    
    def infrared_refractive_index(self,
                                  temp: float=None)-> float:
        """
        Calculates the refractive index based on temperature. This equation only works
        on temperature ranges between 77K and 400K.

        Parameters
        ----------
        temp : float, optional
            temperature in Kelvin, by default None

        Returns
        -------
        float
            The refractive index

        Raises
        ------
        ValueError
            Temperature is outside of range specified
        """
        temp = self.abstemp if temp is None else temp

        if 77 < temp < 400:
            return 3.38 * (1 + (3.9e-5 * temp))
        else:
            raise ValueError("Temperature outside of specified range (77 < temp < 400)!")
        