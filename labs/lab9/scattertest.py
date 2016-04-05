import random
import matplotlib.pyplot as plt
x = [x + 1 for x in range(0,10)]
y = [(elem + random.random()*10) % 10 for elem in x]
sizes = [200 * elem + random.random() * 9300 for elem in x]
plt.scatter(x, y, s=sizes, c=sizes, alpha=0.8)
plt.savefig('img/matplotlib_scatter.png')
plt.show()
