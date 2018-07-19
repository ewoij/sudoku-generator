import random

def get_constraint_indices_line(n):
    lb = int(n / 9) * 9
    return [lb + c for c in range(9)]

def get_constraint_indices_column(n):
    c = n % 9
    return [l * 9 + c for l in range(9)]

def get_constraint_indices_square(n):
    gx, gy = int(n % 9 / 3), int(n / (9 * 3))
    return [l * 9 + c for l in range(gy * 3, gy * 3 + 3) for c in range(gx * 3, gx * 3 + 3)]

def get_constraint_indices(n):
    indices = set(
        get_constraint_indices_line(n) +
        get_constraint_indices_column(n) +
        get_constraint_indices_square(n))
    indices.remove(n)
    return indices

def get_possibilites(grid, n):
    cis = get_constraint_indices(n)
    constraints = set(grid[ci] for ci in cis if ci < len(grid))
    return list(set(range(1, 9 + 1)) - constraints)

def generate_grid(grid = []):
    n = len(grid)
    if n == 81: return grid
    ps = get_possibilites(grid, n)
    random.shuffle(ps)
    for p in ps:
        g = generate_grid(grid + [p])
        if g:
            return g
    return None

def print_grid(grid):
    for i in range(81):
        if i > 0 and i % 9 != 0 and i % 3 == 0:
            print(' |', end='')
        if i % 9 == 0:
            print()
            if i > 0 and i % (3 * 9) == 0:
                print('-' * (9 * 2 + 2 * 2 + 1))
        value = grid[i] if i < len(grid) and grid[i] is not None else ''
        print('{:2}'.format(value), end='')
    print()

def generate_placeholders_single_solution(grid):
    grid = grid.copy()
    indices = [n for n, v in enumerate(grid) if v is not None]
    random.shuffle(indices)
    for i in indices:
        value = grid[i]
        grid[i] = None
        solutions = compute_solutions(grid)
        if len(solutions) > 1:
            grid[i] = value
    return grid

def compute_solutions(grid):
    empty_cells = [n for n, v in enumerate(grid) if v is None]
    if not empty_cells:
        return [grid]
    n, ps = min(((n, get_possibilites(grid, n)) for n in empty_cells), key=lambda i: len(i[1]))
    grid = grid.copy()
    solutions = []
    for p in ps:
        grid[n] = p
        solutions += compute_solutions(grid)
    return solutions
