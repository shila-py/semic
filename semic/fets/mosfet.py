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

    def transconductance(self,
                         i_d: float=None,
                         v_gs: float=None,
                         v_t: float=None,
                         current_gain: float=None,
                         process_param: float=None,
                         width: float=None,
                         length: float=None)-> float:
        """_summary_

        Parameters
        ----------
        i_d : float, optional
            _description_, by default None
        v_gs : float, optional
            _description_, by default None
        v_t : float, optional
            _description_, by default None
        current_gain : float, optional
            _description_, by default None
        process_param : float, optional
            _description_, by default None
        width : float, optional
            _description_, by default None
        length : float, optional
            _description_, by default None

        Returns
        -------
        float
            _description_
        """
        formula_a = [current_gain,v_gs,v_t]
        formula_b = [process_param,width,length,i_d]
        formula_c = [i_d,v_gs,v_t]
        
        if all(params is not None for params in formula_a):
            g_m1 = current_gain * (v_gs - v_t)
            return g_m1
        elif all(params is not None for params in formula_b):
            g_m2 = np.sqrt(2 * process_param * (width / length)) * np.sqrt(i_d)
            return g_m2
        elif all(params is not None for params in formula_c):
            g_m3 = 2 * i_d / (v_gs - v_t)
            return g_m3
        else:
            raise TypeError("Function needs 3 correct arguments!")

    def body_transconductance(self,body_effect,transconductance)-> float:
        """_summary_

        Parameters
        ----------
        body_effect : _type_
            _description_
        transconductance : _type_
            _description_

        Returns
        -------
        float
            _description_
        """
        g_mb = body_effect * transconductance
        return g_mb

    def body_effect(self,
                    gamma: float=None,
                    phi: float=None,
                    v_sb: float=0.0)-> float:
        """_summary_

        Parameters
        ----------
        gamma : float
            _description_
        phi : float, optional
            _description_, by default None
        v_sb : float, optional
            _description_, by default 0.0

        Returns
        -------
        float
            _description_
        """
        bep = self.body_effect_param if gamma is None else gamma
        two_phi = self.surface_potential if phi is None else phi

        body_eff = bep * (2 * np.sqrt(two_phi + np.abs(v_sb)))

        return body_eff

    def gate_source_capacitance(self,
                                c_ox: float,
                                width: float=None,
                                length: float=None,
                                length_ld: float=None,
                                c_gd: float=None)-> float:
        """_summary_

        Parameters
        ----------
        c_ox : float
            _description_
        width : float, optional
            _description_, by default None
        length : float, optional
            _description_, by default None
        length_ld : float, optional
            _description_, by default None

        Returns
        -------
        float
            _description_
        """

        l_ov = self.lat_diff_len if length_ld is None else length_ld
        channel_width = self.ch_width if width is None else width
        channel_length = self.ch_length if length is None else length
        cgd = ((channel_width * l_ov) * c_ox) if c_gd is None else c_gd

        c_gs = ((2 / 3) * (channel_width / channel_length) * c_ox) + cgd

        return c_gs

    def gate_drain_capacitance(self,
                               c_ox: float,
                               width: float=None,
                               length_ld: float=None)-> float:
        """_summary_

        Parameters
        ----------
        c_ox : float
            _description_
        width : float, optional
            _description_, by default None
        length_ld : float, optional
            _description_, by default None

        Returns
        -------
        float
            _description_
        """
        l_ov = self.lat_diff_len if length_ld is None else length_ld
        channel_width = self.ch_width if width is None else width

        c_gd = (channel_width * l_ov) * c_ox

        return c_gd

    def source_body_capacitance(self,
                                v_sb: float,
                                v_o: float,
                                c_sbo: float=None)-> float:
        """_summary_

        Parameters
        ----------
        c_sbo : float
            _description_
        v_sb : float
            _description_
        v_o : float
            _description_

        Returns
        -------
        float
            _description_
        """
        csbo = self.bulk_source_cap if c_sbo is None else c_sbo

        c_sb = csbo / np.sqrt(1 + (v_sb / v_o))
        return c_sb

    def drain_body_capacitance(self,
                               v_db: float,
                               v_o: float,
                               c_dbo: float=None)-> float:
        """_summary_

        Parameters
        ----------
        v_db : float
            _description_
        v_o : float
            _description_
        c_dbo : float, optional
            _description_, by default None

        Returns
        -------
        float
            _description_
        """
        cdbo = self.bulk_drain_cap if c_dbo is None else c_dbo

        c_db = cdbo / np.sqrt(1 + (v_db / v_o))
        return c_db

    def transition_frequency(self,
                             g_m: float,
                             c_gs: float,
                             c_gd: float)-> float:
        """_summary_

        Parameters
        ----------
        g_m : float
            _description_
        c_gs : float
            _description_
        c_gd : float
            _description_

        Returns
        -------
        float
            _description_
        """
        f_T = g_m / (2 * np.pi * (c_gs + c_gd))
        return f_T

