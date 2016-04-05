import random
import matplotlib.pyplot as plt
x = [x + 3 for x in range(0,52,2)]
y = [random.random() * x + x for x in x]

plt.plot(x, y)
plt.xlabel('Time spent coding')
plt.ylabel('Winning')
plt.title('Data plot.')
plt.savefig('img/matplotlib_labeled1.png')
plt.show()
