import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import pandas as pd

def hmd(y,t,kf,kr,kc):
    dy0=-kf*y[0]*y[2]-kr*y[1] #Substrate
    dy1=kf*y[0]*y[2]-kr*y[1]-kc*y[1] #Enzyme-Substrate complex
    dy2=-kf*y[0]*y[2]+kc*y[1] #holo-Hmd
    dy3=kc*y[1] # Product
    return[dy0,dy1,dy2,dy3]



tout = np.linspace(0,600,num=600)
S = [37.5, 35.7, 28, 22.9, 12.4]
Vmax = 65 #U/mg
kcat = Vmax/0.026/60
km = [5.5, 7.5, 5.5, 4.5, 3]
P = np.zeros(shape=(600,6))
D = np.zeros(shape=(600,6)) #Define difference in substrate concentration

for j in range(len(S)):
    y0 = [S[j], 0, 0.0037, 0]
    k_vals = (kcat/km[j]), 0, kcat
    yout = odeint(hmd,y0,tout,k_vals)
    P[:,j] = yout[:,3]
    for i in range(600-1):
        D[i,j]=(P[i+1,j]-P[i,j])




A = D*60/y0[2]*0.026 #Calculate activity from substrate differences

#Plot Substrate vs time
#--------------------

#import from excel
prod_wt_ox = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Python\pHmd\Models\Corrected models\WT_ox.xlsx', sheet_name='WT_ox') 
ori_time_prod = prod_wt_ox.loc[:,'Time']


plt.figure(dpi=600)
plt.figure(dpi=600)
plt.plot(tout,P)
for k in range(1,6):
    plt.plot(ori_time_prod, prod_wt_ox.iloc[:,k], 'x', markersize=3, markevery=4)

plt.axis([0,600,0,50])
plt.ylabel('Prouct (µM)')
plt.xlabel('Time')

# plt.subplot(122)
# plt.plot(tout,P)
# plt.plot(ori_time_prod,prod_wt_ox.loc[:,'A'], 'x', color='blue', markersize=2)
# plt.plot(ori_time_prod,prod_wt_ox.loc[:,'B'], 'x', color='orange', markersize=2)
# plt.plot(ori_time_prod,prod_wt_ox.loc[:,'C'], 'x', color='green', markersize=2)
# plt.plot(ori_time_prod,prod_wt_ox.loc[:,'D'], 'x', color='red', markersize=2)
# plt.plot(ori_time_prod,prod_wt_ox.loc[:,'E'], 'x', color='purple', markersize=2)
# plt.plot(ori_time_prod,prod_wt_ox.loc[:,'F'], 'x', color='brown', markersize=2)
# plt.axis([0,150,0,20])
# plt.ylabel('Prouct (µM)')
# plt.xlabel('Time')


# A = np.delete(A,(0),axis=0)
# plt.subplot(122)
# plt.plot(tout,A)
# plt.plot(ori_time_prod,prod_wt_ox.loc[:,'A'], 'x', color='blue', markersize=2)
# plt.plot(ori_time_prod,prod_wt_ox.loc[:,'B'], 'x', color='orange', markersize=2)
# plt.plot(ori_time_prod,prod_wt_ox.loc[:,'C'], 'x', color='green', markersize=2)
# plt.plot(ori_time_prod,prod_wt_ox.loc[:,'D'], 'x', color='red', markersize=2)
# plt.plot(ori_time_prod,prod_wt_ox.loc[:,'E'], 'x', color='purple', markersize=2)
# plt.plot(ori_time_prod,prod_wt_ox.loc[:,'F'], 'x', color='brown', markersize=2)
# plt.axis([0,0.02,0,80])
# plt.ylabel('Activity (U/mg)')
# plt.xlabel('Time')
# plt.legend(['4 nM', '17 nM', '50 nM', '100 nM', '300 nM', '700 nM'], fontsize=6, loc='upper right')
