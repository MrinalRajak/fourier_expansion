
#Determination of Fourier coefficient of square wave using defined function ,using(quad)

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import scipy.signal as s

def f(t):
    if(-np.pi<=t<0.0):
        result=-1
    if(0.0<=t<=np.pi):
        result=+1
    return result
ff=np.vectorize(f)
L=np.pi
n=100
t,h=np.linspace(-np.pi,np.pi,1000,retstep=True)
y1=s.square(t)
plt.plot(t,y1)
an=[]
bn=[]
# Determination of coefficient an and bn
for i in range(n):
    an.append(quad(lambda t:ff(t)*np.cos((i*np.pi*t)/L),-np.pi,np.pi)[0]/L)
    bn.append(quad(lambda t:ff(t)*np.sin((i*np.pi*t)/L),-np.pi,np.pi)[0]/L)
print("an: ",an)
print("bn: ",bn)
s=0
for i in range(n):
    if(i==0):
        s=s+(an[i]/2)
    else:
        s=s+an[i]*np.cos((i*np.pi*t)/L)+bn[i]*np.sin((i*np.pi*t)/L)
plt.plot(t,s)
plt.grid(True)
plt.show()