class PMOS(MOSFET):
    """PMOS class"""
    def body_effect_parameter(self,
                              concentration: float,
                              c_ox: float)-> float:
        """_summary_

        Parameters
        ----------
        mos_type : str
            Type of MOSFET. pMOS or nMOS. Input options are 'p' or 'n' 
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
        gamma = -1.0*np.sqrt(2*ELEMENTARY_CHARGE*concentration) / c_ox
        return gamma
    
    def operation_mode(self,
                       v_gs: float,
                       v_ds: float,
                       v_tp: float)-> str:
        """_summary_

        Parameters
        ----------
        v_gs : float
            _description_
        v_ds : float
            _description_
        v_tp : float
            _description_

        Returns
        -------
        str
            _description_
        """
        modes = ["Cut off", "Linear", "Saturation", "Lin/Sat Boundary"]

        volt = v_gs - v_tp

        if v_gs > v_tp:
            return modes[0] #Cut off mode
        elif (v_gs < v_tp) and (v_ds < volt):
            return modes[1]
        elif (v_gs < v_tp) and (v_ds > volt):
            return modes[2]
        elif (v_ds == volt):
            return modes[3]

    def drain_current(self,
                      mode: str,
                      current_gain: float,
                      v_gs: float,
                      v_tp: float,
                      v_ds: float,
                      lamda: float = 0.0)-> float:
        """_summary_

        Parameters
        ----------
        mode : str
            _description_
        current_gain : float
            _description_
        v_gs : float
            _description_
        v_tp : float
            _description_
        v_ds : float
            _description_
        lamda : float, optional
            _description_, by default 0.0

        Returns
        -------
        float
            _description_

        Raises
        ------
        ValueError
            _description_
        """
        modes = ["Cut off", "Linear", "Saturation"]

        if mode not in modes:
            raise ValueError("Invalid mode! Mode must be Cut off, Linear, or Saturation!")

        if mode == "Cut off":
            return 0.0  #cutoff region drain current is always 0.0 Amperes
        elif mode == "Linear":
            if np.abs(v_ds) < 1.0:
                return current_gain * (v_gs-v_tp) * v_ds #approx Linear drain current
            else:
                v_sq = (v_ds * (v_gs - v_tp)) - ((v_ds ** 2) / 2)
                return current_gain * v_sq #triode region drain current
        elif mode == "Saturation":
            k = 0.5*current_gain
            voltage_product = ((v_gs - v_tp) ** 2) * (1 + (lamda*v_ds))
            return k * voltage_product #saturation region drain current

class NMOS(MOSFET):
    """NMOS class"""
    def body_effect_parameter(self,
                              concentration: float,
                              c_ox: float)-> float:
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

    def operation_mode(self,
                       v_gs: float,
                       v_ds: float,
                       v_tn: float)-> str:
        """_summary_

        Parameters
        ----------
        v_gs : float
            _description_
        v_ds : float
            _description_
        v_tn : float
            _description_

        Returns
        -------
        str
            _description_
        """
        modes = ["Cut off", "Linear", "Saturation", "Lin/Sat Boundary"]

        volt = v_gs - v_tn

        if v_gs < v_tn:
            return modes[0] #Cut off mode
        elif (v_gs > v_tn) and (v_ds > volt):
            return modes[1]
        elif (v_gs > v_tn) and (v_ds < volt):
            return modes[2]
        elif (v_ds == volt):
            return modes[3]

    def drain_current(self,
                      mode: str,
                      current_gain: float,
                      v_gs: float,
                      v_tn: float,
                      v_ds: float,
                      lamda: float = 0.0)-> float:
        """_summary_

        Parameters
        ----------
        mode : str
            _description_
        current_gain : float
            _description_
        v_gs : float
            _description_
        v_tn : float
            _description_
        v_ds : float
            _description_
        lamda : float, optional
            _description_, by default 0.0

        Returns
        -------
        float
            _description_

        Raises
        ------
        ValueError
            _description_
        """
        modes = ["Cut off", "Linear", "Saturation"]

        if mode not in modes:
            raise ValueError("Invalid mode! Mode must be Cut off, Linear, or Saturation!")

        if mode == "Cut off":
            return 0.0  #cutoff region drain current is always 0.0 Amperes
        elif mode == "Linear":
            if v_ds < 1.0:
                return current_gain * (v_gs-v_tn) * v_ds #approx Linear drain current
            else:
                v_sq = (v_ds * (v_gs - v_tn)) - ((v_ds ** 2) / 2)
                return current_gain * v_sq #triode region drain current
        elif mode == "Saturation":
            k = 0.5*current_gain
            voltage_product = ((v_gs - v_tn) ** 2) * (1 + (lamda*v_ds))
            return k * voltage_product #saturation region drain current
