"""
Created on Mon Jan 10 19:12:19 2022

@author: Nithin Kumar Santha Kumar

Description: Bipolar Junction Transistor equations
"""

def vbe(vb=0,ve=0):
    """


    Parameters
    ----------
    vb : TYPE, optional
        DESCRIPTION. The default is 0.
    ve : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    None.

    """
    voltage = vb-ve
    return voltage

def vbc(vb=0,vc=0):
    """


    Parameters
    ----------
    vb : TYPE, optional
        DESCRIPTION. The default is 0.
    vc : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    None.

    """
    voltage = vb - vc
    return voltage

def vce(vc=0,ve=0):
    """


    Parameters
    ----------
    vc : TYPE, optional
        DESCRIPTION. The default is 0.
    ve : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    None.

    """
    voltage = vc - ve
    return voltage

def i_e(i_en=0,i_ep=0):
    """
    Emitter current in a Bipolar Junction Transistor

    Parameters
    ----------
    i_en : TYPE, optional
        DESCRIPTION. The default is 0.
    i_ep : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    None.

    """
    ie = i_en + i_ep
    return ie

def i_b(i_ep=0,i_br=0,i_cp=0):
    """
    Base current in a Bipolar Junction Transistor

    Parameters
    ----------
    i_ep : TYPE, optional
        DESCRIPTION. The default is 0.
    i_br : TYPE, optional
        DESCRIPTION. The default is 0.
    i_cp : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    None.

    """
    ib = i_ep + i_br - i_cp
    return ib

def i_c(i_cn=0,i_cp=0):
    """
    Collector current in a Bipolar Junction Transistor

    Parameters
    ----------
    i_cn : TYPE, optional
        DESCRIPTION. The default is 0.
    i_cp : TYPE, optional
        DESCRIPTION. The default is 0.

    Returns
    -------
    None.

    """
    ic = i_cn + i_cp
    return ic

def emitter_injection_efficiency(i_en=0,i_e=1):
    """
    The emitter injection efficiency measures the fraction
    of the emitter current carried by the desired electrons
    or holes in a NPN or PNP device. The default is for a
    NPN device.

    Parameters
    ----------
    i_en : float, required
        Electron emitter current. The default is 0.
    i_e : TYPE, optional
        Emitter current. The default is 1.

    Returns
    -------
    A float value corresponding to the emitter injection efficiency

    """
    gamma = i_en / i_e
    return gamma

def base_transport_factor(i_cn=0,i_en=1):
    """
    The base transport factor measures the fraction of
    electrons that make it into the collector after injection
    from the emitter.

    Parameters
    ----------
    i_cn : TYPE, optional
        DESCRIPTION. The default is 0.
    i_en : TYPE, optional
        DESCRIPTION. The default is 1.

    Returns
    -------
    None.

    """
    alpha_t = i_cn / i_en
    return alpha_t

def common_base_current_gain(spec=None,i_c=0,i_e=1,beta=0):
    """
    The low frequency common-base current gain of a bipolar
    junction transistor.

    Parameters
    ----------
    spec : string, required
        Specifies calculation type. Choose 'beta' for
        calculations based on common-emitter current gain.
        The default is None.
    i_c : float, optional
        Collector current. The default is 0.
    i_e : float, optional
        Emitter current. The default is 1.
    beta : float, optional
        Common-emitter current gain. The default is 0.

    Returns
    -------
    Float value corresponding to the low freq common-base current gain

    """
    if(spec == 'beta'):
        alpha_dc = beta / (beta + 1)
    else:
        alpha_dc = i_c / i_e
    return alpha_dc

def common_emitter_current_gain(spec=None,i_c=0,i_b=1,alpha=0):
    """
    The common-emitter current gain of a bipolar
    junction transistor.

    Parameters
    ----------
    spec : string, required
        Specifies calculation type. Choose 'alpha' for
        calculations based on common-base current gain.
        The default is None.
    i_c : float, optional
        Collector current. The default is 0.
    i_b : float, optional
        Base current. The default is 1.
    alpha : float, optional
        Common-base current gain. The default is 0.

    Returns
    -------
    Float value corresponding to the common-emitter current gain

    """
    if(spec == 'alpha'):
        beta_dc = alpha / (1 - alpha)
    else:
        beta_dc = i_c / i_b
    return beta_dc
