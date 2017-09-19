import  pandas as pd
import numpy as np

# daily_count=pd.DataFrame(np.zeros(29,dtype=np.int64),columns=['Req Num'])
# day_len = 1e6*60*60*24
# for i in range(0,25):
#         filename='agrregate'+str(i)+'.csv'
#         tmp= pd.read_csv(filename)
#         tmp=tmp[tmp['Event Type']==0]
#         first=tmp.iloc[0]['Time']
#         first_day = np.floor((first-600*1e6)/day_len).astype(int)
#         last=tmp.iloc[tmp.shape[0]-1]['Time']
#         last_day=np.ceil((last-600*1e6)/day_len).astype(int)
#
#         for day in range(first_day,last_day):
#             start = 600*1e6+day*day_len
#             end = 600*1e6+(day+1)*day_len
#             tmp_count = tmp[(tmp['Time']>=start) & (tmp['Time']<end)].shape[0]
#             daily_count.iloc[day]['Req Num']=daily_count.iloc[day]['Req Num']+tmp_count
# print(daily_count)
# daily_count.to_csv('daily_count.csv',index=False)


# daily_kill=pd.DataFrame(np.zeros(29,dtype=np.int64),columns=['Req Num'])
# day_len = 1e6*60*60*24
# for i in range(0,25):
#         filename='agrregate'+str(i)+'.csv'
#         tmp= pd.read_csv(filename)
#         tmp=tmp[(tmp['Event Type']==5)|(tmp['Event Type']==3)|(tmp['Event Type']==6)]
#         first=tmp.iloc[0]['Time']
#         first_day = np.floor((first-600*1e6)/day_len).astype(int)
#         last=tmp.iloc[tmp.shape[0]-1]['Time']
#         last_day=np.ceil((last-600*1e6)/day_len).astype(int)
#
#         for day in range(first_day,last_day):
#             start = 600*1e6+day*day_len
#             end = 600*1e6+(day+1)*day_len
#             tmp_count = tmp[(tmp['Time']>=start) & (tmp['Time']<end)].shape[0]
#             daily_kill.iloc[day]['Req Num']=daily_kill.iloc[day]['Req Num']+tmp_count
# print(daily_kill)
# daily_kill.to_csv('daily_kill.csv')



#
#
# hourly_count=pd.DataFrame(np.zeros(29*24+1,dtype=np.int64),columns=['Req Num'])
# hour_len = 1e6*60*60
# for i in range(0,25):
#         filename='agrregate'+str(i)+'.csv'
#         tmp= pd.read_csv(filename)
#         tmp = tmp[tmp['Event Type'] == 0]
#         first=tmp.iloc[0]['Time']
#         first_hour = np.floor((first-600*1e6)/hour_len).astype(int)
#         last=tmp.iloc[tmp.shape[0]-1]['Time']
#         last_hour=np.ceil((last-600*1e6)/hour_len).astype(int)
#
#         for hour in range(first_hour,last_hour+1):
#             start = 600*1e6+hour*hour_len
#             end = 600*1e6+(hour+1)*hour_len
#             tmp_count = tmp[(tmp['Time']>=start) & (tmp['Time']<end)].shape[0]
#             hourly_count.iloc[hour]['Req Num']=hourly_count.iloc[hour]['Req Num']+tmp_count
# print(hourly_count)
# hourly_count.to_csv('hourly_count.csv',index=False)


# halfhour_count=pd.DataFrame(np.zeros(29*24*2+1,dtype=np.int64),columns=['Req Num'])
# halfhour_len = 1e6*60*60/2
# for i in range(0,25):
#         filename='agrregate'+str(i)+'.csv'
#         tmp= pd.read_csv(filename)
#         tmp = tmp[tmp['Event Type'] == 0]
#         first=tmp.iloc[0]['Time']
#         first_hfhour = np.floor((first-600*1e6)/halfhour_len).astype(int)
#         last=tmp.iloc[tmp.shape[0]-1]['Time']
#         last_hfhour=np.ceil((last-600*1e6)/halfhour_len).astype(int)
#
#         for hfhour in range(first_hfhour,last_hfhour+1):
#             start = 600*1e6+hfhour*halfhour_len
#             end = 600*1e6+(hfhour+1)*halfhour_len
#             tmp_count = tmp[(tmp['Time']>=start) & (tmp['Time']<end)].shape[0]
#             halfhour_count.iloc[hfhour]['Req Num']=halfhour_count.iloc[hfhour]['Req Num']+tmp_count
# #print(hourly_count)
# halfhour_count.to_csv('halfhour_count.csv',index=False)



