# Import libraries
import pandas as pd
import numpy as np
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
#set.sns()

#Display
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)
pd.options.display.float_format= '{:.2f}'.format

# First Update - 20hs
df20 = pd.read_csv('test-2021-09-07--20-33-53.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df20.sort_index(inplace=True)
#df20.head()

# Second Update - 21hs
df21 = pd.read_csv('test-2021-09-07--21-33-58.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df21.sort_index(inplace=True)
#df21.head()

#Third Update - 22hs
df22 = pd.read_csv('test-2021-09-07--22-34-05.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df22.sort_index(inplace=True)
#df22.head()

#Fourth Update - 23hs
df23 = pd.read_csv('test-2021-09-07--23-34-14.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df23.sort_index(inplace=True)
#df23.head()

######### Other Day // 2021-09-08 ##########

# 0 hs
df0 = pd.read_csv('test-2021-09-08--00-34-23.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df0.sort_index(inplace=True)
#df0.head()

# 1 hs
df1 = pd.read_csv('test-2021-09-08--01-34-28.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df1.sort_index(inplace=True)
#df1.head()

# 2 hs
df2 = pd.read_csv('test-2021-09-08--02-34-33.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df2.sort_index(inplace=True)
#df2.head()

# 3 hs
df3 = pd.read_csv('test-2021-09-08--03-34-38.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df3.sort_index(inplace=True)
#df3.head()

# 6 hs
df6 = pd.read_csv('test-2021-09-08--06-34-44.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df6.sort_index(inplace=True)
#df6.head()

# 7 hs
df7 = pd.read_csv('test-2021-09-08--07-34-50.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df7.sort_index(inplace=True)
#df7.head()

# 8 hs
df8 = pd.read_csv('test-2021-09-08--08-34-56.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df8.sort_index(inplace=True)
#df8.head()

# 9 hs
df9 = pd.read_csv('test-2021-09-08--09-35-02.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df9.sort_index(inplace=True)
#df9.head()

# 10 hs
df10 = pd.read_csv('test-2021-09-08--10-35-06.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df10.sort_index(inplace=True)
#df10.head()

# 11 hs
df11 = pd.read_csv('test-2021-09-08--11-35-12.csv',usecols=[0,1,2,3,4,5,6,7,8,9,10,11,15,20,21,22])
df11.sort_index(inplace=True)
#df11.head()

#################################################################################

df_20 = df20[df20['Date'] == '2021-09-07 20:00:00']
df_21 = df21[df21['Date'] == '2021-09-07 20:00:00']
df_22 = df22[df22['Date'] == '2021-09-07 20:00:00']
df_23 = df23[df23['Date'] == '2021-09-07 20:00:00']

Rows = pd.DataFrame()
Rows['20hs'] = [df_20.shape[0]]
Rows['21hs'] = [df_21.shape[0]]
Rows['22hs'] = [df_22.shape[0]]
Rows['23hs'] = [df_23.shape[0]]
Rows

Installs=df_20['Installs'].describe().reset_index()
Installs.set_index('index',inplace=True)
Installs['21hs']=df_21['Installs'].describe()
Installs['22hs']=df_22['Installs'].describe()
Installs['23hs']=df_23['Installs'].describe()
Installs

Sessions=df_20['Sessions'].describe().reset_index()
Sessions.set_index('index',inplace=True)
Sessions['21hs']=df_21['Sessions'].describe()
Sessions['22hs']=df_22['Sessions'].describe()
Sessions['23hs']=df_23['Sessions'].describe()
Sessions

Revenue=df_20['Revenue'].describe().reset_index()
Revenue.set_index('index',inplace=True)
Revenue['21hs']=df_21['Revenue'].describe()
Revenue['22hs']=df_22['Revenue'].describe()
Revenue['23hs']=df_23['Revenue'].describe()
Revenue

region=df_20['region'].value_counts().reset_index()
region.set_index('index',inplace=True)
region['21hs']=df_21['region'].value_counts()
region['22hs']=df_22['region'].value_counts()
region['23hs']=df_23['region'].value_counts()
region

##### Test - Hour 0:00 ########################

df_0 = df0[df0['Date'] == '2021-09-08 00:00:00']
df_1 = df1[df1['Date'] == '2021-09-08 00:00:00']
df_2 = df2[df2['Date'] == '2021-09-08 00:00:00']
df_3 = df3[df3['Date'] == '2021-09-08 00:00:00']
df_6 = df6[df6['Date'] == '2021-09-08 00:00:00']
df_7 = df7[df7['Date'] == '2021-09-08 00:00:00']
df_8 = df8[df8['Date'] == '2021-09-08 00:00:00']
df_9 = df9[df9['Date'] == '2021-09-08 00:00:00']
df_10 = df10[df10['Date'] == '2021-09-08 00:00:00']
df_11 = df11[df11['Date'] == '2021-09-08 00:00:00']


Nulls = pd.DataFrame()
Nulls['0hs'] = [df_0.shape[0]]
Nulls['1hs'] = [df_1.shape[0]]
Nulls['2hs'] = [df_2.shape[0]]
Nulls['3hs'] = [df_3.shape[0]]
Nulls['6hs'] = [df_6.shape[0]]
Nulls['7hs'] = [df_7.shape[0]]
Nulls['8hs'] = [df_8.shape[0]]
Nulls['9hs'] = [df_9.shape[0]]
Nulls['10hs'] = [df_10.shape[0]]
Nulls['11hs'] = [df_11.shape[0]]
Nulls



Installs=df_0['Installs'].describe().reset_index()
Installs.set_index('index',inplace=True)
Installs['1hs']=df_1['Installs'].describe()
Installs['2hs']=df_2['Installs'].describe()
Installs['3hs']=df_3['Installs'].describe()
Installs['6hs']=df_6['Installs'].describe()
Installs['7hs']=df_7['Installs'].describe()
Installs['8hs']=df_8['Installs'].describe()
Installs['9hs']=df_9['Installs'].describe()
Installs['10hs']=df_10['Installs'].describe()
Installs['11hs']=df_11['Installs'].describe()
Installs


Sessions=df_0['Sessions'].describe().reset_index()
Sessions.set_index('index',inplace=True)
Sessions['1hs']=df_1['Sessions'].describe()
Sessions['2hs']=df_2['Sessions'].describe()
Sessions['3hs']=df_3['Sessions'].describe()
Sessions['6hs']=df_6['Sessions'].describe()
Sessions['7hs']=df_7['Sessions'].describe()
Sessions['8hs']=df_8['Sessions'].describe()
Sessions['9hs']=df_9['Sessions'].describe()
Sessions['10hs']=df_10['Sessions'].describe()
Sessions['11hs']=df_11['Sessions'].describe()
Sessions

Revenue=df_0['Revenue'].describe().reset_index()
Revenue.set_index('index',inplace=True)
Revenue['1hs']=df_1['Revenue'].describe()
Revenue['2hs']=df_2['Revenue'].describe()
Revenue['3hs']=df_3['Revenue'].describe()
Revenue['6hs']=df_6['Revenue'].describe()
Revenue['7hs']=df_7['Revenue'].describe()
Revenue['8hs']=df_8['Revenue'].describe()
Revenue['9hs']=df_9['Revenue'].describe()
Revenue['10hs']=df_10['Revenue'].describe()
Revenue['11hs']=df_11['Revenue'].describe()
Revenue


region=df_0['region'].value_counts().reset_index()
region.set_index('index',inplace=True)
region['1hs']=df_1['region'].value_counts()
region['2hs']=df_2['region'].value_counts()
region['3hs']=df_3['region'].value_counts()
region['6hs']=df_6['region'].value_counts()
region['7hs']=df_7['region'].value_counts()
region['8hs']=df_8['region'].value_counts()
region['9hs']=df_9['region'].value_counts()
region['10hs']=df_10['region'].value_counts()
region['11hs']=df_11['region'].value_counts()
region

partner=df_0['Partner'].value_counts().reset_index()
partner.set_index('index',inplace=True)
partner['1hs']=df_1['Partner'].value_counts()
partner['2hs']=df_2['Partner'].value_counts()
partner['3hs']=df_3['Partner'].value_counts()
partner['6hs']=df_6['Partner'].value_counts()
partner['7hs']=df_7['Partner'].value_counts()
partner['8hs']=df_8['Partner'].value_counts()
partner['9hs']=df_9['Partner'].value_counts()
partner['10hs']=df_10['Partner'].value_counts()
partner['11hs']=df_11['Partner'].value_counts()
partner


##### Test - Hour 01:00 ########################

df_1 = df1[df1['Date'] == '2021-09-08 01:00:00']
df_2 = df2[df2['Date'] == '2021-09-08 01:00:00']
df_3 = df3[df3['Date'] == '2021-09-08 01:00:00']
df_6 = df6[df6['Date'] == '2021-09-08 01:00:00']
df_7 = df7[df7['Date'] == '2021-09-08 01:00:00']
df_8 = df8[df8['Date'] == '2021-09-08 01:00:00']
df_9 = df9[df9['Date'] == '2021-09-08 01:00:00']
df_10 = df10[df10['Date'] == '2021-09-08 01:00:00']
df_11 = df11[df11['Date'] == '2021-09-08 01:00:00']


Nulls = pd.DataFrame()
Nulls['1hs'] = [df_1.shape[0]]
Nulls['2hs'] = [df_2.shape[0]]
Nulls['3hs'] = [df_3.shape[0]]
Nulls['6hs'] = [df_6.shape[0]]
Nulls['7hs'] = [df_7.shape[0]]
Nulls['8hs'] = [df_8.shape[0]]
Nulls['9hs'] = [df_9.shape[0]]
Nulls['10hs'] = [df_10.shape[0]]
Nulls['11hs'] = [df_11.shape[0]]
Nulls


Sessions=df_1['Sessions'].describe().reset_index()
Sessions.set_index('index',inplace=True)
Sessions['2hs']=df_2['Sessions'].describe()
Sessions['3hs']=df_3['Sessions'].describe()
Sessions['6hs']=df_6['Sessions'].describe()
Sessions['7hs']=df_7['Sessions'].describe()
Sessions['8hs']=df_8['Sessions'].describe()
Sessions['9hs']=df_9['Sessions'].describe()
Sessions['10hs']=df_10['Sessions'].describe()
Sessions['11hs']=df_11['Sessions'].describe()
Sessions


Installs=df_1['Installs'].describe().reset_index()
Installs.set_index('index',inplace=True)
Installs['2hs']=df_2['Installs'].describe()
Installs['3hs']=df_3['Installs'].describe()
Installs['6hs']=df_6['Installs'].describe()
Installs['7hs']=df_7['Installs'].describe()
Installs['8hs']=df_8['Installs'].describe()
Installs['9hs']=df_9['Installs'].describe()
Installs['10hs']=df_10['Installs'].describe()
Installs['11hs']=df_11['Installs'].describe()
Installs

Revenue=df_1['Revenue'].describe().reset_index()
Revenue.set_index('index',inplace=True)
Revenue['2hs']=df_2['Revenue'].describe()
Revenue['3hs']=df_3['Revenue'].describe()
Revenue['6hs']=df_6['Revenue'].describe()
Revenue['7hs']=df_7['Revenue'].describe()
Revenue['8hs']=df_8['Revenue'].describe()
Revenue['9hs']=df_9['Revenue'].describe()
Revenue['10hs']=df_10['Revenue'].describe()
Revenue['11hs']=df_11['Revenue'].describe()
Revenue


region=df_1['region'].value_counts().reset_index()
region.set_index('index',inplace=True)
region['2hs']=df_2['region'].value_counts()
region['3hs']=df_3['region'].value_counts()
region['6hs']=df_6['region'].value_counts()
region['7hs']=df_7['region'].value_counts()
region['8hs']=df_8['region'].value_counts()
region['9hs']=df_9['region'].value_counts()
region['10hs']=df_10['region'].value_counts()
region['11hs']=df_11['region'].value_counts()
region

partner=df_1['Partner'].value_counts().reset_index()
partner.set_index('index',inplace=True)
partner['2hs']=df_2['Partner'].value_counts()
partner['3hs']=df_3['Partner'].value_counts()
partner['6hs']=df_6['Partner'].value_counts()
partner['7hs']=df_7['Partner'].value_counts()
partner['8hs']=df_8['Partner'].value_counts()
partner['9hs']=df_9['Partner'].value_counts()
partner['10hs']=df_10['Partner'].value_counts()
partner['11hs']=df_11['Partner'].value_counts()
partner


##### Test - Hour 02:00 ########################

df_2 = df2[df2['Date'] == '2021-09-08 02:00:00']
df_3 = df3[df3['Date'] == '2021-09-08 02:00:00']
df_6 = df6[df6['Date'] == '2021-09-08 02:00:00']
df_7 = df7[df7['Date'] == '2021-09-08 02:00:00']
df_8 = df8[df8['Date'] == '2021-09-08 02:00:00']
df_9 = df9[df9['Date'] == '2021-09-08 02:00:00']
df_10 = df10[df10['Date'] == '2021-09-08 02:00:00']
df_11 = df11[df11['Date'] == '2021-09-08 02:00:00']


Nulls = pd.DataFrame()

Nulls['2hs'] = [df_2.shape[0]]
Nulls['3hs'] = [df_3.shape[0]]
Nulls['6hs'] = [df_6.shape[0]]
Nulls['7hs'] = [df_7.shape[0]]
Nulls['8hs'] = [df_8.shape[0]]
Nulls['9hs'] = [df_9.shape[0]]
Nulls['10hs'] = [df_10.shape[0]]
Nulls['11hs'] = [df_11.shape[0]]
Nulls


Sessions=df_2['Sessions'].describe().reset_index()
Sessions.set_index('index',inplace=True)
Sessions['3hs']=df_3['Sessions'].describe()
Sessions['6hs']=df_6['Sessions'].describe()
Sessions['7hs']=df_7['Sessions'].describe()
Sessions['8hs']=df_8['Sessions'].describe()
Sessions['9hs']=df_9['Sessions'].describe()
Sessions['10hs']=df_10['Sessions'].describe()
Sessions['11hs']=df_11['Sessions'].describe()
Sessions


Installs=df_2['Installs'].describe().reset_index()
Installs.set_index('index',inplace=True)
Installs['3hs']=df_3['Installs'].describe()
Installs['6hs']=df_6['Installs'].describe()
Installs['7hs']=df_7['Installs'].describe()
Installs['8hs']=df_8['Installs'].describe()
Installs['9hs']=df_9['Installs'].describe()
Installs['10hs']=df_10['Installs'].describe()
Installs['11hs']=df_11['Installs'].describe()
Installs


Revenue=df_2['Revenue'].describe().reset_index()
Revenue.set_index('index',inplace=True)
Revenue['3hs']=df_3['Revenue'].describe()
Revenue['6hs']=df_6['Revenue'].describe()
Revenue['7hs']=df_7['Revenue'].describe()
Revenue['8hs']=df_8['Revenue'].describe()
Revenue['9hs']=df_9['Revenue'].describe()
Revenue['10hs']=df_10['Revenue'].describe()
Revenue['11hs']=df_11['Revenue'].describe()
Revenue


region=df_2['region'].value_counts().reset_index()
region.set_index('index',inplace=True)
region['3hs']=df_3['region'].value_counts()
region['6hs']=df_6['region'].value_counts()
region['7hs']=df_7['region'].value_counts()
region['8hs']=df_8['region'].value_counts()
region['9hs']=df_9['region'].value_counts()
region['10hs']=df_10['region'].value_counts()
region['11hs']=df_11['region'].value_counts()
region

partner=df_2['Partner'].value_counts().reset_index()
partner.set_index('index',inplace=True)
partner['3hs']=df_3['Partner'].value_counts()
partner['6hs']=df_6['Partner'].value_counts()
partner['7hs']=df_7['Partner'].value_counts()
partner['8hs']=df_8['Partner'].value_counts()
partner['9hs']=df_9['Partner'].value_counts()
partner['10hs']=df_10['Partner'].value_counts()
partner['11hs']=df_11['Partner'].value_counts()
partner

##### Test - Hour 03:00 ########################

df_2 = df2[df2['Date'] == '2021-09-08 03:00:00']
df_3 = df3[df3['Date'] == '2021-09-08 03:00:00']
df_6 = df6[df6['Date'] == '2021-09-08 03:00:00']
df_7 = df7[df7['Date'] == '2021-09-08 03:00:00']
df_8 = df8[df8['Date'] == '2021-09-08 03:00:00']
df_9 = df9[df9['Date'] == '2021-09-08 03:00:00']
df_10 = df10[df10['Date'] == '2021-09-08 03:00:00']
df_11 = df11[df11['Date'] == '2021-09-08 03:00:00']

Nulls = pd.DataFrame()
Nulls['3hs'] = [df_3.shape[0]]
Nulls['6hs'] = [df_6.shape[0]]
Nulls['7hs'] = [df_7.shape[0]]
Nulls['8hs'] = [df_8.shape[0]]
Nulls['9hs'] = [df_9.shape[0]]
Nulls['10hs'] = [df_10.shape[0]]
Nulls['11hs'] = [df_11.shape[0]]
Nulls


Sessions=df_3['Sessions'].describe().reset_index()
Sessions.set_index('index',inplace=True)
Sessions['6hs']=df_6['Sessions'].describe()
Sessions['7hs']=df_7['Sessions'].describe()
Sessions['8hs']=df_8['Sessions'].describe()
Sessions['9hs']=df_9['Sessions'].describe()
Sessions['10hs']=df_10['Sessions'].describe()
Sessions['11hs']=df_11['Sessions'].describe()
Sessions


Installs=df_3['Installs'].describe().reset_index()
Installs.set_index('index',inplace=True)
Installs['6hs']=df_6['Installs'].describe()
Installs['7hs']=df_7['Installs'].describe()
Installs['8hs']=df_8['Installs'].describe()
Installs['9hs']=df_9['Installs'].describe()
Installs['10hs']=df_10['Installs'].describe()
Installs['11hs']=df_11['Installs'].describe()
Installs

Revenue=df_3['Revenue'].describe().reset_index()
Revenue.set_index('index',inplace=True)
Revenue['6hs']=df_6['Revenue'].describe()
Revenue['7hs']=df_7['Revenue'].describe()
Revenue['8hs']=df_8['Revenue'].describe()
Revenue['9hs']=df_9['Revenue'].describe()
Revenue['10hs']=df_10['Revenue'].describe()
Revenue['11hs']=df_11['Revenue'].describe()
Revenue


region=df_3['region'].value_counts().reset_index()
region.set_index('index',inplace=True)
region['6hs']=df_6['region'].value_counts()
region['7hs']=df_7['region'].value_counts()
region['8hs']=df_8['region'].value_counts()
region['9hs']=df_9['region'].value_counts()
region['10hs']=df_10['region'].value_counts()
region['11hs']=df_11['region'].value_counts()
region

partner=df_3['Partner'].value_counts().reset_index()
partner.set_index('index',inplace=True)
partner['6hs']=df_6['Partner'].value_counts()
partner['7hs']=df_7['Partner'].value_counts()
partner['8hs']=df_8['Partner'].value_counts()
partner['9hs']=df_9['Partner'].value_counts()
partner['10hs']=df_10['Partner'].value_counts()
partner['11hs']=df_11['Partner'].value_counts()
partner


###########################################################################
#Test1
df1.tail()
df_test1 = df1[df1['Date'] == '2021-09-07 20:00:00']
df_test2 = df2[df2['Date'] == '2021-09-07 20:00:00']
df_test3 = df3[df3['Date'] == '2021-09-07 20:00:00']
df_test4 = df4[df4['Date'] == '2021-09-07 20:00:00']

df_test1.head()
df_test2.head()

df_test1.shape
df_test2.shape
df_test3.shape
df_test4.shape

#Test 2
df_test5 = df2[df2['Date'] == '2021-09-07 21:00:00']
df_test6 = df3[df3['Date'] == '2021-09-07 21:00:00']
df_test7 = df4[df4['Date'] == '2021-09-07 21:00:00']

df_test5.shape
df_test6.shape
df_test7.shape

#test3
df_test8 = df3[df3['Date'] == '2021-09-07 22:00:00']
df_test9 = df4[df4['Date'] == '2021-09-07 22:00:00']

df_test8.shape
df_test9.shape


#Functions

def nullValues(dataSet):
      #analizo completitud de datos para ver columnas a borrar o completar
    x = dataSet.isna().sum()
    if len(x[x>0])>0:
        d = {'NullRecord': x[x>0], 'TotalRecord': dataSet.shape[0]}
        y = pd.DataFrame(d)
        y["CompleteRecord"] = y["TotalRecord"] - y["NullRecord"]
        y["Complete %"] = round((y["CompleteRecord"] / y["TotalRecord"] ) * 100,2)
        y["Empy %"] = 100 - y["Complete %"] 
    return y.sort_values("NullRecord",ascending=True)


def Zerovalues(df):
    d = {'TotalRecord': df.shape[0], '#Zeros':0, '%Zeros':0}
    y = pd.DataFrame(d, index= df.columns)
     
    for c  in df.columns:
         y.loc[c,"#Zeros"] = len(df[df[c]==0])
         y.loc[c,"%Zeros"] = round((y.loc[c,"#Zeros"] / y.loc[c,"TotalRecord"] ),2) * 100
    return y[y["#Zeros"]>0]


nullValues(df_test3)
nullValues(df_test4)


Zerovalues(df_test3)
Zerovalues(df_test4)

null=df_test3.isnull().sum().reset_index()
null.set_index('index',inplace=True)
null[1]=df_test4.isnull().sum()
null['Diff'] = null[1] - null[0]
null


def neg(data,variables):
    for i in variables:
        n=data[i]<0
        if n.any() == True:
            print(f'The column {i} has {n.shape[0]} negative values.')

print(uniqueRate(df_test4))

variables = ['Tracker','Campaign','region','Country','Platform','Device Type','OS Name','Partner']


# Differences in numerical variable 
Clicks=df_test3['Clicks'].describe().reset_index()
Clicks.set_index('index',inplace=True)
Clicks['Clicks2']=df_test4['Clicks'].describe()
Clicks['Diff'] = Clicks['Clicks']-Clicks['Clicks2']
Clicks

Impressions=df_test3['Impressions'].describe().reset_index()
Impressions.set_index('index',inplace=True)
Impressions['Impressions2']=df_test4['Impressions'].describe()
Impressions['Diff'] = Impressions['Impressions2']-Impressions['Impressions']
Impressions


Installs=df_test3['Installs'].describe().reset_index()
Installs.set_index('index',inplace=True)
Installs['Installs2']=df_test4['Installs'].describe()
Installs['Diff'] = Installs['Installs2']-Installs['Installs']
Installs


Sessions=df_test3['Sessions'].describe().reset_index()
Sessions.set_index('index',inplace=True)
Sessions['Sessions2']=df_test4['Sessions'].describe()
Sessions['Diff'] = Sessions['Sessions2']-Sessions['Sessions']
Sessions


Revenue=df_test3['Revenue'].describe().reset_index()
Revenue.set_index('index',inplace=True)
Revenue['Revenue2']=df_test4['Revenue'].describe()
Revenue['Diff'] = Revenue['Revenue2']-Revenue['Revenue']
Revenue


# Differences in categorical variable 
a=df_test3['Partner'].value_counts().reset_index()
a.set_index('index',inplace=True)
a['Partner2']=df_test4['Partner'].value_counts()
a['Diff'] = a['Partner2'] - a['Partner']
a

b=df_test3['OS Name'].value_counts().reset_index()
b.set_index('index',inplace=True)
b['OS Name2']=df_test4['OS Name'].value_counts()
b['Diff'] = b['OS Name2'] - b['OS Name']
b

c=df_test3['Platform'].value_counts().reset_index()
c.set_index('index',inplace=True)
c['Platform2']=df_test4['Platform'].value_counts()
c['Diff'] = c['Platform2'] - c['Platform']
c

d=df_test3['region'].value_counts().reset_index()
d.set_index('index',inplace=True)
d['region2']=df_test4['region'].value_counts()
d['Diff'] = d['region2'] - d['region']
d


# Functions to create BoxPlots

def Boxplot(df,lista):
    for i in lista:
        if(df[i].dtype !="object"):
            plt.figure(figsize=(10,5))
            plt.title(i)
            sns.boxplot(x=df[i])



Boxplot(df_test3,numerics)
Boxplot(df_test4,numerics)