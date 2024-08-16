# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:31:06 2020

@author: Francisco
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pandas as pd

#define mass acion kinetics
#-------------------
def hmd(y,t,kf,kr,kc):
    dy0=-kf*y[0]*y[2]-kr*y[1] #Substrate
    dy1=kf*y[0]*y[2]-kr*y[1]-kc*y[1] #Enzyme-Substrate complex
    dy2=-kf*y[0]*y[2]+kc*y[1] #holo-Hmd
    dy3=kc*y[1] # Product
    return[dy0,dy1,dy2,dy3]

#Initial parameters
#----------------------

tout = np.linspace(0,600,num=600)
S = 24.3 #Substrate in µM. Can be one or many concentrations
E = [0.001, 0.0037, 0.005, 0.0074, 0.01, 1]
y0 = [S, 0, E, 0] #initial concentrations µM
Vmax = 61 #U/mg
kcat = Vmax/0.026/60 #kcat per sec
km = 4.1
k_vals = (kcat/km), 0, kcat
P = np.zeros(shape=(600,6))
D = np.zeros(shape=(601,6)) #Define difference in substrate concentration
A = np.zeros(shape=(601,6))

#Run simulation for all S
#--------------------

for j in range(len(E)):
    y0 = [S, 0, E[j], 0]
    yout = odeint(hmd,y0,tout,k_vals)
    P[:,j] = yout[:,3]
    for i in range(600-1):
        D[i,j]=(P[i+1,j]-P[i,j])

for k in range(len(E)):
    A[:,k] = D[:,k]*60/E[k]*0.026 #Calculate activity from substrate differences, correct for timescale differences

#Find Time of Max activity
#--------------------------
maxar = np.amax(A, axis=0)
tmax = np.where(maxar==A)
# tmaxs = tmax[0]/100
tmaxmin = tmax[0]/60
tmaxmin_rev = tmaxmin[::-1]

# maxa = maxar[::-1]

maxat = np.transpose(maxar)
print(maxat)

#import from excel
#-----------------
prod_wt_ox = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Python\pHmd\Models\WT_ox_product.xlsx', sheet_name='Product_2') 
ori_time_prod = prod_wt_ox.loc[:,'Time']

#Plot Substrate vs time
#--------------------

plt.figure(dpi=600)
# tout = np.linspace(0,10,num=601)
plt.plot(tout,P[:,1])
plt.plot(ori_time_prod,prod_wt_ox.loc[:,'E'], 'x', color='purple', markersize=2)
plt.axis([0,600,0,25])
plt.ylabel('Prouct (µM)')
plt.xlabel('Time')
# plt.legend(['10 nM', '25 nM', '50 nM', '75 nM', '100 nM', '250 nM'], fontsize=6, loc='upper right')
