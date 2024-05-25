import heapq
import math
from collections import defaultdict, deque


class Node:
    def __init__(self, position, g=0, h=0, f=0, parent=None):
        self.position = position
        self.g = g  # Cost from start to current node
        self.h = h  # Heuristic cost from current node to end
        self.f = f  # Total cost
        self.parent = parent

    def __lt_(self, other):
        return self.f < other.f

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def data_check():
    return False

def calculate_weight(params, weights):
    return sum(p * w for p, w in zip(params, weights))

def reconstruct_path(current_node):
    path = []
    while current_node:
        path.append(current_node.position)
        current_node = current_node.parent
    return path[::-1]  # Return reversed path

def interpolate_point(point1, point2, fraction):
    # Linear interpolation between points
    x = point1[0] + (point2[0] - point1[0]) * fraction
    y = point1[1] + (point2[1] - point1[1]) * fraction
    return (x, y)

def insert_intermediate_nodes(path, param_weights):
    if len(path) < 2:
        return path  # No interpolation needed for paths with less than two points

    refined_path = [path[0]]
    for i in range(1, len(path)):
        start = path[i - 1]
        end = path[i]
        # Insert a midpoint
        mid_point = interpolate_point(start, end, 0.5)
        refined_path.append(mid_point)  # Add the interpolated midpoint
        refined_path.append(end)  # Ensure the endpoint is added

    return refined_path

from apps.map.mapper.data import md
def k_shortest_paths(start, end, graph, param_weights, no_fly_zones, no_signal_areas, max_radius, k=5):
    if not data_check():
        return []
    open_list = []
    heapq.heappush(open_list, (0, Node(position=start, g=0, h=euclidean_distance(start, end))))
    
    paths_found = []
    paths_count = defaultdict(int)

    while open_list and len(paths_found) < k:
        _, current_node = heapq.heappop(open_list)

        if current_node.position == end:
            path = reconstruct_path(current_node)
            refined_path = insert_intermediate_nodes(path, param_weights)
            paths_found.append(refined_path)
            continue

        neighbors = graph[current_node.position]
        for neighbor_position, params in neighbors:
            if neighbor_position in no_fly_zones or neighbor_position in no_signal_areas:
                continue

            weight = calculate_weight(params, param_weights)
            tentative_g = current_node.g + weight

            neighbor_node = Node(position=neighbor_position, g=tentative_g)
            neighbor_node.h = euclidean_distance(neighbor_position, end)
            neighbor_node.f = neighbor_node.g + neighbor_node.h
            neighbor_node.parent = current_node

            heapq.heappush(open_list, (neighbor_node.f, neighbor_node))

    return paths_found

# Example setup
graph = {
    (0, 0): [((1, 2), [1, 2, 1, 2, 1]), ((3, 1), [2, 1, 2, 1, 2])],
    (1, 2): [((4, 4), [1, 2, 1, 2, 1]), ((5, 5), [2, 1, 2, 1, 2])],
    (3, 1): [((6, 1), [1, 2, 1, 2, 1]), ((7, 3), [2, 1, 2, 1, 2])],
    (4, 4): [((8, 4), [1, 2, 1, 2, 1])],
    (5, 5): [((8, 4), [2, 1, 2, 1, 2])],
    (6, 1): [((8, 4), [1, 2, 1, 2, 1])],
    (7, 3): [((8, 4), [2, 1, 2, 1, 2])],
    (8, 4): []
}
param_weights = [0.2, 0.2, 0.2, 0.2, 0.2]
start = (0, 0)
end = (8, 4)
no_fly_zones = [(4, 4)]
no_signal_areas = [(5, 5)]
max_radius = 10



def get_current_path_data():
    top_k_paths = k_shortest_paths(start, end, graph, param_weights, no_fly_zones, no_signal_areas, max_radius, k=5)
    print("Top 6 optimized paths:")
    for i, path in enumerate(top_k_paths):
        print(f"Path {i+1}: {path}")
    return md.calculated_path
