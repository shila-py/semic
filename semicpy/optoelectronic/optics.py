'''Module docstring for optics'''

from dataclasses import dataclass
from semicpy.constants.constants import value
import numpy as np

"""
Constants
"""
EPSILON_0 = value("Vacuum electric permittivity")
MU_0 = value("Vacuum magnetic permeability")
SPEED_OF_LIGHT = value("Speed of light in vacuum")
PLANCK = value("Planck constant in eV s")


@dataclass
class Light:
    velocity : float = 3.0e8
    frequency : float = 5.402e14
    wavelength : float = 555.0e-9
    polarization : str = None
    direction : str = "z"
    intensity : float = 1.0
    relative_permittivity : float = 1.0
    relative_permeability : float = 1.0
    vacuum : bool = True
    
    def phase_velocity(self) -> float:
        """_summary_

        Returns
        -------
        float
            _description_
        """
        if self.vacuum == True:
            return SPEED_OF_LIGHT
        else:
            return 1 / np.sqrt(self.relative_permittivity * self.relative_permeability * EPSILON_0 * MU_0)

    def refractive_index(self) -> float:
        """_summary_

        Returns
        -------
        float
            _description_
        """
        return np.sqrt(self.relative_permittivity)

    def cauchy_dispersion_relation(self,
                                   n_minus2: float=-2.04e-8,
                                   n_0: float=3.4189,
                                   n_2: float=8.15e-2,
                                   n_4: float=1.25e-2) -> float:
        """_summary_

        Parameters
        ----------
        n_minus2 : float, optional
            material-specific constant, by default -2.04e-8 eV^2
        n_0 : float, optional
            material-specific constant, by default 3.4189
        n_2 : float, optional
            material-specific constant, by default 8.15e-2 eV^-2
        n_4 : float, optional
            material-specific constant, by default 1.25e-2 eV^-4

        Returns
        -------
        float
            n, the refractive index.
        """
        nm2 = n_minus2 * (self.photon_energy() ** -2)
        n2 = n_2 * np.square(self.photon_energy())
        n4 = n_4 * (self.photon_energy() ** 4)

        return nm2 + n_0 + n2 + n4

    def photon_energy(self) -> float:
        """_summary_

        Returns
        -------
        float
            returns the energy of a photon in eV
        """
        return self.frequency * PLANCK

    def sellmeier_equation(self,
                           wavelength: float = None,
                           A1: float = 0.696749,
                           A2: float = 0.408218,
                           A3: float = 0.890815,
                           lambda1: float = 0.0690660e-6,
                           lambda2: float = 0.115662e-6,
                           lambda3: float = 9.900559e-6) -> float:
        """_summary_

        Parameters
        ----------
        wavelength : float, optional
            Sellmeier coefficients, by default None
        A1 : float, optional
            _description_, by default 0.696749
        A2 : float, optional
            _description_, by default 0.408218
        A3 : float, optional
            _description_, by default 0.890815
        lambda1 : float, optional
            _description_, by default 0.0690660e-6 m
        lambda2 : float, optional
            _description_, by default 0.115662e-6 m
        lambda3 : float, optional
            _description_, by default 9.900559e-6 m

        Returns
        -------
        float
            n^2, the refractive index squared.
        """
        lambda_sq = np.square(wavelength)
        a1 = A1 * lambda_sq / (lambda_sq - np.square(lambda1))
        a2 = A2 * lambda_sq / (lambda_sq - np.square(lambda2))
        a3 = A3 * lambda_sq / (lambda_sq - np.square(lambda3))
        
        return 1 + a1 + a2 + a3

    def group_index(self,
                    refractive_index: float,
                    dn: float,
                    dW: float = 0.001e-6) -> float:
        """_summary_

        Parameters
        ----------
        refractive_index : float
            refractive index
        dn : float
            change in refractive index
        dW : float, optional
            change in wavelength, by default 0.001e-6 m

        Returns
        -------
        float
            Ng, or the group index.
        """

        return refractive_index - (self.wavelength * (dn / dW))

    def group_velocity_in_medium(self):
        """_summary_

        Returns
        -------
        _type_
            _description_
        """
        return SPEED_OF_LIGHT / self.group_index()