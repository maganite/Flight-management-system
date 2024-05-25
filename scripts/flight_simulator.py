import requests

import time
import numpy as np
from scipy.interpolate import interp1d
from geopy.distance import geodesic


# Define the waypoints
waypoints = [
    (34.052235, -118.243683),  # Los Angeles
    (35.1738, -94.0429),  # Las Vegas
    (40.712776, -74.005974),   # New York
]

# Define altitudes for each waypoint
altitudes = [3000, 15000, 5000]

# Function to calculate total distance between waypoints
def calculate_distances(waypoints):
    distances = []
    for i in range(len(waypoints)-1):
        point1 = waypoints[i]
        point2 = waypoints[i+1]
        distance = geodesic(point1, point2).miles
        distances.append(distance)
    return distances

# Calculate total distances for flight path
distances = calculate_distances(waypoints)
print(distances)
# Assume a constant airspeed (miles per hour)
airspeed_mph = 50000

# Calculate time intervals based on distances and airspeed
times = [0]
for distance in distances:
    travel_time = (distance / airspeed_mph) * 3600  # convert hours to seconds
    times.append(times[-1] + travel_time)
print(times)
# Create interpolating functions
latitudes, longitudes = zip(*waypoints)
latitude_interp = interp1d(times, latitudes, kind='linear')
longitude_interp = interp1d(times, longitudes, kind='linear')
altitude_interp = interp1d(times, altitudes, kind='linear')

def simulate_flight():
    start_time = time.time()
    total_duration = times[-1]

    while True:
        elapsed = time.time() - start_time
        if elapsed > total_duration:
            break

        lat = latitude_interp(elapsed)
        lon = longitude_interp(elapsed)
        alt = altitude_interp(elapsed)
        airspeed = 450 + np.random.randn() * 10
        engine_temp = 200 + np.random.randn() * 5
        fuel_level = 100 - (elapsed / total_duration * 100)

        print(f"Time: {elapsed:.2f}s")
        print(f"Current Position: Latitude = {lat:.4f}, Longitude = {lon:.4f}")
        print(f"Altitude: {alt:.0f} feet")
        print(f"Airspeed: {airspeed:.1f} knots")
        print(f"Engine Temperature: {engine_temp:.1f}°C")
        print(f"Fuel Level: {fuel_level:.1f}%")
        print("-" * 40)
        flight_data = {
            "elapsed": f"{elapsed:.2f}",
            "lat": f"{lat:.4f}",
            "lon": f"{lon:.4f}",
            "alt": f"{alt:.0f}",
            "airspeed": f"{airspeed:.1f}",
            "engine_temp": f"{engine_temp:.1f}",
            "fuel_level": f"{fuel_level:.1f}%"
        }
        url = "http://localhost:8000/flight/get_data/1/"
        response = requests.post(url, json=flight_data)

        if response.status_code == 200:
            try:
                data = response.json()
                print("JSON Data:", data)
            except ValueError:
                print("Invalid JSON received:", response.text)
        else:
            print("Failed to retrieve data. Status Code:", response.status_code)
            print("Response:", response.text)
        time.sleep(1)

simulate_flight()
