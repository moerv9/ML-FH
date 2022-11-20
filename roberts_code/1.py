import matplotlib.pyplot as plt
import numpy as np
from random import randrange
import math

import time

gridsize = 10
grid = np.zeros((gridsize, gridsize), dtype=float)
explorerate = 0.5
ignoreexplorethreshold = 0.75
rewardrate = 1.2
targetx = int(randrange((gridsize - 1)))
targety = int(randrange((gridsize - 1)))
stepsongoing = 0
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
while True:
    _gridcolors = np.full((gridsize, gridsize), "w")
    gridcolors = _gridcolors.tolist()
    posx = int(randrange((gridsize - 1)))
    posy = int(randrange((gridsize - 1)))
    sx = posx
    sy = posy

    print("Iteration " + str(stepsongoing))
    # sessiongrid = np.zeros(gridsize,gridsize)
    route = []
    s = 0
    nosolfound = False
    laststep = -1
    while True:
        _tempgridcolors = np.full((gridsize, gridsize), "w")
        tempgridcolors = _tempgridcolors.tolist()
        tcx = "--Steps " + str(s) + " x: " + str(posx) + " y: " + str(posy)
        print(tcx, end="\r")
        s = s + 1
        if s > 100000:
            nosolfound = True
            print("--No Way Found or Bugged out")
            break
        if int(targetx) == int(posx) and int(targety) == int(posy):
            break
        bestfield = -1
        bestx = 0
        besty = 0
        dir = []
        # 1 left  2 up   3 right     4 down
        if posx > 0:
            if bestfield < grid[posx - 1, posy]:
                bestfield = grid[posx - 1, posy]
                bestx = posx - 1
                besty = posy
            dir.append(1)
            laststep = 1
        if posx < gridsize - 1:
            if bestfield < grid[posx + 1, posy]:
                bestfield = grid[posx + 1, posy]
                bestx = posx + 1
                besty = posy
            dir.append(3)
            laststep = 3
        if posy > 0:
            if bestfield < grid[posx, posy - 1]:
                bestfield = grid[posx, posy - 1]
                bestx = posx
                besty = posy - 1
            dir.append(4)
            laststep = 4
        if posy < gridsize - 1:
            if bestfield < grid[posx, posy + 1]:
                bestfield = grid[posx, posy + 1]
                bestx = posx
                besty = posy + 1
            dir.append(2)
            laststep = 2
        randexplore = randrange(1)
        if randexplore <= explorerate:
            lenth = len(dir)
            # print(lenth)
            choosendir = dir[int(randrange(lenth))]
            if choosendir == 1:
                posx = posx - 1
                posy = posy
            if choosendir == 2:
                posx = posx
                posy = posy + 1
            if choosendir == 3:
                posx = posx + 1
                posy = posy
            if choosendir == 4:
                posx = posx
                posy = posy - 1
        else:
            posy = besty
            posx = bestx
        route.append([posx, posy])
        """Path animation extrem langsam -.-
        for p in route:
            tempgridcolors[p[0]][p[1]] = "b"
        tempgridcolors[posx][posy] = "r"
        tempgridcolors[sx][sy] = "c"
        tempgridcolors[targetx][targety] = "m"
        data = grid.tolist()
        colums = []
        rows = []
        for i in range(0,gridsize):
            x = str(i)+"X"
            y = str(i)+"Y"
            colums.append(x)
            rows.append(y)
        table = ax.table(cellText=data,rowLabels=rows,cellColours=tempgridcolors,colLabels=colums, loc='top',bbox=[0.0,0.0,1,1])
        fig.tight_layout()
        #fig.canvas.draw()
        table.auto_set_font_size(False)
        table.set_fontsize(7)
        fig.canvas.draw()
        fig.canvas.flush_events()
       # input()
       """
    route.reverse()

    if nosolfound:
        continue
    c = 1
    i = 1
    for p in route:
        grid[p[0], p[1]] = round((grid[p[0], p[1]] + 1 / math.pow(rewardrate, i)), 2)
        gridcolors[p[0]][p[1]] = (0, c, 1 - c)
        c = i / (len(route) - 1)
        i = i + 1
    data = grid.tolist()

    colums = []
    rows = []
    for i in range(0, gridsize):
        x = str(i) + "X"
        y = str(i) + "Y"
        colums.append(x)
        rows.append(y)
    stepsongoing = stepsongoing + 1
    # plt.table(cellText=data,rowLabels=rows,colLabels=colums)
    # plt.show()
    gridcolors[targetx][targety] = "m"
    gridcolors[sx][sy] = "y"

    # hide axes
    # fig.patch.set_visible(False)
    # ax.axis('off')
    # ax.axis('tight')
    table = ax.table(
        cellText=data,
        rowLabels=rows,
        cellColours=gridcolors,
        colLabels=colums,
        loc="top",
        bbox=[0.0, 0.0, 1, 1],
    )
    fig.tight_layout()
    # fig.canvas.draw()
    table.auto_set_font_size(False)
    table.set_fontsize(7)
    fig.canvas.draw()
    fig.canvas.flush_events()
    input()
