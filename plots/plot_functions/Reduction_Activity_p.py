import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

#import from excel
act_wt_red = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\FeGP titration\All\data_phmd.xlsx', sheet_name='act_wt_red') 
act_m_red = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\FeGP titration\All\data_phmd.xlsx', sheet_name='act_m_red') 

#t = np.arange(2,142,2)
fig1=plt.figure(dpi=1200)
#plt.subplots_adjust(wspace=0.4, hspace=0.5)
 
fig_ox_wt=fig1.add_subplot(221)
#WT
plt.plot(act_wt_red.loc[:,'Time'],act_wt_red.loc[:,'A'],'.',color='#840b0f', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_wt_red.loc[:,'Time'],act_wt_red.loc[:,'B'],'+',color='#ef060e', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_wt_red.loc[:,'Time'],act_wt_red.loc[:,'C'],'^',color='#f9474d', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_wt_red.loc[:,'Time'],act_wt_red.loc[:,'D'],'s',color='#FB9DA0', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_wt_red.loc[:,'Time'],act_wt_red.loc[:,'E'],'o',color='#fdb0b2', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_wt_red.loc[:,'Time'],act_wt_red.loc[:,'F'],'d',color='#feebec', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.fill_between(act_wt_red.loc[:,'Time'],act_wt_red.loc[:,'A']-act_wt_red.loc[:,'A_SD'],act_wt_red.loc[:,'A']+act_wt_red.loc[:,'A_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )
plt.fill_between(act_wt_red.loc[:,'Time'],act_wt_red.loc[:,'B']-act_wt_red.loc[:,'B_SD'],act_wt_red.loc[:,'B']+act_wt_red.loc[:,'B_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )    
plt.fill_between(act_wt_red.loc[:,'Time'],act_wt_red.loc[:,'C']-act_wt_red.loc[:,'C_SD'],act_wt_red.loc[:,'C']+act_wt_red.loc[:,'C_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )
plt.fill_between(act_wt_red.loc[:,'Time'],act_wt_red.loc[:,'D']-act_wt_red.loc[:,'D_SD'],act_wt_red.loc[:,'D']+act_wt_red.loc[:,'D_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )
plt.fill_between(act_wt_red.loc[:,'Time'],act_wt_red.loc[:,'E']-act_wt_red.loc[:,'E_SD'],act_wt_red.loc[:,'E']+act_wt_red.loc[:,'E_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )
plt.fill_between(act_wt_red.loc[:,'Time'],act_wt_red.loc[:,'F']-act_wt_red.loc[:,'F_SD'],act_wt_red.loc[:,'F']+act_wt_red.loc[:,'F_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )

plt.axis([0, 250, 0, 100])
plt.xlabel('Time after FeGP addition (s)', fontfamily='Arial' , weight='bold', size=10)
plt.ylabel('Activity (U/mg)',fontfamily='Arial' , weight='bold', size=10)              
plt.xticks(fontsize=8,fontfamily='Arial')
plt.yticks(fontsize=8,fontfamily='Arial')

plt.savefig(r'C:\Users\Francisco\ownCloud\ScienceData\Library\pHmd\figures\wt_red_act_2.png',dpi=300,bbox_inches='tight')                
plt.show()     


# #L150A
fig2=plt.figure(dpi=1200)
fig_ox_m=fig2.add_subplot(221)
plt.plot(act_m_red.loc[:,'Time'],act_m_red.loc[:,'A'],'.',color='#0B2B42', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_m_red.loc[:,'Time'],act_m_red.loc[:,'B'],'+',color='#014270', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_m_red.loc[:,'Time'],act_m_red.loc[:,'C'],'^',color='#218CD9', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_m_red.loc[:,'Time'],act_m_red.loc[:,'D'],'s',color='#5CB4F2', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_m_red.loc[:,'Time'],act_m_red.loc[:,'E'],'o',color='#78BEF0', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(act_m_red.loc[:,'Time'],act_m_red.loc[:,'F'],'d',color='#C8E4F9', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.fill_between(act_m_red.loc[:,'Time'],act_m_red.loc[:,'A']-act_m_red.loc[:,'A_SD'],act_m_red.loc[:,'A']+act_m_red.loc[:,'A_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )
plt.fill_between(act_m_red.loc[:,'Time'],act_m_red.loc[:,'B']-act_m_red.loc[:,'B_SD'],act_m_red.loc[:,'B']+act_m_red.loc[:,'B_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )    
plt.fill_between(act_m_red.loc[:,'Time'],act_m_red.loc[:,'C']-act_m_red.loc[:,'C_SD'],act_m_red.loc[:,'C']+act_m_red.loc[:,'C_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )
plt.fill_between(act_m_red.loc[:,'Time'],act_m_red.loc[:,'D']-act_m_red.loc[:,'D_SD'],act_m_red.loc[:,'D']+act_m_red.loc[:,'D_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )
plt.fill_between(act_m_red.loc[:,'Time'],act_m_red.loc[:,'E']-act_m_red.loc[:,'E_SD'],act_m_red.loc[:,'E']+act_m_red.loc[:,'E_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )
plt.fill_between(act_m_red.loc[:,'Time'],act_m_red.loc[:,'F']-act_m_red.loc[:,'F_SD'],act_m_red.loc[:,'F']+act_m_red.loc[:,'F_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )


plt.axis([0, 250, 0, 100])
plt.xlabel('Time after FeGP addition (s)', fontfamily='Arial' , weight='bold', size=10)
plt.ylabel('Activity (U/mg)',fontfamily='Arial' , weight='bold', size=10)              
plt.xticks(fontsize=8,fontfamily='Arial')
plt.yticks(fontsize=8,fontfamily='Arial')

plt.savefig(r'C:\Users\Francisco\ownCloud\ScienceData\Library\pHmd\figures\m_red_act_2.png',dpi=300,bbox_inches='tight')                
plt.show()                 

