import pandas as pd
fout1 = open("collect_sub1.csv", "a")
fout2 = open("collect_term1.csv", "a")
for i in range(0,1):
    filename = 'agrregate' + str(i) + '.csv'
    tmp = pd.read_csv(filename)
    tmp1=tmp[tmp['Event Type']==0].drop(['Event Type'],axis=1)

    tmp2 = tmp[tmp['Event Type']==4].drop(['Event Type'],axis=1)
    if (i == 0):
        tmp1.columns = ['Time', 'JobID', 'TaskID']
        tmp2.columns = ['Time', 'JobID', 'TaskID']
        tmp1.to_csv(fout1,index=False)
        tmp2.to_csv(fout2,index=False)
    else:
        tmp1.to_csv(fout1,header=False,index=False)
        tmp2.to_csv(fout2, header=False,index=False)

fout1.close()
fout2.close()


