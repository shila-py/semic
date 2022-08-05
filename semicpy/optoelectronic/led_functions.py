"""
Module docstring for LED fundamental equations

Based on Optoelectronics and Photonics: Principles and Practices by S.O. Kasap
"""
import numpy as np
from semicpy.constants.constants import value

###########################CONSTANTS#############################
K = 633 #lm W^-1 Conversion constant
CHARGE = value("Elementary charge") #Coulombs
BOLTZMANN = value("Boltzmann constant in J/K") #Joule / Kelvin
PLANCK = value("Planck constant in J s") #Joule-second
SPEED_OF_LIGHT = value("Speed of light in vacuum") #meter/second
#################################################################
luminous_efficacy_dict = {380: 0.000039, 390: 0.000120, 400: 0.000396, 410: 0.001210, 420: 0.004000,
                          430: 0.011600, 440: 0.023000, 450: 0.038000, 460: 0.060000, 470: 0.090980,
                          480: 0.139020, 490: 0.208020, 500: 0.323000, 507: 0.444310, 510: 0.503000,
                          520: 0.710000, 530: 0.862000, 540: 0.954000, 550: 0.994950, 555: 1.000000,
                          560: 0.995000, 570: 0.952000, 580: 0.870000, 590: 0.757000, 600: 0.631000,
                          610: 0.503000, 620: 0.381000, 630: 0.265000, 640: 0.175000, 650: 0.107000,
                          660: 0.061000, 670: 0.032000, 680: 0.017000, 690: 0.008200, 700: 0.004102,
                          710: 0.002091, 720: 0.001047, 730: 0.000520, 740: 0.000249, 750: 0.000120,
                          760: 0.000060, 770: 0.000030}

def internal_quantum_eff(tau_r: float=None,
                         tau_nr: float=None,
                         flux_ph: float=0.0,
                         current: float=1.0)-> float:
    """_summary_

    Parameters
    ----------
    tau_r : float
        _description_
    tau_nr : float
        _description_
    flux_ph : float, optional
        _description_, by default 0.0
    current : float, optional
        _description_, by default 1.0

    Returns
    -------
    float
        Internal quantum efficiency.
    """
    if (tau_r is None) or (tau_nr is None):
        return flux_ph / (current / CHARGE)
    else:
        return np.reciprocal(tau_r) / (np.reciprocal(tau_r) + np.reciprocal(tau_nr))


def photon_flux(internal_optical_power,
                frequency: float=1.0):
    """The number of photons emitted per second.

    Parameters
    ----------
    internal_optical_power : float
        _description_
    frequency : float, optional
        _description_, by default 1.0 Hz

    Returns
    -------
    float
        Photon flux. Units are m^-2 s^-1
    """
    return internal_optical_power / (PLANCK * frequency)

def external_quantum_eff(radiant_flux,
                         frequency: float=1.0,
                         current: float=1.0)-> float:
    """_summary_

    Parameters
    ----------
    radiant_flux : _type_
        Optical power emitted to the ambient. Unit is W or Watt
    frequency : float, optional
        _description_, by default 1.0 Hz
    current : float, optional
        Electric current, by default 1.0 A

    Returns
    -------
    float
        _description_
    """
    nom = radiant_flux / (PLANCK * frequency)
    denom = current / CHARGE

    return nom / denom

def extraction_eff(photons_emitted: float,
                   photons_generated: float)-> float:
    """_summary_

    Parameters
    ----------
    photons_emitted : float
        _description_
    photons_generated : float
        _description_

    Returns
    -------
    float
        _description_
    """
    return photons_emitted / photons_generated

def emitted_optical_power(extraction_eff,
                          internal_quantum_eff,
                          frequency,
                          current)-> float:
    """Emitted Optical Output Power, or Radiant Flux.

    Parameters
    ----------
    extraction_eff : _type_
        _description_
    internal_quantum_eff : _type_
        _description_
    frequency : _type_
        _description_
    current : _type_
        _description_

    Returns
    -------
    float
        _description_
    """
    return PLANCK * frequency * extraction_eff * internal_quantum_eff * (current / CHARGE)

def power_efficiency(optical_power_out,
                     electrical_power_in)-> float:
    """_summary_

    Parameters
    ----------
    optical_power_out : _type_
        _description_
    electrical_power_in : _type_
        _description_

    Returns
    -------
    float
        _description_
    """
    return optical_power_out / electrical_power_in

def luminous_flux(radiant_flux,
                  luminosity_func)-> float:
    """_summary_

    Parameters
    ----------
    radiant_flux : _type_
        _description_
    luminosity_func : _type_
        _description_

    Returns
    -------
    float
        _description_
    """
    return radiant_flux * K * luminosity_func

def luminosity_function(wavelength)-> float:
    """_summary_

    Parameters
    ----------
    wavelength : _type_
        _description_

    Returns
    -------
    float
        _description_
    """
    return luminous_efficacy_dict.get(wavelength)
    

def luminous_efficacy(lflux: float,
                      I: float=1.0,
                      V: float=1.0)-> float:
    """Luminous efficacy of a light source. The efficiency with which an electric 
    light source converts the input electric power (watts) into emitted luminous flux (lumens).

    Parameters
    ----------
    lflux : float
        Luminous flux, or the measure of the perceived power of light. Units are lm or lumens.
    I : float, optional
        Electric current, by default 1.0 A
    V : float, optional
        Voltage, by default 1.0 V

    Returns
    -------
    float
        phi_v. A value that corresponds to the luminous efficacy of a light source. Units are lm W^-1.
    """ 
    if (I == 0) or (V == 0):
        raise ZeroDivisionError("Divide by zero! I or V must be not equal to zero!")
    else:
        phi_v = lflux / (I * V)
        return phi_v

def spectral_line_width(peak_lambda,
                        temperature: float=300.0)-> float:
    """_summary_

    Parameters
    ----------
    peak_lambda : _type_
        _description_
    temperature : float, optional
        _description_, by default 300.0

    Returns
    -------
    float
        _description_
    """
    return np.square(peak_lambda) * 3 * BOLTZMANN * temperature / (PLANCK * SPEED_OF_LIGHT)

def light_extraction_ratio(critical_angle: float=0.0,
                           transmittance: float=0.0):
    """_summary_

    Parameters
    ----------
    critical_angle : float, optional
        _description_, by default 0.0
    transmittance : float, optional
        _description_, by default 0.0
    """
    return 0.5 * (1 - np.cos(critical_angle)) * transmittance

def critical_angle(n_a,
                   n_s)-> float:
    """_summary_

    Parameters
    ----------
    n_a : _type_
        _description_
    n_s : _type_
        _description_

    Returns
    -------
    float
        The critical angle in radians
    """
    return np.arcsin(n_a / n_s)