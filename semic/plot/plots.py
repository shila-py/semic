"""
module docstring for plottting E-k plots
"""

import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
#import plotly.io as pio
import numpy as np
from semic.carriers.dist_functions import fermi_dirac,maxwell_boltzmann,bose_einstein

#pio.renderers.default = 'svg'

def ekplot(energy=0,k=0):
    '''

    Parameters
    ----------
    energy : TYPE, optional
        DESCRIPTION. The default is 0.
    k : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    None.

    '''
    pass

def iv_curve(data=None):
    '''

    Parameters
    ----------
    data : TYPE, optional
        DESCRIPTION. The default is None.

    Returns
    -------
    None.

    '''
    pass

def distribution_function_plot(distribution_function=None,
                               energy=0,
                               fermi_energy=0,
                               omega=0,
                               velocity=0,
                               m_star=0,
                               temp=300):
    '''

    Parameters
    ----------
    distribution_function : str, required
        Distribution Functions (Fermi-Dirac,Maxwell-Boltzmann, Bose-Einstein).
        The default is None.
    energy : float, optional
        DESCRIPTION. The default is 0.
    fermi_energy : float, optional
        DESCRIPTION. The default is 0.
    omega : float, optional
        angular frequency in rad/s. The default is 0.
    velocity : float, optional
        velocity or group velocity of electrons. The default is 0.
    m_star : float, optional
        effective mass in carrier band. The default is 0.
    temp : float, optional
        Temperature in Kelvin. The default is 1.

    Returns
    -------
    None.

    '''
    if(distribution_function == 'Fermi-Dirac'):
        x = np.arange(start = (energy-fermi_energy) - 1,
                        stop = (energy-fermi_energy) + 1.1, step=0.1)

        fig = go.Figure(data = go.Scatter(x = x,y = fermi_dirac(x,0,temp)))
        fig.update_layout(title="Fermi-Dirac Distribution",
                          xaxis_title = '(E-Ef)/kbT',
                          yaxis_title = 'f_FD (E)')
        fig.show()
        '''
        sns.lineplot(x=x,y=fermi_dirac(x,0,temp))
        plt.xlabel("E-Ef (eV)")
        plt.ylabel("f_FD(E)")
        plt.title("Fermi-Dirac Distribution")'''
    elif(distribution_function == 'Maxwell-Boltzmann'):
        x = np.linspace(start = 0,stop = velocity + 1000)
        sns.lineplot(x=x,y=maxwell_boltzmann(x,m_star,temp))
        plt.xlabel("Velocity")
        plt.ylabel("f_MB")
        plt.title("Maxwell-Boltzmann Distribution")
    elif(distribution_function == 'Bose-Einstein'):
        x = np.linspace(start=1,stop=omega+10)
        sns.lineplot(x=x,y=bose_einstein(x,temp))
        plt.xlabel("\u03C9")
        plt.ylabel("f_BE")
        plt.title("Bose-Einstein Distribution")
    else:
        raise ValueError("ERROR! please specify a distribution function!")