# halfhour_count=pd.DataFrame(np.zeros(29*24*2+2,dtype=np.int64),columns=['Req Num'])
# halfhour_len = 1e6*60*60/2
# for i in range(0,25):
#         filename='agrregate'+str(i)+'.csv'
#         tmp= pd.read_csv(filename)
#         tmp = tmp[tmp['Event Type'] == 0]
#         first=tmp.iloc[0]['Time']
#         first_hfhour = np.floor((first)/halfhour_len).astype(int)
#         last=tmp.iloc[tmp.shape[0]-1]['Time']
#         last_hfhour=np.ceil((last)/halfhour_len).astype(int)
#
#         for hfhour in range(first_hfhour,last_hfhour+1):
#             start = hfhour*halfhour_len
#             end = (hfhour+1)*halfhour_len
#             tmp_count = tmp[(tmp['Time']>=start) & (tmp['Time']<end)].shape[0]
#             halfhour_count.iloc[hfhour]['Req Num']=halfhour_count.iloc[hfhour]['Req Num']+tmp_count
# #print(hourly_count)
# halfhour_count.to_csv('halfhour_count2.csv',index=False)


# hourly_kill=pd.DataFrame(np.zeros(29*24+1,dtype=np.int64),columns=['Req Num'])
# hour_len = 1e6*60*60
# for i in range(0,25):
#         filename='agrregate'+str(i)+'.csv'
#         tmp= pd.read_csv(filename)
#         tmp=tmp[(tmp['Event Type']==5)|(tmp['Event Type']==3)|(tmp['Event Type']==6)]
#         first=tmp.iloc[0]['Time']
#         first_hour = np.floor((first-600*1e6)/hour_len).astype(int)
#         last=tmp.iloc[tmp.shape[0]-1]['Time']
#         last_hour=np.ceil((last-600*1e6)/hour_len).astype(int)
#
#         for hour in range(first_hour,last_hour):
#             start = 600*1e6+hour*hour_len
#             end = 600*1e6+(hour+1)*hour_len
#             tmp_count = tmp[(tmp['Time']>=start) & (tmp['Time']<end)].shape[0]
#             hourly_kill.iloc[hour]['Req Num']=hourly_kill.iloc[hour]['Req Num']+tmp_count
#
# hourly_kill.to_csv('hourly_kill.csv',index=False)








# fivemin_count=pd.DataFrame(np.zeros(29*24*12+1,dtype=np.int64),columns=['Req Num'])
# fivemin_len = 1e6*60*5
# for i in range(0,25):
#         filename='agrregate'+str(i)+'.csv'
#         tmp= pd.read_csv(filename)
#         tmp = tmp[tmp['Event Type'] == 0]
#         first=tmp.iloc[0]['Time']
#         first_fivemin = np.floor((first-600*1e6)/fivemin_len).astype(int)
#         last=tmp.iloc[tmp.shape[0]-1]['Time']
#         last_fivemin=np.ceil((last-600*1e6)/fivemin_len).astype(int)
#
#         for fivemin in range(first_fivemin,last_fivemin+1):
#             start = 600*1e6+fivemin*fivemin_len
#             end = 600*1e6+(fivemin+1)*fivemin_len
#             tmp_count = tmp[(tmp['Time']>=start) & (tmp['Time']<end)].shape[0]
#             fivemin_count.iloc[fivemin]['Req Num']=fivemin_count.iloc[fivemin]['Req Num']+tmp_count
# #print(hourly_count)
# fivemin_count.to_csv('fivemin_count.csv',index=False)

# res=0
# for i in range(0,25):
#         filename='agrregate'+str(i)+'.csv'
#         tmp= pd.read_csv(filename)
#
#         for index, row in tmp.iterrows():
#             if(tmp.iloc[index]['Event Type']==5):
#                 checkpoint = index-1
#                 checkid = tmp.iloc[index]['Job ID']
#                 checktask = tmp.iloc[index]['Task Index']
#                 end = tmp.iloc[index]['Time']/1e6 -600
#                 while(checkpoint>0):
#                     if((tmp.iloc[checkpoint]['Job ID']==checkid) & (tmp.iloc[checkpoint]['Task Index']==checktask)
#                         & (tmp.iloc[checkpoint]['Event Type']==1)):
#                         start = tmp.iloc[checkpoint]['Time']/1e6 -600
#                         res = max(res,end-start)
#                         break
#                     checkpoint=checkpoint-1
#         print(res)

# count1=0
# count2=0
# for i in range(0,25):
#     filename = 'agrregate' + str(i) + '.csv'
#     tmp = pd.read_csv(filename)
#     count1=count1+tmp[tmp['Event Type']==0].shape[0]
#     count2 = count2 + tmp[(tmp['Event Type'] >= 2) & (tmp['Event Type'] <= 6)].shape[0]
# print(count1)
# print("\n")
# print(count2)


filename = 'agrregate' + str(0) + '.csv'
tmp = pd.read_csv(filename)
while(True):
    finish = tmp[(tmp['Event Type'] >= 2) & (tmp['Event Type'] <= 6)].iloc[0]



