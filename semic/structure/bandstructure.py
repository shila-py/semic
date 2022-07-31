'''Module docstring for Bandstructure'''

#raise NotImplementedError("Bandstructure has not been implemented yet!")

from semic.constants.constants import value
import numpy as np
import numpy.typing as npt

HBAR = value('Reduced Planck constant in eV s')

def conduction_band(k: npt.ArrayLike,
                    K_c: npt.ArrayLike,
                    M_e: npt.ArrayLike,
                    ec: float=0.0):
    """General equation for Conduction bands with minimum at Kc and assuming parabolic bands

    Parameters
    ----------
    k : npt.ArrayLike
        _description_
    K_c : npt.ArrayLike
        _description_
    M_e : npt.ArrayLike
        _description_
    ec : float, optional
        Lowest energy in the conduction bands, by default 0.0
    """
    return ec + ((np.square(HBAR) / 2) * (k - K_c) / M_e * (k - K_c))

def valence_band(k: npt.ArrayLike,
                 K_v: npt.ArrayLike,
                 M_h: npt.ArrayLike,
                 ev: float=0.0):
    """_summary_

    Parameters
    ----------
    k : npt.ArrayLike
        _description_
    K_v : npt.ArrayLike
        _description_
    M_h : npt.ArrayLike
        _description_
    ev : float, optional
        _description_, by default 0.0
    """
    return ev - ((np.square(HBAR) / 2) * (k - K_v) / M_h * (k - K_v)) 

def eff_mass_matrix(mxx: float=0.0,
                    mxy: float=0.0,
                    mxz: float=0.0,
                    myy: float=0.0,
                    myz: float=0.0,
                    mzz: float=0.0)-> npt.NDArray:
    """The effective mass matrix of electrons or holes.
    
    Effective Mass Matrix, M_e or M_h, must be symmetric due to physical considerations.
    Therefore mxy = myx, myz = mzy, mxz = mzx

    Parameters
    ----------
    mxx : float, optional
        _description_, by default 0.0
    mxy : float, optional
        _description_, by default 0.0
    mxz : float, optional
        _description_, by default 0.0
    myy : float, optional
        _description_, by default 0.0
    myz : float, optional
        _description_, by default 0.0
    mzz : float, optional
        _description_, by default 0.0

    Returns
    -------
    npt.NDArray
        Matrix corresponding to the Effective Mass Matrix. 
    """
    return np.array([[mxx,mxy,mxz],[mxy,myy,myz],[mxz,myz,mzz]])
