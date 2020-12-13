import numpy as np
import math
import matplotlib.pyplot as plt

f = open("F:/results/test.doc", "a")
x = -5
def y(x): 
        y = -20*math.exp(-0.2*math.sqrt(0.5*(x**2)))-math.exp(0.5*(np.cos(2*math.pi*x)))+math.exp(1)+20
        y1 = round(y, 2)
        return y1


f.write("X         Y")

while x <= 5: 
    f.write("\n" + str(x) + "         " + str(y(x)))
    x = x + 0.5

f.close()

x = np.arange(-5, 5)
fig, ax = plt.subplots()
ax.plot(x, y(x))  
lgnd = ax.legend(['y'], loc='upper center', shadow=True)
lgnd.get_frame().set_facecolor('green')
plt.show()