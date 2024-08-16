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
S = [11.15, 11.04, 7.82, 7.68, 4.32, 3.96]
# y0 = [S,0,0.0037,0]
Vmax = 350 #U/mg
kcat = Vmax/0.026/60
km = [65, 65, 50, 50, 30, 30]
kr = 0
# k_vals = (kcat/km), 0, kcat
Sub = np.zeros(shape=(600,12))
D = np.zeros(shape=(600,12)) #Define difference in substrate concentration

for j in range(len(S)):
    y0 = [S[j], 0, 0.0037, 0]
    k_vals = ((kcat-kr)/km[j]), 0, kcat
    yout = odeint(hmd,y0,tout,k_vals)
    Sub[:,j] = yout[:,0]
    for i in range(600-1):
        D[i,j]=(Sub[i+1,j]-Sub[i,j])




A = -1*D*60/y0[2]*0.026 #Calculate activity from substrate differences, correct for timescale differences

#Find Time of Max activity
#--------------------------
# maxar = np.amax(A, axis=0)
# tmax = np.where(maxar==A)
# tmaxmin = tmax[0]/60
# tmaxmin_rev = tmaxmin[::-1]

# maxa = maxar[::-1]

# maxat = np.transpose(maxar)
# print(maxat)




# Km data for WT_ox
#---------------------

ori_wt_ox_act = [32.2, 39.1, 46.5, 46.2, 50.1, 52.8]
ori_wt_ox_act_2 = [33.49305556, 33.78472222,45.84027778,36.26388889,45.69444444,45.79166667]

# Plot Max activity
#-----------------
# plt.figure(dpi=600)
# plt.plot(S,maxat, 'o', color='blue')
# plt.plot(S,ori_wt_ox_act_2, 'x', color='red')
# plt.legend(['Simulated', 'Experimental'], fontsize=5, loc='lower right')
# plt.axis([0,50,0,80])

#Plot Substrate vs time
#--------------------

#import from excel
prod_wt_ox = pd.read_excel ('KA_red.xlsx', sheet_name='KA_red') 
ori_time_prod = prod_wt_ox.loc[:,'Time']


plt.figure(dpi=600)
# tout = np.linspace(0,10,num=601)
# plt.subplot(121)
plt.plot(tout,Sub)
for k in range(1,7):
    plt.plot(ori_time_prod,prod_wt_ox.iloc[:,k], 'x', markersize=2)

plt.axis([0,200,0,20])
plt.ylabel('Prouct (µM)')
plt.xlabel('Time')

# plt.subplot(122)
# plt.plot(tout,Sub)
# for k in range(1,13):
#     plt.plot(ori_time_prod,prod_wt_ox.iloc[:,k], 'x', markersize=2)
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
