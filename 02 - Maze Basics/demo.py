from pyamaze import maze, COLOR, agent, textLabel

m = maze(15, 20)
m.CreateMaze(2, 2, theme='light')

a = agent(m, 5, 5, shape='square', footprints=True, color=COLOR.red, filled=True)

m.markCells = [(5, 2), (5, 9), (5, 1), (9, 2), (9, 3), (10, 1)]

m.tracePath({a: m.path}, delay=100, showMarked=True, kill=True)

label1 = textLabel(m, "Total Cells", m.rows * m.cols)

m.run()