import matplotlib.pyplot as plt
from datapoint import DataPoint as dp
from random import uniform as rand
import math

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

def mplot(points = [], join = 0, cluster = 0):
    if not points: return
    colmap = {}
    xmap = {}
    ymap = {}

    for a in points:
        temp = a.cluster
        
        if not temp in colmap: colmap[temp] = int(rand(0, len(colors)-1e-9))
            
        if temp in xmap:
            xmap[temp][0] = max(a.x, xmap[temp][0])
            xmap[temp][1] = min(a.x, xmap[temp][1])
        else:
            xmap[temp] = [a.x, a.x]

        if temp in ymap:
            ymap[temp][0] = max(a.y, ymap[temp][0])
            ymap[temp][1] = min(a.y, ymap[temp][1])
        else:
            ymap[temp] = [a.y, a.y]
    
    x = [point.x for point in points]
    y = [point.y for point in points]
    cols = [colors[colmap[point.cluster]] for point in points]

    fig, ax = plt.subplots()

    if cluster:
        for key in colmap:       
            cenx = (xmap[key][0] + xmap[key][1])/2
            ceny = (ymap[key][0] + ymap[key][1])/2
            circle = plt.Circle((cenx, ceny), radius = max(xmap[key][0]-xmap[key][1], ymap[key][0]-ymap[key][1])/math.sqrt(2), edgecolor = colors[colmap[key]], facecolor = 'none')
            ax.add_patch(circle)
    
    plt.scatter(x, y, c = cols, s = 2)

    tot = len(points)
    if join:
        for i in range(tot):
            ax.plot((points[i].x, points[(i+1)%tot].x), (points[i].y, points[(i+1)%tot].y), color = colors[colmap[points[i].cluster]], linewidth = 1)
    
    plt.show()