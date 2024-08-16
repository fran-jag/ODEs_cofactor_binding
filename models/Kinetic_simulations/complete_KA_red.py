import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from hcr import hcr
import pandas as pd

#Parameters of the simulation
#-----------------------------
fegp = [4, 10, 50, 100, 350, 700] #FeGP concentrations
ts=6 #timescale
l = ts*60*100
tout = np.linspace(0,ts,num=(l))
k_val = 0.21, 0.00005, 0, 34, 1, 80000 # constants default 0.1, 0.001, 0, 6, 1, 48000
# FeGP degradation, FeGP binding, FeGP dissociation, Substrate binding, Substrate dissociation, Kcat
S = np.zeros(shape=(l,6)) #Define substrate array


#Running the simulation
#-----------------------

for i in range(len(fegp)):
    
    y0 = [fegp[i], 4, 0, 20000, 0, 0]   
    yout = odeint(hcr,y0,tout,k_val)
    # plt.plot(tout,yout[:,5])
    S[:,i] = yout[:,5]

#Calculating Activity
#----------------------
D = np.zeros(shape=(l+1, 6)) #Define difference in substrate concentration
tout = np.linspace(0,ts,num=l+1)
for j in range(6):
    for i in range(l-1):
        D[i,j]=(S[i+1,j]-S[i,j])

A = D*100*100/(1000) #Calculate activity from substrate differences

plt.figure(dpi=300)
plt.plot(tout,A)
plt.axis([0,ts,0,120])
plt.ylabel('Activity')
plt.xlabel('Time after FeGP addition (min)')
plt.legend(['4 nM', '17 nM', '50 nM', '100 nM', '300 nM', '700 nM'], fontsize=6, loc='upper right')

#import from excel
act_ka_rd = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\FeGP titration\All\Activities.xlsx', sheet_name='KA_rd') 
ori_time_act = act_ka_rd.loc[:,'Time']/60

plt.plot(ori_time_act,act_ka_rd.loc[:,'A'],'+',color='brown',markersize=3,mew =0.5, markevery=4, ls='')
plt.plot(ori_time_act,act_ka_rd.loc[:,'B'],'+',color='purple',markersize=3,mew =0.5, markevery=4, ls='')
plt.plot(ori_time_act,act_ka_rd.loc[:,'C'],'+',color='red',markersize=3,mew =0.5, markevery=4, ls='')
plt.plot(ori_time_act,act_ka_rd.loc[:,'D'],'+',color='green',markersize=3,mew =0.5, markevery=4, ls='')
plt.plot(ori_time_act,act_ka_rd.loc[:,'E'],'+',color='orange',markersize=3,mew =0.5, markevery=4, ls='')
plt.plot(ori_time_act,act_ka_rd.loc[:,'F'],'+',color='blue',markersize=3,mew =0.5, markevery=4, ls='')


#Find Time of Max activity
#--------------------------
maxar = np.amax(A, axis=0)
tmax = np.where(maxar==A)
tmaxs = tmax[0]/100
tmaxmin = tmaxs/60
tmaxmin_rev = tmaxmin[::-1]

maxa = maxar[::-1]

maxat = np.transpose(maxa)
print(maxat)
print(tmaxs)

#Calculate log FeGP
#---------------------------------
import math
fegp_array = np.array(fegp, dtype=float)
fegp_log = np.zeros(shape=(6,1))

for k in range(len(fegp_array)):
    fegp_log[k]= math.log(fegp_array[k])
    
#Original experimental data
#-------------------------------
ori_fegp = np.array([700, 350, 100, 50, 10, 4])
ori_ka_time = np.array([159.33, 174.67, 278.67, 390.00, 363.30, 363.3])
ori_ka_time_min = ori_ka_time/60

#Plot Log FeGP vs time for max activity
#---------------------------------------
plt.figure(dpi=600)
plt.plot(fegp,tmaxmin_rev, '.', color='red')
plt.plot(ori_fegp,ori_ka_time_min, '+', color='red')
plt.ylabel('Time for max activity (min)')
plt.xlabel('FeGP (nM)')
plt.axis([0,750,0,10])
plt.legend(['Lys150Ala simulated data', 'Lys150Ala experimental data'])

# plt.savefig(r'C:\Users\Francisco\ownCloud\ScienceData\Python\pHmd\Models\Time of max act\K150A_red_comparison.png',dpi=600,bbox_inches='tight')                
# plt.show()     


# from scipy.optimize import curve_fit
# from numpy import savetxt
# savetxt('substrate.csv', S, delimiter= ',')
# savetxt('activities.csv', A, delimiter= ',')
        # 