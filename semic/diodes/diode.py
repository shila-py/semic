"""
Module docstring
"""
class Diode:
    """Diode class description"""
    def __init__(self,
                 sat_current: float,
                 series_resistance: float,
                 emission_coeff: float,
                 transit_time: float,
                 junction_capacitance: float,
                 junction_potential: float,
                 junction_grading_coeff: float,
                 activation_energy: float,
                 temp_exponent: float,
                 flicker_noise_coeff: float,
                 flicker_noise_exp: float,
                 forward_capacitance: float,
                 reverse_breakdown_voltage: float,
                 reverse_breakdown_current: float)-> None:
        """_summary_

        Parameters
        ----------
        sat_current : float
            _description_
        series_resistance : float
            _description_
        emission_coeff : float
            _description_
        transit_time : float
            _description_
        junction_capacitance : float
            _description_
        junction_potential : float
            _description_
        junction_grading_coeff : float
            _description_
        activation_energy : float
            _description_
        temp_exponent : float
            _description_
        flicker_noise_coeff : float
            _description_
        flicker_noise_exp : float
            _description_
        forward_capacitance : float
            _description_
        reverse_breakdown_voltage : float
            _description_
        reverse_breakdown_current : float
            _description_
        """
        self.i_s = sat_current
        self.r_s = series_resistance
        self.em_coeff = emission_coeff
        self.t_t = transit_time
        self.c_d0 = junction_capacitance
        self.v_j = junction_potential
        self.j_gc = junction_grading_coeff
        self.e_g = activation_energy
        self.p_i = temp_exponent
        self.k_f = flicker_noise_coeff
        self.a_f = flicker_noise_exp
        self.f_c = forward_capacitance
        self.b_v = reverse_breakdown_voltage
        self.i_bv = reverse_breakdown_current
