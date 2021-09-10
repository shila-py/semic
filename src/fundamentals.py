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
from math import sqrt,exp



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

def fermi_dirac_df(E=None,Ef=None,temp=None):
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

