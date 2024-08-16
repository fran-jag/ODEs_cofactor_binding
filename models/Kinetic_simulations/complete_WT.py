import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from hcr import hcr
import pandas as pd

#Parameters of the simulation
#-----------------------------
fegp = [4, 10, 50, 100, 350, 700] #FeGP concentrations
ts=5 #timescale
l = ts*60*100
tout = np.linspace(0,ts,num=(l))
k_val = 0.12, 0.0001, 0, 157, 0, 350000 # constants default 0.1, 0.001, 0, 12000, 1, 24000
# FeGP degradation, FeGP binding, FeGP dissociation, Substrate binding, Substrate dissociation, Kcat
S = np.zeros(shape=(l,6)) #Define substrate array

#Running the simulation
#-----------------------

for i in range(len(fegp)):
    
    y0 = [fegp[i], 3.7, 0, 14580, 0, 0]   
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

A = D*100*60/(1000)*3.8 #Calculate activity from substrate differences, correct for timescale differences

plt.figure(dpi=600)
plt.plot(tout,A)
plt.axis([0,4,0,200])
plt.ylabel('Activity')
plt.xlabel('Time after FeGP addition (min)')
plt.legend(['4 nM', '17 nM', '50 nM', '100 nM', '300 nM', '700 nM'], fontsize=6, loc='upper right')

#Plotting experimental data (activities)
#--------------------

#import from excel
act_wt_ox = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\FeGP titration\All\Activities.xlsx', sheet_name='WT_ox') 
ori_time_act = act_wt_ox.loc[:,'Time']/60

plt.plot(ori_time_act,act_wt_ox.loc[:,'A'],'+',color='brown',markersize=3,mew =0.5, markevery=4, ls='')
plt.plot(ori_time_act,act_wt_ox.loc[:,'B'],'+',color='purple',markersize=3,mew =0.5, markevery=4, ls='')
plt.plot(ori_time_act,act_wt_ox.loc[:,'C'],'+',color='red',markersize=3,mew =0.5, markevery=4, ls='')
plt.plot(ori_time_act,act_wt_ox.loc[:,'D'],'+',color='green',markersize=3,mew =0.5, markevery=4, ls='')
plt.plot(ori_time_act,act_wt_ox.loc[:,'E'],'+',color='orange',markersize=3,mew =0.5, markevery=4, ls='')
plt.plot(ori_time_act,act_wt_ox.loc[:,'F'],'+',color='blue',markersize=3,mew =0.5, markevery=4, ls='')


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
ori_wt_time = np.array([35.3, 54.7, 85.3, 134, 283, 256.7])

ori_wt_time_min = ori_wt_time/60


#Plot Log FeGP vs time for max activity
#---------------------------------------
# plt.figure(dpi=600)
# plt.plot(fegp,tmaxmin_rev, '.', color='blue')
# plt.plot(ori_fegp,ori_wt_time_min, '+', color='blue')
# plt.ylabel('Time for max activity (min)')
# plt.xlabel('FeGP (nM)')
# plt.axis([0,750,0,5])
# plt.legend(['WT simulated data', 'WT experimental data', 'K150A experimental data'])

# plt.savefig(r'C:\Users\Francisco\ownCloud\ScienceData\Python\pHmd\Models\Time of max act\WT_comparison.png',dpi=600,bbox_inches='tight')                
# plt.show()     


# from scipy.optimize import curve_fit
# from numpy import savetxt

# savetxt('substrate.csv', S, delimiter= ',')
# savetxt('activities.csv', A, delimiter= ',')
        # 