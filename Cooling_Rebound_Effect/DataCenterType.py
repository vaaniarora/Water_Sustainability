class DataCenterType:
    def __init__(self, name, average_wue, range_wue, average_pue, range_pue, percent_of_servers):
        self.name = name  # e.g., 'Hyperscale'
        self.average_wue = average_wue
        self.range_wue = range_wue
        self.average_pue = average_pue
        self.range_pue = range_pue
        self.percent_of_servers = percent_of_servers

    def get_average_wue(self, name):
        return self.average_wue

    def get_range_wue(self, name):
        return self.range_wue
    
    def get_average_pue(self):
        return self.average_pue

    def get_range_pue(self):
        return self.range_pue

    def __str__(self):
        return f"{self.name} Data Center"