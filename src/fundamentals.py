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



def find_pn(ni=None,na=None,nd=None):
   '''
   Function to find n and p concentrations
   '''
   #constants
   k = constants.codata.value('Boltzmann constant in eV/K')

   temp = float(input("Enter temperature (in Kelvin) : "))
   eg = float(input("Enter bandgap value (in eV) : "))
   nc = float(input("Enter Nc (#/cm^3) : "))
   nv = float(input("Enter Nv (#/cm^3) : "))
   ni = sqrt(nc * nv)*exp(-eg/(2*k*temp))

   if na > nd:
      p = ((na-nd) + sqrt((na-nd)**2 + 4*(ni**2))) / 2.0
      n = (ni**2)/p
   if nd > na:
      n = ((nd-na) + sqrt((nd-na)**2 + 4*(ni**2))) / 2.0
      p = (ni**2)/n  
      
   return n,p

def eg_temp(temp):
   eg = 1.17 - 4.73e-4*(temp**2/(temp+636))
   return eg

def nc_temp(temp):
   nc = 6.2e15*temp**(3/2)
   return nc

def nv_temp(temp):
   nv = 3.5e15*temp**(3/2)
   return nv

def find_ic(i_sat, vbe, temp):
   kt = constants.codata.value('Boltzmann constant in eV/K') * temp
   ic = i_sat * exp((vbe/kt)-1)
   return ic

