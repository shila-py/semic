'''
module docstring for carrier equilibrium density
'''

from numpy import exp,sqrt,pi
from semic.constants.constants import value

def find_n0(n_c=0,conduction_band_energy=0,fermi_energy=0,temp=0):
    '''
    Function to find nondegenerate Equilibrium electron density
    in the conduction band.

    n_c: Thermal effective density of states in the
        conduction band.

    conduction_band_energy: Conduction band edge energy in a semiconductor.
        This is the potential energy of electrons, including
        electrostatic potential.

    fermi_energy: Fermi energy, or the chemical potential for electrons.

    k_b: Boltzmann's constant in eV/K

    temp: Temperature in Kelvin

    n0 = n_c*exp(-(conduction_band_energy-fermi_energy)/(k_b*temp))
    '''
    kb_t = value('Boltzmann constant in eV/K') * temp
    n_0 = n_c*exp(-(conduction_band_energy-fermi_energy)/kb_t)

    return n_0

def find_nc(mass_c=0,temp=0):
    '''
    Function to find thermal effective density of states in
    conduction band.

    mass_c: The effective mass of a carrier in the conduction band

    k_b: Boltzmann constant in eV/K

    temp: Temperature in Kelvin

    hbar: reduced Planck constant in eV s

    n_c = 2*[mass_c*k_b*temp/(2pi*hbar^2)]^(3/2)
    '''
    kb_t = value('Boltzmann constant in eV/K') * temp
    h_bar = value('reduced Planck constant in eV s')
    n_c = 2*((mass_c*kb_t/(2*pi*(h_bar**2)))**(3/2))

    return n_c

def find_p0(n_v=0,valence_band_energy=0,fermi_energy=0,temp=0):
    '''
    Function to find the nondegenerate Equilibrium hole density
    in the valence band.

    n_v: Thermal effective density of states in valence band

    valence_band_energy: Valence band edge energy in a semiconductor.
        This is the potential energy of electrons, including
        electrostatic potential.

    k_b: Boltzmann constant in eV/K

    temp: Temperature in Kelvin

    p0 = n_v*exp(valence_band_energy-fermi_energy/k_b*temp)
    '''

    kb_t = value('Boltzmann constant in eV/K') * temp
    p_0 = n_v*exp((valence_band_energy-fermi_energy)/kb_t)

    return p_0

def find_nv(mass_v=0,temp=0):
    '''
    Function to find the thermal effective density
    of states in valence band.

    mass_v: The effective mass of of carrier in valence band

    temp: Temperature in Kelvin

    k_b: Boltzmann constant in eV/K

    hbar: reduced Planck constant in eV s

    n_v = 2*[mass_v*k_b*temp/(2pi*hbar^2)]^(3/2)
    '''

    kb_t = value('Boltzmann constant in eV/K') * temp
    h_bar = value('reduced Planck constant in eV s')

    n_v = 2*(mass_v*kb_t/(2*pi*(h_bar**2)))**(3/2)

    return n_v


def find_ni(n_0 = 0, p_0 = 0):
    '''
    Function to find the intrinsic carrier density

    n_0 = Equilibrium carrier density of electrons in conduction band

    p_0 = Equilibrium carrier density of holes in valence band

    n_i = sqrt(n_0*p_0)
    '''

    n_i = sqrt(n_0 * p_0)

    return n_i
