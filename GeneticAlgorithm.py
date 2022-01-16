from Maze import Maze
import random

from NeuralNetwork import DEAD_END_ALL_SIDE_SN, CORRIDOR_ALL_SIDE_SN

def slice_3x3_matrix(mat: list[list], i: int, j: int):
    return [
        mat[i][j:j+3],
        mat[i+1][j:j+3],
        mat[i+2][j:j+3]
    ]

DEAD_END_VALUE = 1
CORRIDOR_VALUE = 0.5
BLOCK_CELL_VALUE = 0.5

def pass_thru_maze(maze: Maze) -> int:
    values_sum: float = 0
    
    for y in range(len(maze.maze) - 2):
        for x in range(len(maze.maze[0]) - 2):
            pass_window = slice_3x3_matrix(maze.maze, y, x)
            
            has_dead_end = DEAD_END_ALL_SIDE_SN.infer(pass_window)
            has_corridor = CORRIDOR_ALL_SIDE_SN.infer(pass_window)
    
            values_sum += int(has_dead_end) * DEAD_END_VALUE + int(has_corridor) * CORRIDOR_VALUE

    return values_sum

def fitness(maze: Maze) -> int:
    fit_value = 0
    max_path = maze.is_valid()
    
    if max_path == 0:
        fit_value -= maze.width * maze.height
        
    fit_value += max_path
    
    patterns_values = pass_thru_maze(maze)
    
    for line in maze.maze:
        for value in line:
            if value == 1:
                fit_value += BLOCK_CELL_VALUE
    
    return fit_value + patterns_values

def crossover(maze1: Maze, maze2: Maze) -> tuple[Maze, Maze]:
    assert maze1.height == maze2.height
    assert maze1.width == maze2.width
    
    # max_len = maze1.width * maze1.height
    point = random.choice(range(maze1.height))
    
    ret_maze1 = maze1.maze[:point] + maze2.maze[point:]
    ret_maze1 = Maze(ret_maze1)
    
    ret_maze2 = maze2.maze[:point] + maze1.maze[point:]
    ret_maze2 = Maze(ret_maze2)
    
    return (ret_maze1, ret_maze2)

def mutate(maze: Maze, prob=0.3):
    for y in range(maze.height):
        for x in range(maze.width):
            if random.uniform(0, 1) <= prob:
                val = maze.maze[y][x]
                if val == 0 or val == 1:
                    maze.maze[y][x] = int(not bool(val))

def gen_matrix(height: int, width: int) -> list[list[int]]:
    result_matrix = []
    row_list = [0] * width
    
    for _ in range(height):
        result_matrix.append(row_list.copy())    
    
    return result_matrix

def gen_init_pop(start_maze: Maze, num_pop: int, mutate_rate: float = 0.3):
    start_population = []
    
    for _ in range(num_pop):
        new_maze = start_maze.copy()
        mutate(new_maze, mutate_rate)
        start_population.append(new_maze)
    
    for maze in start_population:
        maze.color_points()
    
    return start_population

def run(
    num_population: int, num_elite: int, generations: int,
    mutation_rate: float, shape: tuple[int, int] = (4,4),
    verbose: bool = False, quantity: int = 1
):
    assert quantity <= generations
    
    steps = generations // quantity
    total = steps * quantity
    
    start_maze = Maze(gen_matrix(*shape))
    initial_pop = gen_init_pop(start_maze, num_population, 0.3)
    
    best_ret_mazes = []
    
    population = initial_pop
    
    for gen in range(1, generations - (generations - total) + 1):
        scored_mazes = []
        for maze in population:
            score = fitness(maze)
            scored_mazes.append((score, maze))
        
        scored_mazes.sort(key=lambda x: x[0])
        scored_mazes.reverse()
        
        if verbose:
            print('#### The best maze was ####')
            print(f'Score: {scored_mazes[0][0]},\n{scored_mazes[0][1]}')
            print('############\n')
        if gen % steps == 0:
            best_ret_mazes.append(scored_mazes[0][1])

        best_mazes = scored_mazes[:num_elite]

        new_generation = []
        for values in best_mazes:
            new_generation.append(values[1].copy())
        
        for _ in range(num_population//2 - num_elite):
            first_maze = random.choice(best_mazes)[1].copy()
            second_maze = random.choice(best_mazes)[1].copy()

            ret_maze = crossover(first_maze, second_maze)
            
            for maze in ret_maze:
                mutate(maze, mutation_rate)
            
            new_generation.extend(ret_maze)

        population = new_generation

    return best_ret_mazes


if __name__ == '__main__':
    simple_maze = Maze([[-2, 0, 0,  0],
                        [ 0, 0, 0,  1],
                        [ 0, 1, 1, -1],
                        [ 0, 0, 0,  0]])
    
    fit_val = fitness(simple_maze)
    assert fit_val == 8.5
    
    for i in range(1, 20):
      mazes = run(100, 10, 20, 0.1, quantity=i)
      
      assert i == len(mazes)
    
    maze1 = Maze([[1,1], [1,1]])
    maze2 = Maze([[0,0], [0,0]])
    maze1.color_points()
    maze2.color_points()
    
    aaa1, aaa2 = crossover(maze1, maze2)
    print(aaa1)
    print(aaa2)
    
    mutate(maze1)
    print(maze1)
    
    print(fitness(maze1))
    print(fitness(maze2))
    print(fitness(aaa1))
    print(fitness(aaa2))