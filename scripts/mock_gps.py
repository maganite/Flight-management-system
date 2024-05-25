import random

def generate_area_data(num_areas=1000):
    """
    Generates mock data for thousands of random areas in India with varying aerial conditions including geographic coordinates.
    """
    conditions = ['Low Signal Frequency', 'No Communication', 'High Signal Interference', 'No Fly Zone']
    
    area_data = []
    for _ in range(num_areas):
        # Randomly generate latitude and longitude within the bounds of India
        latitude = random.uniform(8.4, 37.6)
        longitude = random.uniform(68.7, 97.25)
        condition = random.choice(conditions)
        population_density = random.uniform(100, 15000)  # per square km
        area_data.append({
            'coordinates': (latitude, longitude),
            'condition': condition,
            'population_density': population_density
        })
    return area_data

def print_area_data(area_data):
    """
    Prints the generated area data.
    """
    for area in area_data:
        coords = area['coordinates']
        print(f"Coordinates: ({coords[0]:.2f}, {coords[1]:.2f}), Condition: {area['condition']}, Population Density: {area['population_density']:.2f}")

if __name__ == "__main__":
    area_data = generate_area_data()
    print_area_data(area_data)
