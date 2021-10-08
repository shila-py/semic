##########################################
# Semiconductor Calculations Package
# Author: Nithin Kumar Santha Kumar
# Date: 4/25/2021
##########################################
# Changelog: 
# 4/25/2021 - Started Package
# 6/29/2021 - Added additional functions
# 
##########################################

from scipy import constants
from math import pi, sqrt,exp



def find_pn(temp=None,eg=None,ni=None,na=None,nd=None):
   '''
   Function to find n and p concentrations.
   
   temp : Temperature in Kelvin
   
   eg : Bandgap value in eV
   
   ni: Intrinsic concentration
   
   na: Acceptor concentration
   
   nd: Donor concentration
   
   Returns n and p concentrations as a tuple (n,p)
   '''
   #constants
   #k = constants.codata.value('Boltzmann constant in eV/K')
   #temp = float(input("Enter temperature (in Kelvin) : "))
   #eg = float(input("Enter bandgap value (in eV) : "))
   #nc = float(input("Enter Nc (#/cm^3) : "))
   #nv = float(input("Enter Nv (#/cm^3) : "))
   #ni = sqrt(nc * nv)*exp(-eg/(2*k*temp))

   if na > nd:
      p = ((na-nd) + sqrt((na-nd)**2 + 4*(ni**2))) / 2.0
      n = (ni**2)/p
   if nd > na:
      n = ((nd-na) + sqrt((nd-na)**2 + 4*(ni**2))) / 2.0
      p = (ni**2)/n  
      
   return n,p

def eg_temp(temp=None):
   '''
   Function to find the bandgap value from temperature in Kelvin.
   
   temp: Temperature in Kelvin
   '''
   eg = 1.17 - 4.73e-4*(temp**2/(temp+636))
   return eg

def nc_temp(temp=None):
   '''
   Function to find thermal effective density of states in conduction band
   from temperature in Kelvin.
   
   temp: Temperature in Kelvin
   '''
   nc = 6.2e15*temp**(3/2)
   return nc

def nv_temp(temp=None):
   '''
   Function to find thermal effective density of states in valence band
   from temperature in Kelvin.
   
   temp: Temperature in Kelvin
   '''
   nv = 3.5e15*temp**(3/2)
   return nv

def find_ic(i_sat=None, vbe=None, temp=None):
   '''
   Function to find the collector current of a bipolar transistor.
   
   i_sat: The saturation current
   
   vbe: The DC voltage between the base and the emitter of a bipolar
        transistor.
   
   temp: The temperature in Kelvin
   '''
   kt = constants.codata.value('Boltzmann constant in eV/K') * temp
   ic = i_sat * exp((vbe/kt)-1)
   return ic

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
   kT = constants.codata.value('Boltzmann constant in eV/K') * temp
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
   kT = constants.codata.value('Boltzmann constant in eV/K') * temp
   h_bar = constants.codata.value('reduced Planck constant in eV s')

   f_be = 1/(exp((h_bar*omega)/kT) - 1)

   return f_be

def n0(Nc=None,Ec=None,Ef=None,temp=None):
   '''
   Function to find Equilibrium electron density
   in the conduction band.

   Nc: Thermal effective density of states in the
       conduction band.
   
   Ec: Conduction band edge energy in a semiconductor.
       This is the potential energy of electrons, including
       electrostatic potential.

   Ef: Fermi energy, or the chemical potential for electrons.

   k_b: Boltzmann's constant in eV/K

   temp: Temperature in Kelvin

   n0 = Nc*exp(-(Ec-Ef)/(k_b*temp))
   '''
   kT = constants.codata.value('Boltzmann constant in eV/K') * temp
   n_0 = Nc*exp(-(Ec-Ef)/kT)

   return n_0

def find_nc(mass_c=None,temp=None):
   '''
   Function to find thermal effective density of states in
   conduction band.

   mass_c: The effective mass of a carrier in the conduction band

   k_b: Boltzmann constant in eV/K

   temp: Temperature in Kelvin

   hbar: reduced Planck constant in eV s

   Nc = 2*[mass_c*k_b*temp/(2pi*hbar^2)]^(3/2)
   '''
   kT = constants.codata.value('Boltzmann constant in eV/K') * temp
   h_bar = constants.codata.value('reduced Planck constant in eV s')
   Nc = 2*((mass_c*kT/(2*pi*(h_bar**2)))**(3/2))

   return Nc

def p0(Nv=None,Ev=None,Ef=None,temp=None):
   '''
   Function to find the Equilibrium hole density
   in the valence band.

   Nv: Thermal effective density of states in valence band

   Ev: Valence band edge energy in a semiconductor.
       This is the potential energy of electrons, including
       electrostatic potential.
   
   k_b: Boltzmann constant in eV/K

   temp: Temperature in Kelvin

   p0 = Nv*exp(Ev-Ef/k_b*temp)
   '''

   kT = constants.codata.value('Boltzmann constant in eV/K') * temp
   p_0 = Nv*exp((Ev-Ef)/kT)

   return p_0

def find_nv(mass_v=None,temp=None):
   '''
   Function to find the thermal effective density
   of states in valence band.

   mass_v: The effective mass of of carrier in valence band

   temp: Temperature in Kelvin

   k_b: Boltzmann constant in eV/K

   hbar: reduced Planck constant in eV s

   Nv = 2*[mass_v*k_b*temp/(2pi*hbar^2)]^(3/2)
   '''

   kT = constants.codata.value('Boltzmann constant in eV/K') * temp
   h_bar = constants.codata.value('reduced Planck constant in eV s')

   Nv = 2*(mass_v*kT/(2*pi*(h_bar**2)))**(3/2)

   return Nv


def ni(n_0 = None, p_0 = None):
   '''
   Function to find the intrinsic carrier density

   n_0 = Equilibrium carrier density of electrons in conduction band

   p_0 = Equilibrium carrier density of holes in valence band

   ni = sqrt(n_0*p_0)
   '''

   n_i = sqrt(n_0 * p_0)

   return n_i

