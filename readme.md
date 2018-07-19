# Sudoku Generator

Simple sudoku generator.

# Usage

Example:

```python
from sudoku import print_grid, generate_grid, generate_placeholders_single_solution, compute_solutions

a = generate_grid()
b = generate_placeholders_single_solution(a)
print_grid(a)
print_grid(b)
(s,) = compute_solutions(b)
s == a
```

![example](https://user-images.githubusercontent.com/5585520/42964801-69bb4de8-8b98-11e8-9a89-d7c412c4a940.png)
