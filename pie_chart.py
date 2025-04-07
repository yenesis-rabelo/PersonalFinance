# Matthew McKinley, income/expense tracking ---------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from entries import *

def pie_chart(user_info):
    print("For best experience, use fullscreen.")
    plt.style.use('_mpl-gallery-nogrid')

    titles = []
    values = []

    for entry in user_info["record"]: # Sets the titles and values for income entries
        if entry['amount'] > 0:
            if entry["location"] not in titles:
                titles.append(entry["location"])
                values.append(0)
            values[titles.index(entry["location"])] += entry['amount']
        
    fig, ax = plt.subplots() # Displays income entries
    colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(values)))
    ax.pie(values, labels=titles, colors=colors, radius=3, center=(4, 4),
        wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
    plt.text(3, 8, 'Income', fontsize=30, color='black')
    
    titles = []
    values = []

    for entry in user_info["record"]: # Sets the titles and values for expense entries
        if entry['amount'] < 0:
            if entry["location"] not in titles:
                titles.append(entry["location"])
                values.append(0)
            values[titles.index(entry["location"])] -= entry['amount']

    
    colors = plt.get_cmap('Reds')(np.linspace(0.2, 0.7, len(values))) # Displays expense entries
    ax.pie(values, labels=titles, colors=colors, radius=3, center=(11, 4),
        wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=True)
    plt.text(10, 8, 'Expenses', fontsize=30, color='black')

    ax.set(xlim=(0, 15), xticks=np.arange(1, 0), # Displays the figures
        ylim=(0, 9), yticks=np.arange(1, 0))
    plt.show()
