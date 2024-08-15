import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np

#import from excel
# Ox_wt_abs = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\FeGP titration\All\data_phmd.xlsx', sheet_name='abs_wt_ox') 
# Ox_m_abs = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\FeGP titration\All\data_phmd.xlsx', sheet_name='abs_m_ox') 
Red_wt_abs = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\FeGP titration\All\data_phmd.xlsx', sheet_name='abs_wt_red') 
Red_m_abs = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\FeGP titration\All\data_phmd.xlsx', sheet_name='abs_m_red') 


#Red_u = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\Reconstitution\final_graph.xlsx', sheet_name='Red_u') 
#Ox_abs = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\Reconstitution\final_graph.xlsx', sheet_name='Ox_abs') 
#Ox_u = pd.read_excel (r'C:\Users\Francisco\ownCloud\ScienceData\Activity Assays\pHmd\Reconstitution\final_graph.xlsx', sheet_name='Ox_u') 

#t = np.arange(2,142,2)
fig1=plt.figure(dpi=1200)
#plt.subplots_adjust(wspace=0.4, hspace=0.5)
 
fig_red_wt=fig1.add_subplot(221)
#WT
plt.plot(Red_wt_abs.loc[:,'Time'],Red_wt_abs.loc[:,'A'],'.',color='#840b0f', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(Red_wt_abs.loc[:,'Time'],Red_wt_abs.loc[:,'B'],'+',color='#ef060e', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(Red_wt_abs.loc[:,'Time'],Red_wt_abs.loc[:,'C'],'^',color='#f9474d', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(Red_wt_abs.loc[:,'Time'],Red_wt_abs.loc[:,'D'],'s',color='#FB9DA0', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(Red_wt_abs.loc[:,'Time'],Red_wt_abs.loc[:,'E'],'o',color='#fdb0b2', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(Red_wt_abs.loc[:,'Time'],Red_wt_abs.loc[:,'F'],'d',color='#feebec', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.fill_between(Red_wt_abs.loc[:,'Time'],Red_wt_abs.loc[:,'A']-Red_wt_abs.loc[:,'A_SD'],Red_wt_abs.loc[:,'A']+Red_wt_abs.loc[:,'A_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )
plt.fill_between(Red_wt_abs.loc[:,'Time'],Red_wt_abs.loc[:,'B']-Red_wt_abs.loc[:,'B_SD'],Red_wt_abs.loc[:,'B']+Red_wt_abs.loc[:,'B_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )    
plt.fill_between(Red_wt_abs.loc[:,'Time'],Red_wt_abs.loc[:,'C']-Red_wt_abs.loc[:,'C_SD'],Red_wt_abs.loc[:,'C']+Red_wt_abs.loc[:,'C_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )
plt.fill_between(Red_wt_abs.loc[:,'Time'],Red_wt_abs.loc[:,'D']-Red_wt_abs.loc[:,'D_SD'],Red_wt_abs.loc[:,'D']+Red_wt_abs.loc[:,'D_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )
plt.fill_between(Red_wt_abs.loc[:,'Time'],Red_wt_abs.loc[:,'E']-Red_wt_abs.loc[:,'E_SD'],Red_wt_abs.loc[:,'E']+Red_wt_abs.loc[:,'E_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )
plt.fill_between(Red_wt_abs.loc[:,'Time'],Red_wt_abs.loc[:,'F']-Red_wt_abs.loc[:,'F_SD'],Red_wt_abs.loc[:,'F']+Red_wt_abs.loc[:,'F_SD'], alpha=0.2, edgecolor='#ff827b',facecolor='#ffd6d1' )

plt.axis([0, 250, 0.05, 0.55])
plt.xlabel('Time after FeGP addition (s)', fontfamily='Arial' , weight='bold', size=10)
plt.ylabel('Absorbance 336nm',fontfamily='Arial' , weight='bold', size=10)              
plt.xticks(fontsize=8,fontfamily='Arial')
plt.yticks(fontsize=8,fontfamily='Arial')
#fig_red_1.annotate('A', xy=(0.01,0.9), xycoords="axes fraction", fontfamily='Arial' , weight='bold', size=12)
#fig_red_1.text(-0.1, 1.1, 'A', transform=fig_red_1.transAxes, size=12, weight='bold')

plt.savefig(r'C:\Users\Francisco\ownCloud\ScienceData\Library\pHmd\figures\wt_red.png',dpi=300,bbox_inches='tight')                
# plt.show()    



# #L150A
fig2=plt.figure(dpi=1200)
fig_red_m=fig2.add_subplot(221)
plt.plot(Red_m_abs.loc[:,'Time'],Red_m_abs.loc[:,'A'],'.',color='#0B2B42', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(Red_m_abs.loc[:,'Time'],Red_m_abs.loc[:,'B'],'+',color='#014270', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(Red_m_abs.loc[:,'Time'],Red_m_abs.loc[:,'C'],'^',color='#218CD9', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(Red_m_abs.loc[:,'Time'],Red_m_abs.loc[:,'D'],'s',color='#5CB4F2', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(Red_m_abs.loc[:,'Time'],Red_m_abs.loc[:,'E'],'o',color='#78BEF0', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.plot(Red_m_abs.loc[:,'Time'],Red_m_abs.loc[:,'F'],'d',color='#C8E4F9', markeredgecolor='black',markersize=2,mew =0.5, markevery=4, ls='')
plt.fill_between(Red_m_abs.loc[:,'Time'],Red_m_abs.loc[:,'A']-Red_m_abs.loc[:,'A_SD'],Red_m_abs.loc[:,'A']+Red_m_abs.loc[:,'A_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )
plt.fill_between(Red_m_abs.loc[:,'Time'],Red_m_abs.loc[:,'B']-Red_m_abs.loc[:,'B_SD'],Red_m_abs.loc[:,'B']+Red_m_abs.loc[:,'B_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )    
plt.fill_between(Red_m_abs.loc[:,'Time'],Red_m_abs.loc[:,'C']-Red_m_abs.loc[:,'C_SD'],Red_m_abs.loc[:,'C']+Red_m_abs.loc[:,'C_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )
plt.fill_between(Red_m_abs.loc[:,'Time'],Red_m_abs.loc[:,'D']-Red_m_abs.loc[:,'D_SD'],Red_m_abs.loc[:,'D']+Red_m_abs.loc[:,'D_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )
plt.fill_between(Red_m_abs.loc[:,'Time'],Red_m_abs.loc[:,'E']-Red_m_abs.loc[:,'E_SD'],Red_m_abs.loc[:,'E']+Red_m_abs.loc[:,'E_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )
plt.fill_between(Red_m_abs.loc[:,'Time'],Red_m_abs.loc[:,'F']-Red_m_abs.loc[:,'F_SD'],Red_m_abs.loc[:,'F']+Red_m_abs.loc[:,'F_SD'], alpha=0.3, edgecolor='#EDF6FD',facecolor='#EDF6FD' )


plt.axis([0, 250, 0.05, 0.55])
plt.xlabel('Time after FeGP addition (s)', fontfamily='Arial' , weight='bold', size=10)
plt.ylabel('Absorbance 336nm',fontfamily='Arial' , weight='bold', size=10)              
plt.xticks(fontsize=8,fontfamily='Arial')
plt.yticks(fontsize=8,fontfamily='Arial')

plt.savefig(r'C:\Users\Francisco\ownCloud\ScienceData\Library\pHmd\figures\m_red.png',dpi=300,bbox_inches='tight')                
#plt.show()    