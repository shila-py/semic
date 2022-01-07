'''
module docstring for Fermi-Dirac Integrals
'''
import numpy as np
from numpy import exp,pi,sqrt,absolute,log
from scipy.integrate import quad
from scipy.special import gamma

def fdint_approx(eta=0):
    '''
    Function to find the approximate Fermi-Dirac Integral of
    order 1/2 with an error of +/- 0.5%
    '''
    epsilon = 3 * sqrt(pi/2) * ((eta+2.13) + ((absolute(eta-2.13)**2.4)+9.6)**(5/12))**(-3/2)
    fd = 1 / (exp(-eta)+epsilon)
    return fd

def fermi_dirac_int(order=0.5,eta=0.0):
    """
    Fermi-Dirac integral

    Parameters
    ----------
    order : float, required
        DESCRIPTION. The default is 0.5.
    eta : float, required
        DESCRIPTION. The default is 0.

    Returns
    -------
    Fermi-Dirac integral result

    """
    reciprocal_gamma = 1/gamma(order+1)
    intgrl = quad(lambda t: ((t)**(order)/(1+exp(t-eta))),a=0,b=np.inf,
                  epsabs=1e-300,epsrel=1e-8,limit=100)
    return reciprocal_gamma * intgrl[0]

def ifdint_approx(eta=0):
    """
    The Inverse Fermi-Dirac Integral of Order 1/2 approximation.

    Parameters
    ----------
    eta : float, optional
        . The default is 0.

    Returns
    -------
    None.

    """
    ifd = log(eta) + ((3.53553e-1)*eta)-(4.95009e-3 * (eta**2)) + (1.48386e-4 * (eta**3)) - (4.42563e-6 * (eta**4))
    return ifd
