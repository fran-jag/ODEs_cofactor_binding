# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 19:34:33 2020

@author: Francisco
"""
import numpy as np
# import matplotlib.pyplot as plt
from scipy.integrate import odeint


fegp = [4, 17, 50, 100, 350, 700] #FeGP concentrations
ts=5 #timescale
l = ts*60*100
tout = np.linspace(0,ts,num=(l))
k_val = 0.21, 0.001, 0, 6, 1, 48000 # constants default 0.1, 0.001, 0, 6, 1, 48000
# FeGP degradation, FeGP binding, FeGP dissociation, Substrate binding, Substrate dissociation, Kcat

S = np.zeros(shape=(l,6))

def hcr(y,t,ke,kb,kd,kf,kr,kc):
    dy0=-kb*y[0]*y[1]+kd*y[2]-ke*y[0]
    dy1=-kb*y[0]*y[1]+kd*y[2]
    dy2=kb*y[0]*y[1]-kd*y[2]-kf*y[2]*y[3]+kr*y[4]+kc*y[4]
    dy3=-kf*y[2]*y[3]+kr*y[4]
    dy4=kf*y[2]*y[3]-kr*y[4]-kc*y[4]
    dy5=kc*y[4]
    return(dy0,dy1,dy2,dy3,dy4,dy5)

# plt.figure(dpi=300)

for i in range(len(fegp)):
    
    y0 = [fegp[i], 4, 0, 20000, 0, 0]   
    yout = odeint(hcr,y0,tout,k_val)
    # plt.plot(tout,yout[:,5])
    S[:,i] = yout[:,5]
    

# plt.axis([0,ts,0,21000])
# plt.ylabel('CH$_3$\u2261H$_4$MPT (nM)')
# plt.xlabel('Time after FeGP addition (min)')
# plt.legend(['4 nM', '17 nM', '50 nM', '100 nM', '300 nM', '700 nM'], fontsize=6, loc='upper left')
        

