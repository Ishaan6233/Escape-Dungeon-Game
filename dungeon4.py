'''
Implement: Displaying map with nice Unicode characters,
Checking the win condition (whether the player reached the finish),
Showing help.
Author: Ishaan Meena
When: 15/11/22
'''

MAP_FILE = 'cave_map.txt'


def load_map(map_file: str) -> list[list[str]]:
    """
    Loads a map from a file as a grid (list of lists)
    """
    grid = []
    with open(map_file, 'r') as file:
        file_data = file.readlines()
        for row_index in file_data:
            rows = []
            for column_index in row_index:
                if column_index != '\n':
                    rows.append(column_index)
            grid.append(rows)
    return grid


def find_start(grid: list[list[str]]) -> list[int, int]:
    """
    Finds the starting position of the player on the map.
    """
    row_counter = 0
    for row_index in grid:
        column_counter = 0
        for column_index in row_index:
            if column_index == 'S':
                return [row_counter, column_counter]
            column_counter += 1
        row_counter += 1


def get_command() -> str:
    """
    Gets a command from the user.
    """
    user_input = input("Enter 'escape' to quit/ 'show map' to display/'help' : ")
    return user_input


def display_map(grid: list[list[str]], player_position: list[int, int]) -> None:
    """
    Displays the map.
    """
    return_grid = ''
    row_counter = 0
    for row_index in grid:
        column_counter = 0
        for column_index in row_index:
            if column_index == 'S':  # if position is 'S'
                column_index = '\U0001F3E0'  # Starting position is assigned a House emoji
            elif (row_counter == player_position[0]) and (column_counter == player_position[1]):
                column_index = '\U0001F934'  # Current position is assigned a Person emoji
            elif column_index == '*':
                column_index = '\U0001F7E2'  # Green Dot
            elif column_index == '-':
                column_index = '\U0001F9F1'  # Brick Wall
            elif column_index == 'F':
                column_index = '\U0001F3FA'  # Trophy
            return_grid += column_index
            column_counter += 1
        return_grid += '\n'
        row_counter += 1
    print(return_grid)


def get_grid_size(grid: list[list[str]]) -> list[int, int]:
    """
    Returns the size of the grid.
    """
    return [len(grid), len(grid[0])]


def is_inside_grid(grid: list[list[str]], position: list[int, int]) -> bool:
    """
    Checks if a given position is valid (inside the grid).
    """
    grid_rows, grid_cols = get_grid_size(grid)
    valid = False
    if ((position[0] + 1 <= grid_rows) and (position[0] >= 0)) and (position[1] + 1 <= grid_cols) and (
            position[1] >= 0):
        valid = True
    return valid


def look_around(grid: list[list[str]], player_position: list[int, int]) -> list:
    """
    Returns the allowed directions.
    """
    allowed_objects = ('S', 'F', '*')
    row = player_position[0]
    col = player_position[1]
    directions = []
    if is_inside_grid(grid, [row - 1, col]):
        if grid[row - 1][col] in allowed_objects:
            directions.append('north')
    if is_inside_grid(grid, [row + 1, col]):
        if grid[row + 1][col] in allowed_objects:
            directions.append('south')
    if is_inside_grid(grid, [row, col + 1]):
        if grid[row][col + 1] in allowed_objects:
            directions.append('east')
    if is_inside_grid(grid, [row, col - 1]):
        if grid[row][col - 1] in allowed_objects:
            directions.append('west')
    return directions


def move(direction: str, player_position: list[int, int], grid: list[list[str]]) -> bool:
    """
    Moves the player in the given direction.
    """
    grid_directions = look_around(grid, player_position)
    moved = True
    if direction in grid_directions:
        if direction == 'north':
            player_position[0] = player_position[0] - 1
        elif direction == 'south':
            player_position[0] = player_position[0] + 1
        elif direction == 'east':
            player_position[1] = player_position[1] + 1
        elif direction == 'west':
            player_position[1] = player_position[1] - 1
    else:
        moved = False
    return moved


def check_finish(grid: list[list[str]], player_position: list[int, int]) -> bool:
    """
    Checks if the player has reached the exit.
    """
    row_num = 0
    for row in grid:
        column_num = 0
        for column in row:
            if column == 'F' or column == '\U0001F934':
                end = [row_num, column_num]
            column_num += 1
        row_num += 1
    if player_position == end:
        return True
    return False


def display_help() -> None:
    """
    Displays a list of commands.
    """
    with open('help.txt', 'r') as helpfile:
        print(helpfile.read())


def main():
    """
    Main entry point for the game.
    """
    grid = load_map(MAP_FILE)
    current_pos = find_start(grid)
    display_map(grid, current_pos)

    while True:
        directions = look_around(grid, current_pos)

        directions_to_go = ''
        for i in directions:
            directions_to_go += f'{i} '
        print(f'You can go {directions_to_go}')
        direction_input = input('Enter Desired direction: ')[3:].strip()
        if direction_input in directions:
            result = move(direction_input, current_pos, grid)
            if result:
                print(f'Moved {direction_input}.')
        elif direction_input in ['north', 'south', 'east', 'west']:
            print('You can not go there')

        if check_finish(grid, current_pos):
            print('Congratulations you reached the exit!')
            break

        user_input = get_command().lower()
        if user_input == 'escape':
            break
        elif user_input == 'show map':
            display_map(grid, current_pos)
        elif user_input == 'help':
            with open('help.txt', 'r') as file:
                print(file.read())
        else:
            print('I do not Understand')


if __name__ == '__main__':
    main()
