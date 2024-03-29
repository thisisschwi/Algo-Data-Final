import heapq

graph = {
    'A': {'B': 6, 'F': 5},
    'B': {'G': 6, 'C': 5, 'A': 6},
    'F': {'J': 7, 'G': 8, 'A': 5},
    'G': {'K': 8, 'H': 9, 'B': 6, 'F': 8},
    'C': {'H': 5, 'D': 7, 'B': 5},
    'J': {'O': 7, 'K': 5, 'F': 7},
    'O': {'S': 9, 'P': 13, 'J': 7},
    'K': {'L': 7, 'G': 8, 'J': 5},
    'H': {'I': 12, 'G': 9, 'C': 5},
    'D': {'I': 8, 'E': 7, 'C': 7},
    'S': {'T': 9, 'O': 9},
    'P': {'U': 11, 'Q': 8, 'O': 13, 'L': 7},
    'L': {'P': 7, 'M': 7, 'K': 7},
    'T': {'U': 8, 'S': 9},
    'I': {'M': 10, 'H': 12, 'D': 8, 'E': 6},
    'E': {'I': 6, 'N': 15, 'D': 7},
    'M': {'N': 9, 'L': 7, 'I': 10},
    'N': {'R': 7, 'E': 15, 'M': 9},
    'Q': {'R': 9, 'P': 8},
    'R': {'W': 10, 'N': 7, 'Q': 9},
    'U': {'V': 8, 'P': 11, 'T': 8},
    'V': {'W': 5, 'U': 8},
    'W': {'R': 10, 'V': 5}
}

alphabet = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W'}


def dijkstra(graph, start):
    # Create distances dictionary to store shortest distances from start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Start the distance at 0
    # Initialize priority queue to store nodes to visit next
    pq = [(0, start)]
    predasessor = {}

    while pq:
        # Pop node with smallest distance from priority queue
        current_distance, current_node = heapq.heappop(pq)

        # Visit each neighbor of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:  # Update if new distance is shorter than old distance
                distances[neighbor] = distance
                # Store current hop as last visited
                predasessor[neighbor] = current_node
                # Add neighbor to priority queue with updated distance
                heapq.heappush(pq, (distance, neighbor))
                '''The following 2 print statements is just to show what's going on, remove if you dont want to see it.
                Simply all it is doing is going through the graph to each node via the shortest weight.
                It will check every way to get to every node and store the shortest way in a list.
                '''
                #print(predasessor)
                #print(distance)

    return distances, predasessor


def shortest_path_find(predasessor, start, end):
    # Start list to store the path from start to end
    path = []
    # Go from the end of the list back to the start and add each hop to the path list
    current_node = end
    while current_node != start:
        path.insert(0, current_node)
        current_node = predasessor[current_node]
    path.insert(0, start)
    return path

def check_charging_station(start_node):
    shortest_path = None # Set shortest path to none for now
    shortest_distance = float('inf') # Set distance to infinity
    location = '' # Set location to none for now
    charge_locations = ['H', 'K', 'Q', 'T'] # All charging locations
    # Calculate the shortest distance to each charging station from the given start point
    for end_node in charge_locations:
        distances, predecessors = dijkstra(graph, start_node)
        path = shortest_path_find(predecessors, start_node, end_node)
        distance = distances[end_node]

        # Keep track of the charging station closest to the start point with the distance and path to get there.
        if distance < shortest_distance:
            shortest_path = path
            shortest_distance = distance
            location = end_node
    print(f'Shortest distance from node, {start_node}, to the closest charging station: {location}, is: {shortest_distance} '
          f'and the path would be: {shortest_path}')



def main():
    while True:
        start_node = input('Enter starting node please: ')
        if start_node.isalpha() and start_node.upper() in alphabet:
            start_node = start_node.upper()
            check_charging_station(start_node)
            continue
        if start_node.isalpha() and start_node.upper() == 'STOP':
            break
        else:
            print('Error try again')
            continue


if __name__ == "__main__":
    main()
    input("Press Enter to exit...")