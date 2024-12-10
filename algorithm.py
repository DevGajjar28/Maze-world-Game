from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue


def DFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    dfsPath = {}
    dSearch = []
    while len(frontier) > 0:
        currCell = frontier.pop()
        dSearch.append(currCell)
        if currCell == m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    child = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    child = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    child = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    child = (currCell[0] + 1, currCell[1])
                if child in explored:
                    continue
                explored.append(child)
                frontier.append(child)
                dfsPath[child] = currCell
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return dSearch, dfsPath, fwdPath


def aStar(m, start=None):
    if start is None:
        start = (m.rows, m.cols)
    open = PriorityQueue()
    open.put((h(start, m._goal), h(start, m._goal), start))
    aPath = {}
    g_score = {row: float("inf") for row in m.grid}
    g_score[start] = 0
    f_score = {row: float("inf") for row in m.grid}
    f_score[start] = h(start, m._goal)
    searchPath = [start]
    while not open.empty():
        currCell = open.get()[2]
        searchPath.append(currCell)
        if currCell == m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])

                temp_g_score = g_score[currCell] + 1
                temp_f_score = temp_g_score + h(childCell, m._goal)

                if temp_f_score < f_score[childCell]:
                    aPath[childCell] = currCell
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = temp_f_score
                    open.put((f_score[childCell], h(childCell, m._goal), childCell))

    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    return searchPath, aPath, fwdPath


def h(cell1, cell2):
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)


def runDFS(m):
    start = (m.rows, m.cols)
    dSearch, dfsPath, fwdPath = DFS(m, start)
    a = agent(m, *start, footprints=True, shape='square', color=COLOR.green)
    b = agent(m, *m._goal, goal=start, footprints=True, filled=True)
    c = agent(m, *start, footprints=True, color=COLOR.yellow)
    m.tracePath({a: dSearch}, showMarked=True)
    m.tracePath({b: dfsPath})
    m.tracePath({c: fwdPath})


def runAStar(m):
    start = (m.rows, m.cols)
    searchPath, aPath, fwdPath = aStar(m, start)
    a = agent(m, *start, footprints=True, color=COLOR.blue, filled=True)
    b = agent(m, *m._goal, footprints=True, color=COLOR.yellow, filled=True, goal=start)
    c = agent(m, *start, footprints=True, color=COLOR.red)
    m.tracePath({a: searchPath}, delay=300)
    m.tracePath({b: aPath}, delay=300)
    m.tracePath({c: fwdPath}, delay=300)


def chooseAlgorithm(algorithm, m):
    if algorithm == 1:
        runDFS(m)
    elif algorithm == 2:
        runAStar(m)
    else:
        print("Invalid choice!")
