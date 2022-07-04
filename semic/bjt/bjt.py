"""BJT Class Module"""
from semic.constants.constants import value

CHARGE = value('Elementary charge')
BOLTZMANN = value('Boltzmann constant in J/K')

class BJT:
    """BJT Class
    """
    def __init__(self,
                 var1: float=None,
                 var2: float=None,
                 var3: float=None,
                 varN: float=None) -> None:
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3
        self.varN = varN

class NPN(BJT):
    """_summary_

    Parameters
    ----------
    BJT : _type_
        _description_
    """
    pass

class PNP(BJT):
    """_summary_

    Parameters
    ----------
    BJT : _type_
        _description_
    """
    pass

def vbe(vb: float=0.0,
        ve: float=0.0)-> float:
    """_summary_

    Parameters
    ----------
    vb : float, optional
        _description_, by default 0.0
    ve : float, optional
        _description_, by default 0.0

    Returns
    -------
    float
        _description_
    """
    voltage = vb-ve
    return voltage

def vbc(vb: float=0.0,
        vc: float=0.0)-> float:
    """_summary_

    Parameters
    ----------
    vb : float, optional
        _description_, by default 0.0
    vc : float, optional
        _description_, by default 0.0

    Returns
    -------
    float
        _description_
    """
    voltage = vb - vc
    return voltage

def vce(vc: float=0.0,
        ve: float=0.0)-> float:
    """_summary_

    Parameters
    ----------
    vc : float, optional
        _description_, by default 0.0
    ve : float, optional
        _description_, by default 0.0

    Returns
    -------
    float
        _description_
    """
    voltage = vc - ve
    return voltage

def i_e(i_en: float=0.0,
        i_ep: float=0.0)-> float:
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

def i_b(i_ep: float=0.0,
        i_br: float=0.0,
        i_cp: float=0.0)-> float:
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

def i_c(i_cn: float=0.0,
        i_cp: float=0.0)-> float:
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

def emitter_injection_efficiency(i_en: float=0.0,
                                 i_e: float=1.0)-> float:
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

def base_transport_factor(i_cn: float=0.0,
                          i_en: float=1.0)-> float:
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

def common_base_current_gain(spec: str=None,
                             i_c: float=0.0,
                             i_e: float=1.0,
                             beta: float=0.0)-> float:
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

def common_emitter_current_gain(spec: str=None,
                                i_c: float=0.0,
                                i_b: float=1.0,
                                alpha: float=0.0)-> float:
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
