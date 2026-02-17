import pandas as pd

class WaterAvailability:
    def __init__(self, location, month, aware_factor):
        self.location = location
        self.month = month
        self.aware_factor = aware_factor

#     @classmethod
#     def from_csv(cls, file_path):
#         df = pd.read_csv(file_path)
#         objects = []
#         for index, row in df.iterrows():
#             obj = cls(location=row['location'], month=row['month'], aware_factor=row['aware_factor'])
#             objects.append(obj)
#         return objects

# water_availabilities = WaterAvailability.from_csv('Aware102_SimaPro8_4.csv')
