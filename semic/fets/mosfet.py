
class MOSFET:
    """
    Class describing MOSFET based on LEVEL 1-3,6 parameters from ngspice
    """
    def __init__(self,length,width,lat_len,lat_width,vto,kp,gamma,
                 phi,modulation,r_d,r_s,r_g,r_b,r_ds,r_sh,i_s,j_s,
                 p_b,c_bd,c_bs,c_j,c_jsw,m_j,m_jsw,f_c,c_gso,c_gdo,
                 c_gbo,n_sub,n_ss,n_fs,t_ox,t_p_g,x_j,mu_crit,mu_exp,
                 v_max,n_eff,x_qc,delta,theta,eta,kappa,k_f,a_f) -> None:
        self.ch_length = length
        self.ch_width = width
        self.lat_diff_len = lat_len
        self.lat_diff_width = lat_width
        self.zero_bias_threshold_voltage = vto
        self.transconductance_param = kp
        self.bulk_threshold_param = gamma
        self.surface_potential = phi
        self.ch_len_modulation = modulation
        self.drain_ohmic_resist = r_d
        self.source_ohmic_resist = r_s
        self.gate_ohmic_resist = r_g
        self.bulk_ohmic_resist = r_b
        self.drain_source_resist = r_ds
        self.sheet_resist = r_sh
        self.sat_current = i_s
        self.sat_current_area = j_s
        self.bulk_junction_potential = p_b
        self.bulk_drain_cap = c_bd
        self.bulk_source_cap = c_bs
        self.bulk_bot_cap_area = c_j
        self.bulk_sidewall_cap_area = c_jsw
        self.bulk_bot_grading_coeff = m_j
        self.bulk_sidewall_grading_coeff = m_jsw
        self.forward_bias_cap_coeff = f_c
        self.gate_source_overlap_cap = c_gso
        self.gate_drain_overlap_cap = c_gdo
        self.gate_bulk_overlap_cap = c_gbo
        self.substrate_doping_density = n_sub
        self.surface_state_density = n_ss
        self.fast_surface_state_density = n_fs
        self.oxide_thickness = t_ox
        self.gate_mat_type = t_p_g
        self.junction_depth = x_j
        self.mobility_degredation_crit = mu_crit
        self.mobility_degredation_exp = mu_exp
        self.max_drift_mobility = v_max
        self.tot_channel_charge_coeff = n_eff
        self.ch_charge_drain = x_qc
        self.width_effect_on_threshold = delta
        self.mobility_modulation = theta
        self.static_feedback = eta
        self.sat_field_factor = kappa
        self.flicker_noise_coeff = k_f
        self.flicker_noise_exp = a_f
