# Point is tuple (x, y)
# Grid is 2d list
# Point guaranteed to be within bounds
def pt_in_grid(point, grid):
    x_index = 0
    y_index = 1
    return grid[point[x_index]][point[y_index]]

# Main
with open("input.txt") as file:
    grids = int(file.readline())
    for test_case in range(grids):
        print("Test Case#", test_case + 1)

        rows = int(file.readline())
        grid = []
        for _ in range(rows):
            grid.append([int(bit)
                         for bit in file.readline().strip().split(" ")])

        l_count = n_count = u_count = 0
    
        # L if all are 1 in 3x3
        L_ROTATIONS = [
            [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
            [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)],
            [(0, 2), (1, 2), (2, 2), (2, 0), (2, 1)],
        ]

        # N if all are 0 in 3x3
        N_ROTATIONS = [
            [(0, 1), (2, 1)],
            [(1, 0), (1, 2)]
        ]

        # U if (1, 1) and point are 0 in 3x3
        center = (1, 1)
        U_NEIGHBORS = [(0, 1), (2, 1), (1, 2), (1, 0)]

        # Loop through entire grid, one 3x3 section at a time
        for x in range(len(grid) - 2):
            for y in range(len(grid[0])- 2):
                grid_to_check = [
                    [grid[x]  [y], grid[x]  [y+1], grid[x]  [y+2]],
                    [grid[x+1][y], grid[x+1][y+1], grid[x+1][y+2]],
                    [grid[x+2][y], grid[x+2][y+1], grid[x+2][y+2]]
                ]

                points_to_check = [(X, Y) for X in range(3) for Y in range(3)]

                L_FOUND = any([
                    all(pt_in_grid(point, grid_to_check) == 1 if point in rotation else pt_in_grid(point, grid_to_check) == 0
                    for point in points_to_check)
                for rotation in L_ROTATIONS])

                N_FOUND = any([
                    all(pt_in_grid(point, grid_to_check) == 0 if point in rotation else pt_in_grid(point, grid_to_check) == 1
                    for point in points_to_check)
                for rotation in N_ROTATIONS])

                U_FOUND = any([
                    all(pt_in_grid(point, grid_to_check) == 0 if point in [center, neighbor] else pt_in_grid(point, grid_to_check) == 1
                    for point in points_to_check)
                for neighbor in U_NEIGHBORS])

                l_count = l_count + (1 if L_FOUND else 0)
                n_count = n_count + (1 if N_FOUND else 0)
                u_count = u_count + (1 if U_FOUND else 0)

        print("L-count", l_count)
        print("N-count", n_count)
        print("U-count", u_count)

