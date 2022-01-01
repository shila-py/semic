'''
module docstring for Fermi-Dirac Integrals
'''

from numpy import exp,pi,sqrt,absolute

def fdint_approx(eta=0):
    '''
    Function to find the approximate Fermi-Dirac Integral of
    order 1/2 with an error of +/- 0.5%
    '''
    epsilon = 3 * sqrt(pi/2) * ((eta+2.13) + ((absolute(eta-2.13)**2.4)+9.6)**(5/12))**(-3/2)
    fd = 1 / (exp(-eta)+epsilon)
    return fd
