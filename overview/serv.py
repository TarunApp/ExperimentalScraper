import numpy as np
import matplotlib.pyplot as plt
import time, random


#x = np.linspace(0, 2, 1)
							#Function to distribute data points throughout graph
x = random.seed(time)
y = random.randint(0, 19029523)
np.random.seed(y)


N = 50
x = np.random.rand(N) * 2
y = np.random.rand(N) * 5
fig, plot1 = plt.subplots()
plot1.scatter(x, y, 'bo')
#plt.show()