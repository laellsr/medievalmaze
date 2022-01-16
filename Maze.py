class Maze:
    def __init__(
        self, 
        maze: list, 
        start: tuple = (0,0),
        end: tuple = (0,0)
    ):
        self.maze = maze
        self.height = len(maze)
        self.width = len(maze[0])

        self.start_pos = (0,0)
        if start != (0,0):
            self.start_pos = start
        if end != (0,0):
            self.end_pos = end
        else:
            self.end_pos = (self.height//2, self.width-1)

    def color_points(self):
        self.maze[self.start_pos[0]][self.start_pos[1]] = -2
        self.maze[self.end_pos[0]][self.end_pos[1]] = -1

    def print_maze(self):
        for line in self.maze:
            print(line)
    
    def get_pos(self, graph_value):
        x = graph_value % self.width
        y = graph_value // self.width

        return self.maze[y][x]
    
    def generate_graph(self):
        graph = []
        
        for y in range(self.height):
            for x in range(self.width):
                if self.maze[y][x] == 1:
                    graph.append([])
                    continue
                
                current_pos = y * self.width + x
                
                up = (y - 1) * self.width + x
                right = y * self.width + x + 1
                left = y * self.width + x - 1
                down = (y + 1) * self.width + x
                
                append_value = []
                
                if y != 0 and self.get_pos(up) != 1:
                    append_value.append(up)
                
                if x != 0 and self.get_pos(left) != 1:
                    append_value.append(left)
                
                if y != self.height-1 and self.get_pos(down) != 1:
                    append_value.append(down)
                    
                if x != self.width-1 and self.get_pos(right) != 1:
                    append_value.append(right)
                
                graph.append(append_value)
        
        return graph

    def __iter__(self):
        return iter(self.maze)

    def __str__(self):
        ret_str = ''
        for line in self.maze:
            ret_str += str(line) + '\n'
        return ret_str[:-1]

    def copy(self):
        ret_matrix = []
        for line in self.maze:
            ret_matrix.append(line[:])
        return Maze(ret_matrix)

    # Standard DFS with depth caching
    def dfs(self, graph, vert, depths):
        visited = [False] * self.width * self.height
        
        stack = [(vert, 1)]
        
        while (len(stack)):
            s, depth = stack.pop()
            
            if not visited[s]:
                visited[s] = True
            
            for child in graph[s]:
                if self.get_pos(child) == -1:
                    depths.append(depth)
                    break
                
                if not visited[child]:
                    stack.append((child, depth+1))
    
    # Standard BFS with depth caching
    def bfs(self, graph, vert, depths):
        visited = [False] * self.width * self.height
        visited[vert] = True
        
        queue = [(vert, 1)]
        depth = 1
        
        while len(queue):
            s, depth = queue.pop(0)
            
            for child in graph[s]:
                if not visited[child]:
                    if self.get_pos(child) == -1:
                        depths.append(depth)
                        break

                    queue.append((child, depth+1))
                    visited[child] = True
        
    
    # It returns 0 if the maze is invalid
    def is_valid(self):
        graph = self.generate_graph()
        
        depths = []
        start_vert = self.start_pos[0] * self.width + self.start_pos[1]
        
        self.bfs(graph, start_vert, depths)
        
        if depths == []:
            ret_value = 0
        else:
            ret_value = min(depths)
                    
        return ret_value
        

if __name__ == '__main__':
    test_maze = Maze([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ])

    assert test_maze.width == 3
    assert test_maze.height == 3

    test_maze.color_points()
    assert test_maze.maze == [[-2, 0, 0], [0, 0, -1], [0, 0, 0]]

    graph = test_maze.generate_graph()

    # for line in [[0, 1, 2],[3, 4, 5], [6, 7, 8]]:
    #     print(line)
    assert graph == [[3, 1], [0, 4, 2], [1, 5], [0, 6, 4], [1, 3, 7, 5], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]
    
    assert test_maze.is_valid() == 3
    
    assert Maze([[0,0,0],[0,0,0],[0,0,0]]).is_valid() == 0
    
    test_maze.maze[1][1] = 1
    assert test_maze.is_valid() == 3
    
    test_maze.maze[0][1] = 1
    assert test_maze.is_valid() == 5