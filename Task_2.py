from scipy.constants import c, pi
from scipy.special import spherical_jn as jn, spherical_yn as yn
import numpy as np
from pathlib import Path as pth
import matplotlib.pyplot as plt
from urllib.request  import urlopen as uopn
import re
import pandas as pd

tsk_v = 2
pfile = pth('./taskfile.csv')
df=pd.read_csv(pfile, header=None,delimiter=';')
print(df.head())
data=df.to_numpy()

#get data for my variant
m=data[1, :]
D = float(m[0])
fmin = float(m[1])
fmax = float(m[2])

f = np.linspace(fmin, fmax, 400)
r = D/2

def hn(n, x):
    return complex(jn(n, x), yn(n,x))

def bn(n, x):
    upr_n = x * jn(n-1, x) - n*jn(n, x)
    lwr_n = x * hn(n-1, x) - n * hn(n, x)
    return upr_n / lwr_n

def an(n, x):
    return jn(n, x) / hn(n, x) 

def f_sigma(x):
    lmbd = c / x 
    k = 2 * pi / lmbd
    kr = k*r
    Sum = 0+0j
    for n in range(1, 40):
        Sum += ((-1) ** n) * (n + 1/2) * (bn(n, kr) - an(n, kr))
    return ((lmbd**2) / pi) * (np.abs(Sum)**2) 

sigma = [f_sigma(x) for x in f]

p = pth('results')
res = p / 'task_02_307b_nguyen_2.txt'
if not p.exists():
  p.mkdir(exist_ok = True)

if p.exists():
  with res.open('w') as fl:
    i = 0
    for x in f:
      fl.write('%20f   %.20f\n' % (x, sigma[i]))
      i += 1
else:
  print("Error: \'results\' dir does not exists - access denied")


plt.plot(f/1e9, sigma)
plt.xlabel('f, ГГц')
plt.ylabel('$\sigma, м^2$')
plt.grid()
plt.show()

a0 = 4
f_tst = c * a0 / (2*pi*r)
s_tst = f_sigma(f_tst)/(pi * r * r)
l = 2 * pi * r * f_tst / c
print(l, s_tst)
