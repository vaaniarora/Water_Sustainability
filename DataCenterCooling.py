class DataCenterCooling:
    def __init__(self):

        self.supply_air_temp = None  # Temp leaving cooling coils
        self.return_air_temp = None   # Temp entering cooling coils
        self.it_intake_temp = None    # Average IT equipment intake air temp
        self.it_exhaust_temp = None   # Average IT equipment exhaust air temp
        
        self.data_center_class = None
        self.max_it_intake_temp = None  # Adopted max IT intake air temp
        
        self.sensors_match_it_intake = None  # Do temp/humidity sensors represent IT intake air conditions?
        self.operate_near_ashrae_max = None  # Can operate near ASHRAE max temp?
        self.has_humidification_controls = None
        self.has_dehumidification_controls = None
        self.tighter_humidity_limits = None  # Tighter than ASHRAE recommended?
        
        self.crac_control_type = None  # Centralized or distributed?
        self.crac_units_fighting = None  # Units fighting each other? (simultaneously humidifying and dehumidifying)
        self.can_apply_sensor_corrections = None # To the temp/humidity sensors

        self.can_maintain_with_crac_off = None  # Can intake air condition be maintained with CRACH/H units turned off?
        self.has_supplemental_cooling = None
        self.has_free_cooling_coil = None  # Water side economizer
        self.has_airside_free_cooling = None
        self.air_supply_path = None
        self.cable_penetration_sealing = None  # Degree of sealing
        self.cable_buildup_exceeds_limit = None
        self.cable_management_program = None
        self.it_equipment_arrangement = None  #Degree of row arrangement
        self.supply_fan_type = None
        self.high_density_areas = None  # Load densities > 4 * average load density?
        self.air_delivery_balanced = None
        self.air_balancing_program = None

        self.cooling_system_type = None
        self.has_premium_efficiency_motors = None
        self.hvac_redundancy_level = None

    def set_temperatures(self, supply_air_t, return_air_t, it_intake_t, it_exhaust_t):
        self.supply_air_temp = supply_air_t
        self.return_air_temp = return_air_t
        self.it_intake_temp = it_intake_t
        self.it_exhaust_temp = it_exhaust_t

    def set_data_center_type(self, dc_class, max_it_intake_t):
        self.data_center_class = dc_class
        self.max_it_intake_temp = max_it_intake_t

    def set_controls(self, sensors_match, near_ashrae_max, humid, dehumid, tight_limits):
        self.sensors_match_it_intake = sensors_match
        self.operate_near_ashrae_max = near_ashrae_max
        self.has_humidification_controls = humid
        self.has_dehumidification_controls = dehumid
        self.tighter_humidity_limits = tight_limits

    def set_crac_settings(self, control_type, fighting, sensor_corrections):
        self.crac_control_type = control_type
        self.crac_units_fighting = fighting
        self.can_apply_sensor_corrections = sensor_corrections

    def set_air_management_attributes(
        self,
        maintain_with_crac_off,
        supplemental_cooling,
        free_cooling_coil,
        airside_free_cooling,
        supply_path,
        cable_sealing,
        cable_buildup,
        cable_program,
        equipment_arrangement,
        fan_type,
        high_density_areas,
        delivery_balanced,
        balancing_program
    ):
        self.can_maintain_with_crac_off = maintain_with_crac_off
        self.has_supplemental_cooling = supplemental_cooling
        self.has_free_cooling_coil = free_cooling_coil
        self.has_airside_free_cooling = airside_free_cooling
        self.air_supply_path = supply_path
        self.cable_penetration_sealing = cable_sealing
        self.cable_buildup_exceeds_limit = cable_buildup
        self.cable_management_program = cable_program
        self.it_equipment_arrangement = equipment_arrangement
        self.supply_fan_type = fan_type
        self.high_density_areas = high_density_areas
        self.air_delivery_balanced = delivery_balanced
        self.air_balancing_program = balancing_program

    def set_cooling_system_attributes(self, system_type, premium_motors, redundancy_level):
        self.cooling_system_type = system_type
        self.has_premium_efficiency_motors = premium_motors
        self.hvac_redundancy_level = redundancy_level
