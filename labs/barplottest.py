import random
import matplotlib.pyplot as plt
lefts = [x for x in range(0,100,5)]
heights = [x + random.random()*50 + 10 for x in range(0,20)]
plt.bar(left=lefts, height=heights, width=4.5, bottom=0,
        color='lightblue', edgecolor='blue')
plt.show()