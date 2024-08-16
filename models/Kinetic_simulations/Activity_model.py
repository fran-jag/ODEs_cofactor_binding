# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 20:34:30 2020

@author: Francisco
"""

import numpy as np
import matplotlib.pyplot as plt
from Hmd_all import S
from Hmd_all import ts
from Hmd_all import l
from Hmd_all import fegp

D = np.zeros(shape=(l+1, 6))
# ts=10 #timescale
tout = np.linspace(0,ts,num=l+1)
plt.figure(dpi=300)

for j in range(6):
    for i in range(l-1):
        D[i,j]=(S[i+1,j]-S[i,j])

A = D*100*100/(1000)*3

# plt.plot(tout,A)
# plt.axis([0,ts,0,120])
# plt.ylabel('Activity')
# plt.xlabel('Time after FeGP addition (min)')
# plt.legend(['4 nM', '17 nM', '50 nM', '100 nM', '300 nM', '700 nM'], fontsize=6, loc='upper right')

maxar = np.amax(A, axis=0)
tmax = np.where(maxar==A)
tmaxs = tmax[0]/100
tmaxmin = tmaxs/60
tmaxmin_rev = tmaxmin[::-1]

maxa = maxar[::-1]

maxat = np.transpose(maxa)
print(maxat)
print(tmaxs)

import math
fegp_array = np.array(fegp, dtype=float)
fegp_log = np.zeros(shape=(6,1))


for k in range(len(fegp_array)):
    fegp_log[k]= math.log(fegp_array[k])

plt.plot(fegp_array,tmaxmin_rev, '.', color='blue')
plt.ylabel('Time for max activity (min)')
plt.xlabel('FeGP (nM)')
plt.axis([0,750,0,5])
# plt.legend(['4 nM', '17 nM', '50 nM', '100 nM', '300 nM', '700 nM'], fontsize=6, loc='upper right')

# from scipy.optimize import curve_fit



# from numpy import savetxt

# savetxt('substrate.csv', S, delimiter= ',')
# savetxt('activities.csv', A, delimiter= ',')
        # 