import matplotlib.pyplot as plt
import csv

from DataCenterType import DataCenterType
from CoolingType import CoolingSystemType
from WaterAvailability import WaterAvailability
# from WeatherData import WeatherData

AVERAGE_SERVER_POWER_KW = 1.5
TOTAL_SERVERS = 100

def calculate_water_usage(center: DataCenterType, cooling: CoolingSystemType):
    # Calculate IT power for this data center type
    server_count = center.percent_of_servers * TOTAL_SERVERS
    it_power = server_count * AVERAGE_SERVER_POWER_KW

    # Water usage using data center WUE range
    center_wue_min, center_wue_max = center.get_range_wue(center.name)
    datacenter_water_usage_range = (
        center_wue_min * it_power,
        center_wue_max * it_power
    )

    # Water usage using cooling system WUE range
    cooling_wue_min, cooling_wue_max = cooling.get_range_wue(cooling.name)
    cooling_water_usage_range = (
        cooling_wue_min * it_power,
        cooling_wue_max * it_power
    )

    return {
        datacenter_water_usage_range, cooling_water_usage_range
    }

def plot_all_water_usage(cooling_systems, data_centers):
    dc_labels = []
    dc_avgs = []

    cooling_labels = []
    cooling_avgs = []

    # --- Data Center Types ---
    for dc in data_centers:
        server_count = dc.percent_of_servers * TOTAL_SERVERS
        it_power = server_count * AVERAGE_SERVER_POWER_KW
        min_wue, max_wue = dc.get_range_wue(dc.name)
        min_water = min_wue * it_power
        max_water = max_wue * it_power
        avg = (min_water + max_water) / 2

        dc_labels.append(dc.name)
        dc_avgs.append(avg)

    # --- Cooling Types ---
    total_it_power = TOTAL_SERVERS * AVERAGE_SERVER_POWER_KW # since for each type of cooling -- different size, should we calculate for that?
    for cooling in cooling_systems:
        min_wue, max_wue = cooling.get_range_wue(cooling.name)
        min_water = min_wue * total_it_power
        max_water = max_wue * total_it_power
        avg = (min_water + max_water) / 2

        cooling_labels.append(cooling.name)
        cooling_avgs.append(avg)

    # --- Plotting ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Data Center Plot
    ax1.barh(dc_labels, dc_avgs, color='lightblue', edgecolor='black') 
    ax1.set_title("Water Usage by Data Center Type (WUE Ranges)")
    ax1.set_xlabel("Water Usage (Liters/hour)")

    # Cooling System Plot
    ax2.barh(cooling_labels, cooling_avgs, color='lightgreen', edgecolor='black')
    ax2.set_title("Water Usage by Cooling System Type (WUE Ranges)")
    ax2.set_xlabel("Water Usage (Liters/hour)")

    plt.tight_layout()
    plt.show()


def load_cooling_systems_from_csv(csv_file):
    cooling_systems = []

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['CoolingSystem']
            
            # WUE
            avg_wue = float(row['AvgWUE'])
            min_wue = float(row['MinWUE'])
            max_wue = float(row['MaxWUE'])
            range_wue = (min_wue, max_wue)
            
            # PUE
            avg_pue = float(row['AvgPUE'])
            min_pue = float(row['MinPUE'])
            max_pue = float(row['MaxPUE'])
            range_pue = (min_pue, max_pue)


            cooling_system = CoolingSystemType(
                name=name,
                average_wue=avg_wue,
                range_wue=range_wue,
                average_pue=avg_pue,
                range_pue=range_pue
            )
            cooling_systems.append(cooling_system)
    
    return cooling_systems

def load_data_centers_from_csv(csv_file):
    data_centers = []

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Size']

            # WUE
            avg_wue = float(row['AvgWUE'])
            min_wue = float(row['MinWUE'])
            max_wue = float(row['MaxWUE'])
            range_wue = (min_wue, max_wue)

            # PUE
            avg_pue = float(row['AvgPUE'])
            min_pue = float(row['MinPUE'])
            max_pue = float(row['MaxPUE'])
            range_pue = (min_pue, max_pue)

            percent_of_servers = float(row["PercentOfServers"])

            data_center = DataCenterType(
                name = name,
                average_wue=avg_wue,
                range_wue=range_wue,
                average_pue=avg_pue,
                range_pue=range_pue,
                percent_of_servers=percent_of_servers
            )
            data_centers.append(data_center)

    return data_centers
    
def main():
    cooling_systems = load_cooling_systems_from_csv(csv_file='cooling_type_data.csv')
    data_centers = load_data_centers_from_csv(csv_file='datacenter_type_data.csv')

    center = next(c for c in data_centers if c.name == "Hyperscale")
    cooling = next(c for c in cooling_systems if c.name == "Water-Cooled Chiller")

    data_center_water_usage, cooling_water_usage = calculate_water_usage(center, cooling)

    print(f"Data Center Type: {center.name}")
    print(f"Cooling System Type: {cooling.name}")
    print(f"Water Usage (Data Center WUE): {data_center_water_usage} liters/hour (min, max)")
    print(f"Water Usage (Cooling System WUE): {cooling_water_usage} liters/hour (min, max)")

    plot_all_water_usage(cooling_systems, data_centers)
    

if __name__ == "__main__":
    main()
