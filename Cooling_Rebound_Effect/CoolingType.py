class CoolingSystemType:    
    def __init__(self, name, average_wue, range_wue, average_pue, range_pue):
            self.name = name
            self.average_wue = average_wue
            self.range_wue = range_wue
            self.average_pue = average_pue
            self.range_pue = range_pue

    def get_average_wue(self, cooling_type):
        return self.average_wue

    def get_range_wue(self, cooling_type):
        return self.range_wue
    
    

    def __str__(self):
        return f"{self.name} Cooling Type"