from pyamaze import maze, agent, COLOR

def DFS(m):
    start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]

    dfsPath = {}

    while len(frontier) > 0:
        currentCell = frontier.pop()

        if currentCell == (1, 1):
            break

        for direction in 'ESNW':
            if m.maze_map[currentCell][direction] == True:
                if direction == 'E':
                    childCell = (currentCell[0], currentCell[1] + 1)
                elif direction == 'W':
                    childCell = (currentCell[0], currentCell[1] - 1)
                elif direction == 'S':
                    childCell = (currentCell[0] + 1, currentCell[1])
                elif direction == 'N':
                    childCell = (currentCell[0] - 1, currentCell[1])

                if childCell in explored:
                    continue

                explored.append(childCell)
                frontier.append(childCell)

                dfsPath[childCell] = currentCell


    forwardPath = {}
    cell = (1, 1)

    while cell != start:
        forwardPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]

    return forwardPath

if __name__ == '__main__':
    m = maze(25, 25)
    m.CreateMaze(loopPercent=100)
    path = DFS(m)

    a = agent(m, footprints=True)
    m.tracePath({a: path})

    m.run()