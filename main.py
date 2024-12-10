from pyamaze import maze
from algorithm import chooseAlgorithm

if __name__ == '__main__':
    print("Choose an algorithm to solve the maze:")
    print("1. Depth-First Search (DFS)")
    print("2. A* Search")
    choice = int(input("Enter your choice (1 or 2): "))

    m = maze(10, 10)  # Adjust maze size if needed
    m.CreateMaze(1, 1)  # Change the goal cell here if needed

    chooseAlgorithm(choice, m)
    m.run()
