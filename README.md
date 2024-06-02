# Escape-Dungeon-Game
This project is a basic text-based adventure game where the player navigates through a grid map, starting from a designated start point 'S' and aiming to reach the finish point 'F'. The game includes several features, such as displaying the map with Unicode characters, checking the win condition, and providing help information.

## Game Features
### Displaying Map with Unicode Characters:

The map is displayed using Unicode characters for better visualization:
Starting position: 🏠 (House emoji)
Current player position: 🤴 (Person emoji)
Walkable path: 🟢 (Green Dot)
Wall/obstacle: 🧱 (Brick Wall)
Finish/goal: 🏺 (Trophy)

### Checking the Win Condition:
The game checks whether the player has reached the finish point 'F'.
If the player reaches the finish point, a congratulatory message is displayed, and the game ends.

To run the game, simply execute the script. The game will load the map from cave_map.txt and prompt the player for commands to navigate the map. The player can use commands such as 'north', 'south', 'east', 'west' to move, 'show map' to display the map, and 'help' to display the list of commands.
