import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def hac(y,t,kb,kd,ke):
    dy0=-kb*y[0]*y[1]+kd*y[2]-ke*y[0] #FeGP
    dy1=-kb*y[0]*y[1]+kd*y[2] #apo-Hmd
    dy2=kb*y[0]*y[1]-kd*y[2] #holo-Hmd
    return(dy0,dy1,dy2)

ts=1000 #timescale
l=60
tout = np.linspace(0,ts,num=l*ts)

k_val = 0.1, 0, 0.01 #constants per sec
y0 = [0.9, 0.4, 0]

yout = odeint(hac,y0,tout,k_val)

E = yout[:,1] + yout[:,2]
toutmin= tout/60

plt.figure(dpi=300)
plt.plot(tout,yout[:,1])
plt.plot(tout,yout[:,2])
plt.legend(['apo-Hmd', 'holo-Hmd'])
plt.ylabel('Enzyme (µM)')
plt.xlabel('Time (s)')
#plt.axis([0,1000,0,0.2])

max_holo = yout[l*ts-10,2]/y0[1]*100
print(round(max_holo), '% Max Reconstitution')