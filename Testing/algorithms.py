from heapq import heappush, heappop
from queue import PriorityQueue

class Algorithm:
    def __init__(self, name):
        self.name = name
        

    def dfs(self, grid, start, end , visited=None, draw_function=None):
        if visited is None:
            visited = []
            
        visited.append(start)
        
       
        if start == end:
            # return f"Found: {start}, Visited nodes: {visited}"
            return visited.copy()
        
        for neighbor in self.get_neighbors(start, grid):
            if neighbor not in visited:
                if neighbor != start and neighbor != end:
                    grid[neighbor[0]][neighbor[1]] = "visited"
                    if draw_function:
                        draw_function()
                result = self.dfs(grid, neighbor, end, visited, draw_function)
                if result:
                    return result
        
        # return "DFS algorithm implemented"
    # https://www.youtube.com/watch?v=xlVX7dXLS64&t=45s
    
    # def bfs(self, grid, start, end, Visited=None, queue=None):
    #     if Visited is None:
    #         Visited = []
    #     # return "BFS algorithm implemented"
    #     queue = [start]
    #     while len(queue) > 0:
    #         current = queue.pop(0)
    #         Visited.append(current)
    #         if current == end:
    #             return Visited.copy()
            
    #         for neighbor in self.get_neighbors(current, grid):
    #             if neighbor not in Visited and neighbor not in queue:
    #                 queue.append(neighbor)
    def bfs(self, grid, start, end, draw_function):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = [start]
        previous = {}
        
        def get_neighbors(pos):
            r, c = pos
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] != "wall":
                        yield (nr, nc)
        while queue:
            current = queue.pop(0)
            visited.add(current)
            
            if current != start and current != end:
                grid[current[0]][current[1]] = "visited"
                draw_function()
            
            if current == end:
                path = []
                while current in previous:
                    path.append(current)
                    current = previous[current]
                path.append(start)
                path.reverse()
                return path, visited
            
            for neighbor in get_neighbors(current):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    previous[neighbor] = current
        return [], visited  
    
    def dijkstra(self, grid, start, end, draw_function):
        # return "Dijkstra's algorithm implemented"
        rows, cols = len(grid), len(grid[0])
        distances = { (r, c): float("inf") for r in range(rows) for c in range(cols) }
        distances[start] = 0
        previous = {}
        visited = set()
        heap = [(0, start)]
        
        def get_neighbors(r, c):
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] != "wall":
                        yield (nr, nc)
                        
        while heap:
            dist, current = heappop(heap)
            if current in visited:
                continue
            visited.add(current)
            
            if current != start and current != end:
                grid[current[0]][current[1]] = "visited"
                draw_function()

            if current == end:
                path = []
                while current in previous:
                    path.append(current)
                    current = previous[current]
                path.append(start)
                path.reverse()
                return path, visited

            for neighbor in get_neighbors(*current):
                if neighbor in visited:
                    continue
                new_dist = dist + 1
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
                    heappush(heap, (new_dist, neighbor))

        return [],visited  # No path found
        
    
    def a_star(self, grid, start, end ,draw_function):
        # return "A* algorithm implemented"
        rows, cols = len(grid), len(grid[0])
        count = 0
        def h(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)
        
        open_set = PriorityQueue()
        open_set.put((0, count, start))
        g_score = {(r, c): float("inf") for r in range(rows) for c in range(cols)}
        g_score[start] = 0
        f_score = {(r, c): float("inf") for r in range(rows) for c in range(cols)}
        f_score[start] = h(start, end)
        
        visited = set()
        came_from = {}
        open_set_hash = {start}
        
        def get_neighbors(r, c):
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] != "wall":
                        yield (nr, nc)
                        
        while not open_set.empty():
            
            current = open_set.get()[2]
            open_set_hash.remove(current)
            visited.add(current)
            # visited.remove(current)
            
            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path, visited
            
            for neighbor in  get_neighbors(*current):
                temp_g_score = g_score[current] + 1
                
                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + h(neighbor, end)
                    if neighbor not in open_set_hash:
                    # if neighbor not in visited:
                        count += 1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        # visited.add(neighbor)
                        
                        if neighbor != start and neighbor != end:
                            grid[neighbor[0]][neighbor[1]] = "visited"
                            
                        draw_function()
            
        return [], visited
    
    
    
    # https://www.youtube.com/watch?v=KiCBXu4P-2Y&t=44s
    def get_neighbors(self, pos, grid):
        row, col = pos
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]  
        neighbors = []

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] != "wall":
                    neighbors.append((r, c))

        return neighbors
    