class DataCenterCooling:
    def __init__(self):

        self.supply_air_temp = None  # Temp leaving cooling coils
        self.return_air_temp = None   # Temp entering cooling coils

        self.data_center_class = None
        
        self.has_humidification_controls = None  # Y/N
        self.has_dehumidification_controls = None  # Y/N
        
        self.has_free_cooling_coil = None  # Water side economizer   # Y/N
        self.has_airside_free_cooling = None  # Y/N

        self.cooling_system_type = None  # Air-cooled DX, Water-Cooled DX, Evaporatively-Cooled DX, Chilled Water
        self.chiller_type = None  # Air-Cooled, Water-Cooled
        self.chilled_water_supply_temperature = None
        self.water_side_economizer = None  # None, Integrated, Non-Integrated

    def set_temperatures(self, supply_air_t, return_air_t):
        self.supply_air_temp = supply_air_t
        self.return_air_temp = return_air_t

    def set_data_center_type(self, dc_class):
        self.data_center_class = dc_class

    def set_controls(self, humid, dehumid):
        self.has_humidification_controls = humid
        self.has_dehumidification_controls = dehumid

    def set_air_management_attributes(
        self,
        free_cooling_coil,
        airside_free_cooling,        
    ):
        self.has_free_cooling_coil = free_cooling_coil
        self.has_airside_free_cooling = airside_free_cooling

    def set_cooling_system_attributes(self, system_type, chill_type=None, chill_water_supply_temp=None, water_side_econ=None):
        self.cooling_system_type = system_type.lower()

        if self.cooling_system_type == "chilled water":
            self.chiller_type = chill_type
            self.chilled_water_supply_temperature = chill_water_supply_temp

            if chill_type and chill_type.lower() == "water-cooled":
                self.water_side_economizer = chill_water_supply_temp
            else:
                self.water_side_economizer = None
        else:
            self.chiller_type = None
            self.chilled_water_supply_temperature = None
