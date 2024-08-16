import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def hcr(y,t,ke,kb,kd,kf,kr,kc):
    dy0=-kb*y[0]*y[1]+kd*y[2]-ke*y[0]
    dy1=-kb*y[0]*y[1]+kd*y[2]
    dy2=kb*y[0]*y[1]-kd*y[2]-kf*y[2]*y[3]+kr*y[4]+kc*y[4]
    dy3=-kf*y[2]*y[3]+kr*y[4]
    dy4=kf*y[2]*y[3]-kr*y[4]-kc*y[4]
    dy5=kc*y[4]
    return(dy0,dy1,dy2,dy3,dy4,dy5)

fegp = 17 #FeGP concentration (in cuvette)

ts=10 #timescale
tout = np.linspace(0,ts,num=10000)
k_val = 0.21 ,0.005, 0, 0.5, 0.01, 10000 # constants
y0 = [fegp, 4, 0, 20000, 0, 0]

yout = odeint(hcr,y0,tout,k_val)

fig=plt.figure(dpi=600)
plt.subplots_adjust(wspace=0.4, hspace=0.5)

# fig1=fig.add_subplot(121)
# a=plt.plot(tout,yout)
# plt.legend( ['FeGP', 'apo-Hmd', 'holo-Hmd', 'CH$_2$=H$_4$MPT', 'Hmd\u2022S', 'CH$_3$\u2261H$_4$MPT'], bbox_to_anchor=(0, 1.05, 2.4, .102), loc='lower left', ncol=3, mode="expand", borderaxespad=0,)
# plt.axis([0,ts,0,5])

# fig2=fig.add_subplot(122)
# b=plt.plot(tout,yout)
# #plt.legend(['FeGP', 'apo-Hmd', 'holo-Hmd', 'S', 'C', 'P'])
# plt.axis([0,ts,0,21000])


fig3=plt.figure(dpi=600)
c=plt.plot(tout,yout[:,5])
plt.axis([0,ts,0,21000])
plt.ylabel('CH$_3$\u2261H$_4$MPT (nM)')
plt.xlabel('Time after FeGP addition')
plt.legend(['17 nM FeGP'])