import matplotlib.pyplot as plt
import numpy as np
from entries import *

rent = rent
food = food
transportation = transportation
savings = savings


def pie_chart(rent, food, transportation, savings):
    plt.style.use('_mpl-gallery-nogrid')

    titles = ['Rent', 'Food', 'Transportation', 'Savings']
    values = [rent, food, transportation, savings]
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

pie_chart(rent, food, transportation, savings)