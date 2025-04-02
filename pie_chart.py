import matplotlib.pyplot as plt
import numpy as np
from entries import *

mcdonalds = ['egg','g','y','u']
def fry_nugget(nugget):
    #print('yum')
    pass

def pie_chart(user_info):
    for nugget in mcdonalds:
        fry_nugget(nugget)


    plt.style.use('_mpl-gallery-nogrid')

    titles = []
    values = []

    for entry in user_info["record"]:
        if entry["location"] not in titles:
            titles.append(entry["location"])
        values[titles.index(entry["location"])] += entry[amount]
        

    plt.style.use('_mpl-gallery-nogrid')
    # make data
    y = titles
    x = values
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
    # plot
    fig, ax = plt.subplots()
    ax.pie(x, labels=y, colors=colors, radius=3, center=(4, 4),
        wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))
    plt.show()

pie_chart()