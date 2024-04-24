import heapq

def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    grid_size = tuple(map(int, lines[0].strip().split(',')))
    m, n = grid_size
    grid = [[0] * n for _ in range(m)]
    heights = [[0] * n for _ in range(m)]
    
    index = 1
    for i in range(m):
        for j in range(n):
            height, x, y = map(int, lines[index].strip().split(','))
            heights[x][y] = height
            index += 1

    source = tuple(map(int, lines[index].strip().split(',')))
    index += 1
    baths = []
    while index < len(lines):
        bath = tuple(map(int, lines[index].strip().split(',')))
        baths.append(bath)
        index += 1
    
    return m, n, heights, source, baths

def write_output(filename, path_length):
    with open(filename, 'w') as file:
        file.write(str(path_length))

def travel_time(heights, x1, y1, x2, y2):
    return max(-1, 1 + (heights[x2][y2] - heights[x1][y1]))

def min_cost_path(m, n, heights, source, baths):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    bath_set = set(baths)
    # Priority queue of (cost, x, y, visited_baths_mask)
    pq = [(0, source[0], source[1], 0)]
    dist = {(source[0], source[1], 0): 0}
    
    while pq:
        cost, x, y, visited_baths_mask = heapq.heappop(pq)
        
        # Check if we have visited all baths and are at a bath station
        if visited_baths_mask == (1 << len(baths)) - 1 and (x, y) in bath_set:
            return cost
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                next_cost = cost + travel_time(heights, x, y, nx, ny)
                next_mask = visited_baths_mask
                if (nx, ny) in bath_set:
                    bath_index = baths.index((nx, ny))
                    next_mask |= 1 << bath_index
                if (nx, ny, next_mask) not in dist or dist[(nx, ny, next_mask)] > next_cost:
                    dist[(nx, ny, next_mask)] = next_cost
                    heapq.heappush(pq, (next_cost, nx, ny, next_mask))
    
    return float('inf')

def solve_aqueduct_problem(input_filename, output_filename):
    m, n, heights, source, baths = read_input(input_filename)
    path_length = min_cost_path(m, n, heights, source, baths)
    write_output(output_filename, path_length)

solve_aqueduct_problem("grid.txt", "pathLength.txt")