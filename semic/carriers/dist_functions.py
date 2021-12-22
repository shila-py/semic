
from semic.constants.constants import value
from numpy import exp,sqrt,pi


def maxwell_boltzmann(v=None,m_star=None,temp=None):
    '''
    Function to find the the average number of electrons in 
    state f using the Maxwell-Boltzmann distribution function.

    v: group velocity of an electron in a band structure, or
       the velocity of an individual particle in a classical
       model.
    
    m_star: The effective mass of a carrier in an energy band.

    temp: Temperature in Kelvin.

    k_b: Boltzmann's constant in eV/K

    f_mb(v) = sqrt(m_star/(2pi*kb*T))*exp(-m_star*v^2/2kb*T)
    '''

    kT = value('Boltzmann constant in eV/K') * temp
    f_mb = sqrt(m_star / (2*pi*kT)) * exp(-m_star*(v**2) / (2*kT))

    return f_mb

def fermi_dirac(E=None,Ef=None,temp=None):
   '''
   Function to find the average number of electrons in state f
   using the Fermi-Dirac distribution function.

   E: Energy in eV

   Ef: Fermi energy, or chemical potential of electrons, in eV

   temp: temperature in Kelvin

   k: Boltzmann's constant in eV/K

   f_df(E) = 1/(1+exp((E-Ef)/k*temp))
   '''
   kT = value('Boltzmann constant in eV/K') * temp
   f_fd = 1/(1+exp((E-Ef)/(kT)))

   return f_fd

def bose_einstein(omega=None, temp=None):
   '''
   Function to find the average number of bosons in state f
   using the Bose-Einstein Distribution function.

   hbar: Reduced Planck Constant in eV s

   omega (w) : angular frequency in radians per second

   k_b: Boltzmann Constant in eV/K

   temp: Temperature in Kelvin

   f_be(hbar*w) = 1/(exp((h_bar*omega)/(k_b*temp)) - 1)
   '''
   kT = value('Boltzmann constant in eV/K') * temp
   h_bar = value('reduced Planck constant in eV s')

   f_be = 1/(exp((h_bar*omega)/kT) - 1)

   return f_be