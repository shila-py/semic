"""BJT Class Module"""
from semic.constants.constants import value

CHARGE = value('Elementary charge')
BOLTZMANN = value('Boltzmann constant in eV/K')

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