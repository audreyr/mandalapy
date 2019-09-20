from scipy.spatial import Voronoi
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import pi

from helpers import voronoi_plot_2d

"""This function creates mandalas.
This is a Python port of Fronkonstin's R code: https://fronkonstin.com/2018/02/14/mandalas/
"""

f1,f2 = 10,10 #Figure size

def MandalaPy(it, points, radius):
    angles = np.linspace(0,2*pi*(1-1/points), points) + pi/2
    x,y = 0,0
    df = pd.DataFrame([[x,y]], columns = ['x','y']) #Initial center
    #Itearate over centers
    for k in range(it):
        t1 = np.array([])
        t2 = np.array([])
        for i in range(df.shape[0]):
            t1 = np.append(t1,df['x'][i]+radius**(k)*np.cos(angles))
            t2 = np.append(t2,df['y'][i]+radius**(k)*np.sin(angles))
        df = pd.DataFrame(np.column_stack((t1,t2)), columns = ['x','y'])
    mandala = Voronoi(df)
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0], fig_size[1] = f1,f2
    voronoi_plot_2d(mandala, show_points = False, show_vertices = False, line_width = 3), plt.axis('off'), plt.gca().set_aspect('equal', adjustable='box'), plt.savefig(f'mandala-{it}-{points}-{radius}.svg'), plt.savefig(f'mandala-{it}-{points}-{radius}.png', dpi = 100)
    return plt.show()

print(MandalaPy(it=4, points=5, radius=2))
print(MandalaPy(it=3, points=8, radius=8))
