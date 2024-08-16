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
S = [37, 27.5, 22.5, 5.7]
# Vmax = [55, 55, 55, 55, 55, 55] #U/mg
kcat = 42.1
km = 5.7
kr = 0
P = np.zeros(shape=(600,6))
D = np.zeros(shape=(600,6)) #Define difference in substrate concentration

for j in range(len(S)):
    y0 = [S[j], 0, 0.0037, 0.5]
    # kcat = Vmax[j]/0.026/60
    k_vals = ((kcat+kr)/km), kr, kcat
    yout = odeint(hmd,y0,tout,k_vals)
    P[:,j] = yout[:,3]
    for i in range(600-1):
        D[i,j]=(P[i+1,j]-P[i,j])




A = D*60/y0[2]*0.026 #Calculate activity from substrate differences

#Find Time of Max activity
#--------------------------
maxar = np.amax(A, axis=0)
tmax = np.where(maxar==A)
tmaxs = tmax[0]
tmaxmin = tmaxs/60
tmaxmin_rev = tmaxmin[::-1]

maxa = maxar[::-1]

maxat = np.transpose(maxa)
print(maxar)

print(maxar[3]*0.0037*60/0.026*2)
#Plot Substrate vs time
#--------------------

#import from excel
prod_wt_ox = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Python\pHmd\Models\Corrected models\WT_ox.xlsx', sheet_name='WT_ox') 
ori_time_prod = prod_wt_ox.loc[:,'Time']

plt.figure(dpi=600)
plt.subplot(121)

plt.gca().set_prop_cycle(None)
plt.plot(tout,P)

plt.gca().set_prop_cycle(None)
for k in range(1,5):
    if k != 2:
        plt.plot(ori_time_prod, prod_wt_ox.iloc[:,k], 'x', markersize=3, markevery=6)
    if k == 2:
        print()
    
plt.axis([0,450,0,50])
plt.ylabel('Prouct (µM)')
plt.xlabel('Time')

plt.subplot(122)
plt.plot(tout,P)
for k in range(1,5):
    if k != 2:
        plt.plot(ori_time_prod, prod_wt_ox.iloc[:,k], 'x', markersize=3, markevery=6)
    if k == 2:
        break
    
plt.axis([0,100,0,10])
plt.ylabel('Prouct (µM)')
plt.xlabel('Time')


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
