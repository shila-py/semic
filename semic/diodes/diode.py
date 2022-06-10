"""
Module docstring
"""
class Diode:
    """Diode class description"""
    def __init__(self,sat_current,series_resistance,emission_coeff,
                 transit_time,junction_capacitance,junction_potential,
                 junction_grading_coeff,activation_energy,temp_exponent,
                 flicker_noise_coeff,flicker_noise_exp,forward_capacitance,
                 reverse_breakdown_voltage,reverse_breakdown_current):
        """
        Sample docstring
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
