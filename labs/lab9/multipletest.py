import random
import matplotlib.pyplot as plt

x = [elem for elem in range(0,10)]
y = [random.random() for elem in x]

plt.subplot(2, 2, 1)
plt.plot(x, y)

plt.subplot(2, 2, 2)
#plt.plot(x, 0.5 * x ** 2)
plt.plot(x, [elem ** 2 * 0.5 for elem in x])

plt.subplot(2, 2, 3)
#plt.plot(x, y * x ** 2)
plt.plot(x, [y * x ** 2 for x,y in enumerate(y)])

plt.subplot(2, 2, 4)
plt.hist(y)

plt.show()