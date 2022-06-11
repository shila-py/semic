from semic.constants.constants import value
import numpy as np

class MOSFET:
    """
    Class describing MOSFET based on LEVEL 1-3,6 parameters from ngspice
    """
    def __init__(self,length,width,lat_len,lat_width,vto,kp,gamma,
                 phi,modulation,r_d,r_s,r_g,r_b,r_ds,r_sh,i_s,j_s,
                 p_b,c_bd,c_bs,c_j,c_jsw,m_j,m_jsw,f_c,c_gso,c_gdo,
                 c_gbo,n_sub,n_ss,n_fs,t_ox,t_p_g,x_j,mu_crit,mu_exp,
                 v_max,n_eff,x_qc,delta,theta,eta,kappa,k_f,a_f) -> None:
        """
        BLAH BLAH BLAH

        Parameters
        ----------
        length : TYPE
            DESCRIPTION.
        width : TYPE
            DESCRIPTION.
        lat_len : TYPE
            DESCRIPTION.
        lat_width : TYPE
            DESCRIPTION.
        vto : TYPE
            DESCRIPTION.
        kp : TYPE
            DESCRIPTION.
        gamma : TYPE
            DESCRIPTION.
        phi : TYPE
            DESCRIPTION.
        modulation : TYPE
            DESCRIPTION.
        r_d : TYPE
            DESCRIPTION.
        r_s : TYPE
            DESCRIPTION.
        r_g : TYPE
            DESCRIPTION.
        r_b : TYPE
            DESCRIPTION.
        r_ds : TYPE
            DESCRIPTION.
        r_sh : TYPE
            DESCRIPTION.
        i_s : TYPE
            DESCRIPTION.
        j_s : TYPE
            DESCRIPTION.
        p_b : TYPE
            DESCRIPTION.
        c_bd : TYPE
            DESCRIPTION.
        c_bs : TYPE
            DESCRIPTION.
        c_j : TYPE
            DESCRIPTION.
        c_jsw : TYPE
            DESCRIPTION.
        m_j : TYPE
            DESCRIPTION.
        m_jsw : TYPE
            DESCRIPTION.
        f_c : TYPE
            DESCRIPTION.
        c_gso : TYPE
            DESCRIPTION.
        c_gdo : TYPE
            DESCRIPTION.
        c_gbo : TYPE
            DESCRIPTION.
        n_sub : TYPE
            DESCRIPTION.
        n_ss : TYPE
            DESCRIPTION.
        n_fs : TYPE
            DESCRIPTION.
        t_ox : TYPE
            DESCRIPTION.
        t_p_g : TYPE
            DESCRIPTION.
        x_j : TYPE
            DESCRIPTION.
        mu_crit : TYPE
            DESCRIPTION.
        mu_exp : TYPE
            DESCRIPTION.
        v_max : TYPE
            DESCRIPTION.
        n_eff : TYPE
            DESCRIPTION.
        x_qc : TYPE
            DESCRIPTION.
        delta : TYPE
            DESCRIPTION.
        theta : TYPE
            DESCRIPTION.
        eta : TYPE
            DESCRIPTION.
        kappa : TYPE
            DESCRIPTION.
        k_f : TYPE
            DESCRIPTION.
        a_f : TYPE
            DESCRIPTION.

        Returns
        -------
        None
            DESCRIPTION.

        """
        self.ch_length = length
        self.ch_width = width
        self.lat_diff_len = lat_len
        self.lat_diff_width = lat_width
        self.zero_bias_threshold_voltage = vto
        self.transconductance_param = kp
        self.body_effect_param = gamma
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

    def current_gain(self,kp: float)->float:
        """_summary_

        Parameters
        ----------
        kp : float
            _description_

        Returns
        -------
        float
            _description_
        """
        if kp is None:
            return self.transconductance_param * (self.ch_width/self.ch_length)
        return kp * (self.ch_width/self.ch_length)

    def early_voltage(self,modulation: float=None)->float:
        """_summary_

        Parameters
        ----------
        modulation : float, optional
            _description_, by default None

        Returns
        -------
        float
            _description_
        """
        modulation = self.ch_len_modulation if modulation is None else modulation

        return 1/modulation

    def oxide_capacitance(self,k_ox: float,t_ox: float=None)->float:
        """_summary_

        Parameters
        ----------
        k_ox : float
            _description_
        t_ox : float, optional
            _description_, by default None

        Returns
        -------
        float
            _description_
        """
        EPSILON_NOUGHT = value("Vacuum electric permittivity")

        t_ox = self.oxide_thickness if t_ox is None else t_ox

        return (k_ox * EPSILON_NOUGHT) / t_ox
    
    def body_effect_parameter(self,concentration: float,c_ox: float)->float:
        """_summary_

        Parameters
        ----------
        concentration : float
            _description_
        c_ox : float
            _description_

        Returns
        -------
        float
            _description_
        """
        ELEMENTARY_CHARGE = value("Elementary charge")
        gamma = np.sqrt(2*ELEMENTARY_CHARGE*concentration) / c_ox
        return gamma
    
    def process_parameter(self,mu: float,c_ox: float)-> float:
        """_summary_

        Parameters
        ----------
        mu : float
            _description_
        c_ox : float
            _description_

        Returns
        -------
        float
            _description_
        """
        if mu and c_ox is None:
            return self.transconductance_param
        return mu*c_ox
    
    def threshold_voltage(self,
                          v_to: float = None,
                          gamma: float = None,
                          phi: float = None,
                          v_sb: float = None)-> float:
        """_summary_

        Parameters
        ----------
        v_to : float, optional
            _description_, by default None
        gamma : float, optional
            _description_, by default None
        phi : float, optional
            _description_, by default None
        v_sb : float, optional
            _description_, by default None

        Returns
        -------
        float
            _description_
        """
        v_to = self.zero_bias_threshold_voltage if v_to is None else v_to
        gamma = self.body_effect_param if gamma is None else gamma
        phi = self.surface_potential if phi is None else phi

        v_t = v_to + (gamma * (np.sqrt(phi + np.abs(v_sb)) - np.sqrt(phi)))
        return v_t

    def zero_potential_current(self,
                               current_gain: float = None,
                               threshold_voltage: float = None)-> float:
        """_summary_

        Parameters
        ----------
        current_gain : float, optional
            _description_, by default None
        threshold_voltage : float, optional
            _description_, by default None

        Returns
        -------
        float
            _description_
        """

        i_dss = (current_gain / 2) * (np.abs(threshold_voltage)**2)

        return i_dss

class PMOS(MOSFET):
    """PMOS class"""
    pass

class NMOS(MOSFET):
    """NMOS class"""
    pass
