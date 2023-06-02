import math

# Define the data
locations = [
    ("Uttara Branch", 23.8728568, 90.3984184),
    ("City Bank Airport", 23.8513998, 90.3944536),
    ("City Bank Nikunja", 23.8330429, 90.4092871),
    ("City Bank Beside Uttara Diagnostic", 23.8679743, 90.3840879),
    ("City Bank Mirpur 12", 23.8248293, 90.3551134),
    ("City Bank Le Meridien", 23.827149, 90.4106238),
    ("City Bank Shaheed Sarani", 23.8629078, 90.3816318),
    ("City Bank Narayanganj", 23.8673789, 90.429412),
    ("City Bank Pallabi", 23.8248938, 90.3549467),
    ("City Bank JFP", 23.813316, 90.4147498),
]

# Calculate distance between two locations using Haversine formula
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in kilometers

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    distance = R * c
    return distance

# Solve TSP using Nearest Neighbor algorithm
def solve_tsp_nearest_neighbor(locations):
    num_locations = len(locations)
    visited = [False] * num_locations
    path = []
    total_distance = 0

    # Start from the first location
    current_location = 0
    path.append(locations[current_location][0])
    visited[current_location] = True

    # Visit each unvisited location
    for _ in range(num_locations - 1):
        min_distance = float('inf')
        nearest_location = None

        # Find the nearest unvisited location
        for i in range(num_locations):
            if not visited[i]:
                distance = calculate_distance(locations[current_location][1], locations[current_location][2],
                                              locations[i][1], locations[i][2])
                if distance < min_distance:
                    min_distance = distance
                    nearest_location = i

        # Moving to the nearest location
        current_location = nearest_location
        path.append(locations[current_location][0])
        visited[current_location] = True
        total_distance += min_distance

    # Return to the starting location
    path.append(locations[0][0])
    total_distance += calculate_distance(locations[current_location][1], locations[current_location][2],
                                         locations[0][1], locations[0][2])

    return path, total_distance

# Calling the function to solve TSP using the Nearest Neighbor algorithm
best_route, total_distance = solve_tsp_nearest_neighbor(locations)

# Print the best route and total distance
print("Optimized Route:")
for location in best_route:
    print(location)

print("Total Distance:", total_distance)
