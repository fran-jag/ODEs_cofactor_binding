import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

#import from excel
act_wt_ox = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\FeGP titration\All\data_phmd.xlsx', sheet_name='act_wt_ox') 
act_m_ox = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\FeGP titration\All\data_phmd.xlsx', sheet_name='act_m_ox') 
# Ox_m_abs = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\FeGP titration\All\data_phmd.xlsx', sheet_name='abs_m_ox') 

#t = np.arange(2,142,2)
fig1=plt.figure(dpi=1200)
#plt.subplots_adjust(wspace=0.4, hspace=0.5)
 
fig_ox_wt=fig1.add_subplot(221)
#WT
plt.plot(act_wt_ox.loc[:,'Time'],act_wt_ox.loc[:,'A'],'.',color='#840b0f', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_wt_ox.loc[:,'Time'],act_wt_ox.loc[:,'B'],'+',color='#ef060e', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_wt_ox.loc[:,'Time'],act_wt_ox.loc[:,'C'],'^',color='#f9474d', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_wt_ox.loc[:,'Time'],act_wt_ox.loc[:,'D'],'s',color='#FB9DA0', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_wt_ox.loc[:,'Time'],act_wt_ox.loc[:,'E'],'o',color='#fdb0b2', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_wt_ox.loc[:,'Time'],act_wt_ox.loc[:,'F'],'d',color='#feebec', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.fill_between(act_wt_ox.loc[:,'Time'],act_wt_ox.loc[:,'A']-act_wt_ox.loc[:,'A_SD'],act_wt_ox.loc[:,'A']+act_wt_ox.loc[:,'A_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )
plt.fill_between(act_wt_ox.loc[:,'Time'],act_wt_ox.loc[:,'B']-act_wt_ox.loc[:,'B_SD'],act_wt_ox.loc[:,'B']+act_wt_ox.loc[:,'B_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )    
plt.fill_between(act_wt_ox.loc[:,'Time'],act_wt_ox.loc[:,'C']-act_wt_ox.loc[:,'C_SD'],act_wt_ox.loc[:,'C']+act_wt_ox.loc[:,'C_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )
plt.fill_between(act_wt_ox.loc[:,'Time'],act_wt_ox.loc[:,'D']-act_wt_ox.loc[:,'D_SD'],act_wt_ox.loc[:,'D']+act_wt_ox.loc[:,'D_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )
plt.fill_between(act_wt_ox.loc[:,'Time'],act_wt_ox.loc[:,'E']-act_wt_ox.loc[:,'E_SD'],act_wt_ox.loc[:,'E']+act_wt_ox.loc[:,'E_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )
plt.fill_between(act_wt_ox.loc[:,'Time'],act_wt_ox.loc[:,'F']-act_wt_ox.loc[:,'F_SD'],act_wt_ox.loc[:,'F']+act_wt_ox.loc[:,'F_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )

plt.axis([0, 200, 0, 200])
plt.xlabel('Time after FeGP addition (s)', fontfamily='Arial' , weight='bold', size=10)
plt.ylabel('Activity (U/mg)',fontfamily='Arial' , weight='bold', size=10)              
plt.xticks(fontsize=8,fontfamily='Arial')
plt.yticks(fontsize=8,fontfamily='Arial')

plt.savefig(r'C:\Users\Francisco\ownCloud\ScienceData\Library\pHmd\figures\wt_ox_act.png',dpi=300,bbox_inches='tight')                
plt.show()     


# #L150A
fig2=plt.figure(dpi=1200)
fig_ox_m=fig2.add_subplot(221)
plt.plot(act_m_ox.loc[:,'Time'],act_m_ox.loc[:,'A'],'.',color='#0B2B42', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_m_ox.loc[:,'Time'],act_m_ox.loc[:,'B'],'+',color='#014270', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_m_ox.loc[:,'Time'],act_m_ox.loc[:,'C'],'^',color='#218CD9', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_m_ox.loc[:,'Time'],act_m_ox.loc[:,'D'],'s',color='#5CB4F2', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_m_ox.loc[:,'Time'],act_m_ox.loc[:,'E'],'o',color='#78BEF0', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_m_ox.loc[:,'Time'],act_m_ox.loc[:,'F'],'d',color='#C8E4F9', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.fill_between(act_m_ox.loc[:,'Time'],act_m_ox.loc[:,'A']-act_m_ox.loc[:,'A_SD'],act_m_ox.loc[:,'A']+act_m_ox.loc[:,'A_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )
plt.fill_between(act_m_ox.loc[:,'Time'],act_m_ox.loc[:,'B']-act_m_ox.loc[:,'B_SD'],act_m_ox.loc[:,'B']+act_m_ox.loc[:,'B_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )    
plt.fill_between(act_m_ox.loc[:,'Time'],act_m_ox.loc[:,'C']-act_m_ox.loc[:,'C_SD'],act_m_ox.loc[:,'C']+act_m_ox.loc[:,'C_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )
plt.fill_between(act_m_ox.loc[:,'Time'],act_m_ox.loc[:,'D']-act_m_ox.loc[:,'D_SD'],act_m_ox.loc[:,'D']+act_m_ox.loc[:,'D_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )
plt.fill_between(act_m_ox.loc[:,'Time'],act_m_ox.loc[:,'E']-act_m_ox.loc[:,'E_SD'],act_m_ox.loc[:,'E']+act_m_ox.loc[:,'E_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )
plt.fill_between(act_m_ox.loc[:,'Time'],act_m_ox.loc[:,'F']-act_m_ox.loc[:,'F_SD'],act_m_ox.loc[:,'F']+act_m_ox.loc[:,'F_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )


plt.axis([0, 200, 0, 200])
plt.xlabel('Time after FeGP addition (s)', fontfamily='Arial' , weight='bold', size=10)
plt.ylabel('Activity (U/mg)',fontfamily='Arial' , weight='bold', size=10)              
plt.xticks(fontsize=8,fontfamily='Arial')
plt.yticks(fontsize=8,fontfamily='Arial')

plt.savefig(r'C:\Users\Francisco\ownCloud\ScienceData\Library\pHmd\figures\m_ox_act.png',dpi=300,bbox_inches='tight')                
plt.show()                 

