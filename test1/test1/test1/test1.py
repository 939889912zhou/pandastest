
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

nb = pd.read_excel('D:/zhouty/sjj/playoff.xls')

season = list(np.sort(nb["赛季"].unique()))
season = season[2:] + season[:2]

nb["赛季"].unique()     #有多少种

season=list(np.sort(nb["赛季"].unique()))

nb['win']=nb["果"].map({"胜": 1, "负": 0})

winning=nb.groupby(["赛季"])["win"].mean()[season].values
nb2=nb[['赛季','win']]
sjsc=nb2.groupby('赛季').sum()  #赛季胜场
nb['统计']=nb["果"].map({"胜": 1, "负": 1})
nb3=nb[['赛季','统计']]
sjc=nb3.groupby('赛季').sum()   #赛季场
dfl=sjsc.join(sjc, how='inner')  #得分率
dfl['胜率']=dfl['win']/dfl['统计']

jg=dfl['胜率'].to_numpy()

i=85
hz=[]
while(i<=97):
    hz.append(str(i)+"-"+str(i+1))
    i=i+1
hz2=np.array(hz)
hz3=np.delete(hz2,8)

plt.figure(figsize=(10,8), dpi=80)
plt.plot(hz3,jg)
plt.show()