import numpy as np
import math
import matplotlib.pyplot as plt
import os

x = -5
def y(x): 
        y = -20*math.exp(-0.2*math.sqrt(0.5*(x**2)))-math.exp(0.5*(np.cos(2*math.pi*x)))+math.exp(1)+20
        y1 = round(y, 2)
        return y1

# создание файла
try:
 os.mkdir('results')
except OSError:
 pass
complete_file = os.path.join('results', 'task_01_307B_nguyen_2.txt')
f = open(complete_file, 'w')
# текстовый файл с таблицей

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