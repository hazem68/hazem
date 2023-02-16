#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns


# # we start with knowing the values in our data

# In[2]:


df = pd.read_csv("GoogleStock Price Updated.csv")
df.head(10)
df.describe()


# # we added difference column which is the difference between closed and opened values *above zero means closed > opended*
# # difference2 column which is the difference between closed and high value * equal zero means closed = high value*
# # difference3 column which is the difference between closed and low values * equal zero means closed = low value *

# In[3]:


df["difference"]=df["Close"]-df["Open"]
df["difference2"]=df["Close"]-df["High"]
df["difference3"]=df["Close"]-df["Low"]
df


# # grouping the dates to analyze each year separately  
# 
# 
# # the first year 2013 

# In[4]:


from datetime import datetime
first_year= df[(df.Date>="2013/01/02")&(df.Date<='2013/12/31')]
first_year['Date'] = pd.to_datetime(first_year.Date, format='%Y-%m-%d')
first_year['Date']=first_year["Date"].dt.strftime('%m')
first_year 


# In[5]:


first_year_copy=first_year.copy()


# In[6]:


first_year.groupby("Date").mean()


# # 2013 month's statistics 

# In[7]:


first_year_copy["Date"].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
first_year_copy


# # the list which closed values > opened 

# In[8]:


x=first_year["difference"]>0
x.value_counts()


# In[170]:


x=first_year["difference"]>0
sns.countplot(x).set(title="open < close")
sns.set_style("darkgrid")
sns.set_palette("RdBu")
sns.set_context("talk", font_scale=0.7)

plt.legend()


# # the list which closed = high value

# In[10]:


z=first_year["difference2"]==0
print(z.value_counts())
names= 'True','False'
values=[1,251]
colors=["#FF4040",'#FF4040']
plt.pie(z.value_counts())
plt.pie(values,labels=names,labeldistance=1.15,colors=colors)
plt.title("high = close")
plt.show()


# In[11]:


z=first_year["difference2"]==0
sns.countplot(z).set(title="high = close")
plt.show()


# # the list which closed = low value
# 

# In[12]:


e=first_year["difference3"]==0
print(e.value_counts())
names= 'True','False'
values=[0,252]
colors=['#00FFFF']
plt.pie(z.value_counts())
plt.pie(values,labels=names,colors=colors)
plt.title(" low = close")
plt.show()


# In[13]:


e=first_year["difference3"]==0
sns.countplot(e).set(title="low = close")
plt.show()


# # the mean of each month in 2013 year 

# In[14]:


first_year_copy.groupby("Date",sort=False).mean()


# # describing 2013 

# In[15]:


first_year.describe()


# # the second year 2014

# In[16]:


from datetime import datetime
second_year= df[(df.Date>="2014/01/02")&(df.Date<='2014/12/31')]
second_year['Date'] = pd.to_datetime(second_year.Date, format='%Y-%m-%d')
second_year['Date']=second_year["Date"].dt.strftime('%m')
second_year


# In[17]:


second_year_copy=second_year.copy()


# # 2014 month's statistics

# In[18]:


second_year_copy["Date"].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
second_year_copy


# # the list which closed values > opened

# In[19]:


x=second_year["difference"]>0
x.value_counts()


# In[171]:


x=second_year["difference"]>0
sns.countplot(x).set(title="open < close")
sns.set_style("darkgrid")
sns.set_palette("RdBu")
sns.set_context("talk", font_scale=0.7)

plt.legend()


# # the list which closed = high value

# In[21]:


z=second_year["difference2"]==0
print(z.value_counts())
names= 'True','False'
values=[1,251]
colors=["#FF4040",'#FF4040']
plt.pie(z.value_counts())
plt.pie(values,labels=names,labeldistance=1.15,colors=colors)
plt.title("high = close")
plt.show()


# In[22]:


z=second_year["difference2"]==0
sns.countplot(z).set(title="high = close")
plt.show()


# # the list which closed = low value

# In[23]:


e=second_year["difference3"]==0
print(e.value_counts())
names= 'True','False'
values=[1,252]
colors=['#00FFFF',"#000000"]
plt.pie(z.value_counts())
plt.pie(values,labels=names,colors=colors,labeldistance=1.15)
plt.title(" low = close")
plt.show()


# In[24]:


e=second_year["difference3"]==0
sns.countplot(e).set(title="low = close")
plt.show()


# # the mean of each month in 2014 year

# In[25]:


second_year_copy.groupby("Date",sort=False).mean()


# # describing 2014

# In[26]:


second_year.describe()


# # the third year 2015

# In[27]:


third_year= df[(df["Date"]>="2015/01/01")&(df["Date"]<="2015/12/31")]
third_year['Date'] = pd.to_datetime(third_year.Date, format='%Y-%m-%d')
third_year["Date"]=third_year["Date"].dt.strftime("%m")
third_year
               


# # 2015 month's statistics

# In[174]:


third_year_copy=third_year.copy()
third_year["Date"].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
third_year_copy 


# # the list which closed values > opened

# In[29]:


x = third_year_copy["difference"]>0
x.value_counts()


# In[172]:


x=third_year_copy["difference"]>0
sns.countplot(x).set(title="open < close")
sns.set_style("darkgrid")
sns.set_palette("RdBu")
sns.set_context("talk", font_scale=0.7)

plt.legend()


# # the list which closed = high value

# In[31]:


z=third_year["difference2"]==0
print(z.value_counts())
names= 'True','False'
values=[0,252]
colors=["#FF4040",'#FF4040']
plt.pie(z.value_counts())
plt.pie(values,labels=names,labeldistance=1.15,colors=colors)
plt.title("high = close")
plt.show()


# In[32]:


z=third_year["difference2"]==0
sns.countplot(z).set(title="high = close")
plt.show()


# # the list which closed = low value

# In[33]:


e=third_year["difference3"]==0
print(e.value_counts())
names= 'True','False'
values=[1,251]
colors=['#00FFFF',"#000000"]
plt.pie(z.value_counts())
plt.pie(values,labels=names,colors=colors,labeldistance=1.15)
plt.title(" low = close")
plt.show()


# In[34]:


e=third_year["difference3"]==0
sns.countplot(e).set(title="low = close")
plt.show()


# # the mean of each month in 2015 year

# In[175]:


third_year_copy.groupby("Date",sort=False).mean()


# # 2015 describtion 

# In[36]:


third_year.describe()


# # the fourth year 2016

# In[37]:


fourth_year= df[(df["Date"]>="2016/01/01")&(df["Date"]<="2016/12/31")]
fourth_year["Date"]=pd.to_datetime(fourth_year.Date, format='%Y-%m-%d')
fourth_year["Date"]=fourth_year["Date"].dt.strftime("%m")
fourth_year


# In[38]:


fourth_year_copy=fourth_year.copy()


# # 2016 month's statistics

# In[39]:


fourth_year_copy["Date"].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
fourth_year_copy


# # the list which closed values > opened

# In[40]:


x = fourth_year_copy["difference"]>0
x.value_counts()


# In[176]:


x=fourth_year_copy["difference"]>0
sns.countplot(x).set(title="open < close")
sns.set_style("darkgrid")
sns.set_palette("RdBu")
sns.set_context("talk", font_scale=0.7)

plt.legend()


# # the list which closed values = high 

# In[42]:


z=fourth_year["difference2"]==0
print(z.value_counts())
names= 'True','False'
values=[0,252]
colors=["#FF4040",'#FF4040']
plt.pie(z.value_counts())
plt.pie(values,labels=names,labeldistance=1.15,colors=colors)
plt.title("high = close")
plt.show()


# In[43]:


z=fourth_year["difference2"]==0
sns.countplot(z).set(title="high = close")
plt.show()


# # the list which closed values = low

# In[44]:


e=fourth_year["difference3"]==0
print(e.value_counts())
names= 'True','False'
values=[0,252]
colors=['#00FFFF',"#000000"]
plt.pie(z.value_counts())
plt.pie(values,labels=names,colors=colors,labeldistance=1.15)
plt.title(" low = close")
plt.show()


# In[45]:


e=fourth_year["difference3"]==0
sns.countplot(e).set(title="low = close")
plt.show()


# # the mean of each month in 2016 year

# In[46]:


fourth_year_copy.groupby("Date",sort=False).mean()


# # 2016 describtion 

# In[47]:


fourth_year.describe()


# # the fifth year 2017

# In[48]:


fifth_year= df[(df["Date"]>="2017/01/01")&(df["Date"]<="2017/12/31")]
fifth_year["Date"]=pd.to_datetime(fifth_year.Date, format='%Y-%m-%d')
fifth_year["Date"]=fifth_year["Date"].dt.strftime("%m")
fifth_year


# # 2017 month's statistics

# In[49]:


fifth_year_copy=fifth_year.copy()


# In[50]:


fifth_year_copy["Date"].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
fifth_year_copy


# # the list which closed values > opened

# In[51]:


x = fifth_year_copy["difference"]>0
x.value_counts()


# In[177]:


x=fifth_year_copy["difference"]>0
sns.countplot(x).set(title="open < close")
sns.set_style("darkgrid")
sns.set_palette("RdBu")
sns.set_context("talk", font_scale=0.7)

plt.legend()


# # the list which closed values = high

# In[53]:


z=fifth_year["difference2"]==0
print(z.value_counts())
names= 'True','False'
values=[0,251]
colors=["#FF4040",'#FF4040']
plt.pie(z.value_counts())
plt.pie(values,labels=names,labeldistance=1.15,colors=colors)
plt.title("high = close")
plt.show()


# In[54]:


z=fifth_year["difference2"]==0
sns.countplot(z).set(title="high = close")
plt.show()


# # the list which closed values = low 

# In[55]:


h=fifth_year["difference3"]==0
print(e.value_counts())
names= 'True','False'
values=[0,252]
colors=['#00FFFF',"#000000"]
plt.pie(z.value_counts())
plt.pie(values,labels=names,colors=colors,labeldistance=1.15)
plt.title(" low = close")
plt.show()


# In[56]:


h=fifth_year["difference3"]==0
sns.countplot(e).set(title="low = close")
plt.show()


# # the mean of each month in 2017 year

# In[57]:


fifth_year_copy.groupby("Date",sort=False).mean()


# # 2017 describtion 

# In[58]:


fifth_year.describe()


# # the sixth year 2018

# In[59]:


sixth_year=df[(df["Date"]>="2018/01/01")&(df["Date"]<='2018/12/31')]
sixth_year["Date"]=pd.to_datetime(sixth_year.Date, format='%Y-%m-%d')
sixth_year["Date"]=sixth_year["Date"].dt.strftime("%m")
sixth_year


# # 2018 month's statistics

# In[60]:


sixth_year_copy=sixth_year.copy()


# In[61]:


sixth_year_copy["Date"].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
sixth_year_copy


# # the list which closed values > opened

# In[62]:


x = sixth_year_copy["difference"]>0
x.value_counts()


# In[178]:


x=sixth_year_copy["difference"]>0
sns.countplot(x).set(title="open < close")
sns.set_style("darkgrid")
sns.set_palette("RdBu")
sns.set_context("talk", font_scale=0.7)

plt.legend()


# # the list which closed values = high

# In[64]:


z=sixth_year["difference2"]==0
print(z.value_counts())
names= 'True','False'
values=[2,249]
colors=["#FF4040",'#838B8B']
plt.pie(z.value_counts())
plt.pie(values,labels=names,labeldistance=1.15,colors=colors)
plt.title("high = close")
plt.show()


# In[65]:


z=sixth_year["difference2"]==0
sns.countplot(z).set(title="high = close")
plt.show()


# # the list which closed values = low

# In[66]:


h=sixth_year["difference3"]==0
print(e.value_counts())
names= 'True','False'
values=[0,252]
colors=['#00FFFF',"#000000"]
plt.pie(z.value_counts())
plt.pie(values,labels=names,colors=colors,labeldistance=1.15)
plt.title(" low = close")
plt.show()


# In[67]:


h=sixth_year["difference3"]==0
sns.countplot(e).set(title="low = close")
plt.show()


# # the mean of each month in 2018 year

# In[68]:


sixth_year_copy.groupby('Date',sort=False).mean()


# # 2018 describtion 

# In[69]:


sixth_year_copy.describe()


# # the seventh year 2019

# In[70]:


seventh_year=df[(df["Date"]>='2019/01/01')&(df["Date"]<='2019/12/31')]
seventh_year["Date"]=pd.to_datetime(seventh_year.Date, format='%Y-%m-%d')
seventh_year["Date"]=seventh_year["Date"].dt.strftime("%m")
seventh_year


# # 2019 month's statistics

# In[71]:


seventh_year_copy=seventh_year.copy()
seventh_year_copy['Date'].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
seventh_year_copy


# # the list which closed values > opened

# In[72]:


x = seventh_year_copy["difference"]>0
x.value_counts()


# In[179]:


x=seventh_year_copy["difference"]>0
sns.countplot(x).set(title="open < close")
sns.set_style("darkgrid")
sns.set_palette("RdBu")
sns.set_context("talk", font_scale=0.7)

plt.legend()


# # the list which closed values = high 

# In[74]:


z=seventh_year["difference2"]==0
print(z.value_counts())
names= 'True','False'
values=[2,250]
colors=["#FF4040",'#838B8B']
plt.pie(z.value_counts())
plt.pie(values,labels=names,labeldistance=1.15,colors=colors)
plt.title("high = close")
plt.show()


# In[75]:


z=seventh_year["difference2"]==0
sns.countplot(z).set(title="high = close")
plt.show()


# # the list which closed values = low

# In[76]:


h=seventh_year["difference3"]==0
print(e.value_counts())
names= 'True','False'
values=[0,252]
colors=['#00FFFF',"#000000"]
plt.pie(z.value_counts())
plt.pie(values,labels=names,colors=colors,labeldistance=1.15)
plt.title(" low = close")
plt.show()


# In[77]:


h=seventh_year["difference3"]==0
sns.countplot(e).set(title="low = close")
plt.show()


# # the mean of each month in 2019 year

# In[78]:


seventh_year_copy.groupby('Date',sort=False).mean()


# # 2019 describtion

# In[79]:


seventh_year.describe()


# # the eighth year 2020

# In[80]:


eighth_year=df[(df["Date"]>='2020/01/01')&(df["Date"]<='2020/12/31')]
eighth_year["Date"]=pd.to_datetime(eighth_year.Date, format='%Y-%m-%d')
eighth_year["Date"]=eighth_year["Date"].dt.strftime("%m")
eighth_year


# # 2020 month's statistics

# In[81]:


eighth_year_copy=eighth_year.copy()
eighth_year_copy['Date'].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
eighth_year_copy


# # the list which closed values > opened

# In[82]:


x = eighth_year_copy["difference"]>0
x.value_counts()


# In[180]:


x=eighth_year_copy["difference"]>0
sns.countplot(x).set(title="open < close")
sns.set_style("darkgrid")
sns.set_palette("RdBu")
sns.set_context("talk", font_scale=0.7)

plt.legend()


# # the list which closed values = high

# In[84]:


z=eighth_year["difference2"]==0
print(z.value_counts())
names= 'True','False'
values=[1,252]
colors=["#FF4040",'#838B8B']
plt.pie(z.value_counts())
plt.pie(values,labels=names,labeldistance=1.15,colors=colors)
plt.title("high = close")
plt.show()


# In[85]:


z=eighth_year["difference2"]==0
sns.countplot(z).set(title="high = close")
plt.show()


# # the list which closed values = low

# In[86]:


h=eighth_year["difference3"]==0
print(e.value_counts())
names= 'True','False'
values=[0,252]
colors=['#00FFFF',"#000000"]
plt.pie(z.value_counts())
plt.pie(values,labels=names,colors=colors,labeldistance=1.15)
plt.title(" low = close")
plt.show()


# In[87]:


h=eighth_year["difference3"]==0
sns.countplot(e).set(title="low = close")
plt.show()


# # the mean of each month in 2020 year

# In[88]:


eighth_year_copy.groupby('Date',sort=False).mean()


# # 2020 describtion 

# In[89]:


eighth_year.describe()


# # the ninth year 2021

# In[90]:


ninth_year=df[(df["Date"]>='2021/01/01')&(df["Date"]<='2021/12/31')]
ninth_year["Date"]=pd.to_datetime(ninth_year.Date, format='%Y-%m-%d')
ninth_year["Date"]=ninth_year["Date"].dt.strftime("%m")
ninth_year


# # 2021 month's statistics

# In[91]:


ninth_year_copy=ninth_year.copy()
ninth_year_copy['Date'].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
ninth_year_copy


# # the list which closed values > opened

# In[92]:


x = ninth_year_copy["difference"]>0
x.value_counts()


# In[181]:


x=ninth_year_copy["difference"]>0
sns.countplot(x).set(title="open < close")
sns.set_style("darkgrid")
sns.set_palette("RdBu")
sns.set_context("talk", font_scale=0.7)

plt.legend()


# # the list which closed values = high 

# In[94]:


z=ninth_year["difference2"]==0
print(z.value_counts())
names= 'True','False'
values=[1,251]
colors=["#FF4040",'#838B8B']
plt.pie(z.value_counts())
plt.pie(values,labels=names,labeldistance=1.15,colors=colors)
plt.title("high = close")
plt.show()


# In[95]:


z=ninth_year["difference2"]==0
sns.countplot(z).set(title="high = close")
plt.show()


# # the list which closed values = low

# In[96]:


h=ninth_year["difference3"]==0
print(e.value_counts())
names= 'True','False'
values=[0,252]
colors=['#00FFFF',"#000000"]
plt.pie(z.value_counts())
plt.pie(values,labels=names,colors=colors,labeldistance=1.15)
plt.title(" low = close")
plt.show()


# In[97]:


h=ninth_year["difference3"]==0
sns.countplot(e).set(title="low = close")
plt.show()


# # the mean of each month in 2021 year

# In[98]:


ninth_year_copy.groupby('Date',sort=False).mean()


# # 2021 describtion 

# In[99]:


ninth_year.describe()


# # the tenth year 2022

# In[100]:


tenth_year=df[(df["Date"]>='2022/01/01')&(df["Date"]<='2022/12/31')]
tenth_year["Date"]=pd.to_datetime(tenth_year.Date, format='%Y-%m-%d')
tenth_year["Date"]=tenth_year["Date"].dt.strftime("%m")
tenth_year


# # 2022 month's statistics

# In[101]:


tenth_year_copy=tenth_year.copy()
tenth_year_copy['Date'].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
tenth_year_copy


# # the list which closed values > opened

# In[102]:


x = tenth_year_copy["difference"]>0
x.value_counts()


# In[182]:


x=tenth_year_copy["difference"]>0
sns.countplot(x).set(title="open < close")
sns.set_style("darkgrid")
sns.set_palette("RdBu")
sns.set_context("talk", font_scale=0.7)

plt.legend()


# # the list which closed values = high 

# In[104]:


z=tenth_year["difference2"]==0
print(z.value_counts())
names= 'True','False'
values=[1,250]
colors=["#FF4040",'#838B8B']
plt.pie(z.value_counts())
plt.pie(values,labels=names,labeldistance=1.15,colors=colors)
plt.title("high = close")
plt.show()


# In[105]:


z=tenth_year["difference2"]==0
sns.countplot(z).set(title="high = close")
plt.show()


# # the list which closed values = low 

# In[106]:


h=tenth_year["difference3"]==0
print(e.value_counts())
names= 'True','False'
values=[0,252]
colors=['#00FFFF',"#000000"]
plt.pie(z.value_counts())
plt.pie(values,labels=names,colors=colors,labeldistance=1.15)
plt.title(" low = close")
plt.show()


# In[107]:


h=tenth_year["difference3"]==0
sns.countplot(e).set(title="low = close")
plt.show()


# # the mean of each month in 2022 year

# In[108]:


tenth_year_copy.groupby('Date',sort=False).mean()


# # 2022 describtion 

# In[109]:


tenth_year.describe()


#  # 2023 not complete yet 

# In[110]:


last_year=df[(df["Date"]>='2023/01/01')&(df["Date"]<='2023/12/31')]
last_year["Date"]=pd.to_datetime(last_year.Date, format='%Y-%m-%d')
last_year["Date"]=last_year["Date"].dt.strftime("%m")
last_year


# In[111]:


last_year_copy=last_year.copy()
last_year_copy['Date'].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
last_year_copy


# In[112]:


x = last_year_copy["difference"]>0
x.value_counts()


# In[113]:


x=last_year_copy["difference"]>0
sns.countplot(x).set(title="open > close")
sns.set_style("darkgrid")
sns.set_palette("RdBu")
sns.set_context("talk", font_scale=0.7)

plt.legend()


# In[114]:


z=last_year["difference2"]==0
print(z.value_counts())
names= 'True','False'
values=[0,18]
colors=["#FF4040",'#838B8B']
plt.pie(z.value_counts())
plt.pie(values,labels=names,labeldistance=1.15,colors=colors)
plt.title("high = close")
plt.show()


# In[115]:


z=last_year["difference2"]==0
sns.countplot(z).set(title="high = close")
plt.show()


# In[116]:


h=last_year["difference3"]==0
print(e.value_counts())
names= 'True','False'
values=[0,252]
colors=['#00FFFF',"#000000"]
plt.pie(z.value_counts())
plt.pie(values,labels=names,colors=colors,labeldistance=1.15)
plt.title(" low = close")
plt.show()


# In[117]:


h=last_year["difference3"]==0
sns.countplot(e).set(title="low = close")
plt.show()


# In[118]:


last_year_copy.groupby('Date',sort=False).mean()


# In[119]:


last_year.describe()


# In[183]:


plt.plot(["2013",'2014','2015','2016','2017','2018','2019','2020','2021','2022'],[119,118,129,125,136,127,129,142,134,122])
plt.title("closed values > opened")
plt.show()


# # notice at fig above the 2020 has the highst values 

# In[184]:


plt.plot(["2013",'2014','2015','2016','2017','2018','2019','2020','2021','2022'],[1,3,0,0,0,2,2,1,1,1])
plt.title("closed values = high")
plt.show()


# # notice at fig above the 2014 has the highst values

# In[186]:


plt.plot(["2013",'2014','2015','2016','2017','2018','2019','2020','2021','2022'],[0,1,1,0,0,0,0,0,0,1])
plt.title("closed values = low")
plt.show()


# # we grouped the years as periods 
# 
# # first period when google was added to alphabet
# 
# # second period when pichai was the CEO of google
# 
# #  third period when pichai was the CEO of alphabet

# In[120]:


the_first_period= df[(df.Date>="2013/01/02")&(df.Date<='2014/12/31')]
the_first_period["Date"]=pd.to_datetime(the_first_period.Date, format='%Y-%m-%d')
the_first_period["Date"]=the_first_period["Date"].dt.strftime("%m")
the_first_period 


# In[121]:


the_first_period_copy=the_first_period.copy()
the_first_period['Date'].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
the_first_period_copy


# In[ ]:





# In[122]:


the_second_period= df[(df.Date>="2015/01/02")&(df.Date<='2019/12/2')]
the_second_period["Date"]=pd.to_datetime(the_second_period.Date, format='%Y-%m-%d')
the_second_period["Date"]=the_second_period["Date"].dt.strftime("%m")
the_second_period 


# In[123]:


the_second_period_copy=the_second_period.copy()
the_second_period['Date'].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
the_second_period_copy


# In[124]:


the_third_period= df[(df.Date>="2019/12/2")&(df.Date<='2023/01/31')]
the_third_period["Date"]=pd.to_datetime(the_third_period.Date, format='%Y-%m-%d')
the_third_period["Date"]=the_third_period["Date"].dt.strftime("%m")
the_third_period 


# In[125]:


the_third_period_copy=the_third_period.copy()
the_third_period['Date'].replace({'01':"january",'02':'february',"03":"march","04":"april","05":"may","06":'june',"07":"july","08":"august",'09':"september","10":"october","11":"november","12":"december"},inplace=True)
the_third_period_copy


# # the cell below represent the closed value in each period 
# # the third period was having the highst values

# In[126]:


plt.scatter(the_first_period_copy.Date,the_first_period_copy.Close,label='the_first_period',color="#B23AEE")
plt.scatter(the_second_period_copy.Date,the_second_period_copy.Close,alpha=0.1,label='the_second_period',color="#FFD700")
plt.scatter(the_third_period_copy.Date,the_third_period_copy.Close,alpha=0.3,label='the_third_period',color="#EE2C2C")
plt.xticks(rotation=45)
plt.title("Closed")
plt.legend()


# # the volume in each period
# # the first period was having the highst values than the third 

# In[127]:


plt.scatter(the_first_period_copy.Date,the_first_period_copy.Volume,label='the_first_period',color="#6E8B3D")
plt.scatter(the_second_period_copy.Date,the_second_period_copy.Volume,alpha=0.1,label='the_second_period',color="#000000")
plt.scatter(the_third_period_copy.Date,the_third_period_copy.Volume,alpha=0.5,label='the_third_period',color='#FAEBD7')
plt.xticks(rotation=45)
plt.title("Volume")
plt.legend()


# In[128]:


plt.scatter(the_first_period_copy.Date,the_first_period_copy.difference,label='the_first_period',color="#6E8B3D")
plt.scatter(the_second_period_copy.Date,the_second_period_copy.difference,alpha=0.1,label='the_second_period',color="#000000")
plt.scatter(the_third_period_copy.Date,the_third_period_copy.difference,alpha=0.2,label='the_third_period',color='#FAEBD7')
plt.xticks(rotation=45)
plt.title("difference")
plt.legend()


# # the third period having the best closed values than its opened

# In[129]:


plt.scatter(the_first_period_copy.Date,the_first_period_copy.difference2,label='the_first_period',color="#6E8B3D")
plt.scatter(the_second_period_copy.Date,the_second_period_copy.difference2,alpha=0.1,label='the_second_period',color="#000000")
plt.scatter(the_third_period_copy.Date,the_third_period_copy.difference2,alpha=0.3,label='the_third_period',color='#FAEBD7')
plt.xticks(rotation=45)
plt.title("defference2")
plt.legend()


# In[130]:


plt.scatter(the_first_period_copy.Date,the_first_period_copy.difference3,label='the_first_period',color="#6E8B3D")
plt.scatter(the_second_period_copy.Date,the_second_period_copy.difference3,alpha=0.1,label='the_second_period',color="#000000")
plt.scatter(the_third_period_copy.Date,the_third_period_copy.difference3,alpha=0.3,label='the_third_period',color='#FAEBD7')
plt.xticks(rotation=45)
plt.title("defference3")
plt.legend()


# # the third period have the most low closed values

# # the figure below represent the high values in the first period 

# In[131]:


the_first_period_a= df[(df.Date>="2013/01/02")&(df.Date<='2014/12/31')]
the_first_period_a
plt.plot(the_first_period_a.Date,the_first_period_a.High,label='the_first_period',color="#6E8B3D",linewidth=1.5)
plt.scatter(the_first_period_a.Date,the_first_period_a.High,label='the_first_period',color="#000000",alpha=0.2)
plt.xticks(rotation=20)
plt.show()


# # the figure below represent the low values in the first period

# In[132]:


the_first_period_a= df[(df.Date>="2013/01/02")&(df.Date<='2014/12/31')]
the_first_period_a
plt.plot(the_first_period_a.Date,the_first_period_a.Low,label='the_first_period',color="#6E8B3D",linewidth=1.5)
plt.scatter(the_first_period_a.Date,the_first_period_a.Low,label='the_first_period',color="#000000",alpha=0.2)
plt.xticks(rotation=20)
plt.show()


# # the figure below represent the close values in the first period

# In[133]:


the_first_period_a= df[(df.Date>="2013/01/02")&(df.Date<='2014/12/31')]
the_first_period_a
plt.plot(the_first_period_a.Date,the_first_period_a.Close,label='the_first_period',color="#FFD700",linewidth=0.5)
plt.scatter(the_first_period_a.Date,the_first_period_a.Close,label='the_first_period',color="#EE2C2C",alpha=0.2)
plt.xticks(rotation=20)
plt.show()


# # the figure below represent the volume in the first period

# In[134]:


the_first_period_a= df[(df.Date>="2013/01/02")&(df.Date<='2014/12/31')]
the_first_period_a
plt.plot(the_first_period_a.Date,the_first_period_a.Volume,label='the_first_period',color="#9400D3",linewidth=0.5)
plt.scatter(the_first_period_a.Date,the_first_period_a.Volume,label='the_first_period',color="#E3CF57",alpha=0.2)
plt.xticks(rotation=20)
plt.show()


# # the figure below represent the high values in the second period

# In[135]:


the_second_period_a= df[(df.Date>="2015/01/02")&(df.Date<='2019/12/2')]
the_second_period_a
plt.plot(the_second_period_a.Date,the_second_period_a.High,label='the_second_period',color="#6E8B3D",linewidth=1.5)
plt.scatter(the_second_period_a.Date,the_second_period_a.High,label='the_second_period',color="#000000",alpha=0.2)
plt.xticks(rotation=20)
plt.show()


# # the figure below represent the low values in the second period

# In[136]:


the_second_period_a= df[(df.Date>="2015/01/02")&(df.Date<='2019/12/2')]
the_second_period_a
plt.plot(the_second_period_a.Date,the_second_period_a.Low,label='the_second_period',color="#6E8B3D",linewidth=1.5)
plt.scatter(the_second_period_a.Date,the_second_period_a.Low,label='the_second_period',color="#000000",alpha=0.2)
plt.xticks(rotation=20)
plt.show()


# # the figure below represent the closevalues in the second period

# In[137]:


the_second_period_a= df[(df.Date>="2015/01/02")&(df.Date<='2019/12/2')]
the_second_period_a
plt.plot(the_second_period_a.Date,the_second_period_a.Close,label='the_second_period',color="#FFD700",linewidth=0.5)
plt.scatter(the_second_period_a.Date,the_second_period_a.Close,label='the_second_period',color="#EE2C2C",alpha=0.2)
plt.xticks(rotation=20)
plt.show()


# # the figure below represent the volume in the second period

# In[138]:


the_second_period_a= df[(df.Date>="2015/01/02")&(df.Date<='2019/12/2')]
the_second_period_a
plt.plot(the_second_period_a.Date,the_second_period_a.Volume,label='the_second_period',color="#9400D3",linewidth=0.5)
plt.scatter(the_second_period_a.Date,the_second_period_a.Volume,label='the_second_period',color="#E3CF57",alpha=0.2)
plt.xticks(rotation=20)
plt.show()


# # the figure below represent the high values in the third period

# In[139]:


the_third_period_a= df[(df.Date>="2013/12/02")&(df.Date<='2023/1/32')]
the_third_period_a
plt.plot(the_third_period_a.Date,the_third_period_a.High,label='the_third_period',color="#6E8B3D",linewidth=1.5)
plt.scatter(the_third_period_a.Date,the_third_period_a.High,label='the_third_period',color="#000000",alpha=0.2)
plt.xticks(rotation=20)
plt.show()


# # # the figure below represent the low values in the third period

# In[140]:


the_third_period_a= df[(df.Date>="2013/12/02")&(df.Date<='2023/1/32')]
the_third_period_a
plt.plot(the_third_period_a.Date,the_third_period_a.Low,label='the_third_period',color="#6E8B3D",linewidth=1.5)
plt.scatter(the_third_period_a.Date,the_third_period_a.Low,label='the_third_period',color="#000000",alpha=0.2)
plt.xticks(rotation=20)
plt.show()


# #  the figure below represent the close values in the third period

# In[141]:


the_third_period_a= df[(df.Date>="2013/12/02")&(df.Date<='2023/1/32')]
the_third_period_a
plt.plot(the_third_period_a.Date,the_third_period_a.Close,label='the_third_period',color="#FFD700",linewidth=0.5)
plt.scatter(the_third_period_a.Date,the_third_period_a.Close,label='the_third_period',color="#EE2C2C",alpha=0.2)
plt.xticks(rotation=20)
plt.show()


# # the figure below represent the volume in the third period

# In[142]:


the_third_period_a= df[(df.Date>="2013/12/02")&(df.Date<='2023/1/32')]
the_third_period_a
plt.plot(the_third_period_a.Date,the_third_period_a.Volume,label='the_third_period',color="#9400D3",linewidth=0.5)
plt.scatter(the_third_period_a.Date,the_third_period_a.Volume,label='the_third_period',color="#E3CF57",alpha=0.2)
plt.xticks(rotation=20)
plt.show()


# # AS we saw the second period was the best ascending plots 

# # the relation between closed and volume in each period 

# In[143]:


plt.scatter(the_first_period_a.Close,the_first_period_a.Volume,alpha=0.1)
plt.show()


# In[144]:


plt.scatter(the_second_period_a.Close,the_second_period_a.Volume,alpha=0.1)
plt.show()


# In[145]:


plt.scatter(the_third_period_a.Close,the_third_period_a.Volume,alpha=0.1)
plt.show()


# In[ ]:





# In[146]:


the_first_period["Open"].mean()


# In[147]:


the_second_period["Open"].mean()


# In[148]:


the_third_period["Open"].mean() 


# # the curve of the best open values in each period

# In[149]:


plt.plot(["1st period",'2nd period','3rd period'],[25.280300431781345,46.23133212332722,103.63797184630332])
plt.ylabel("Open")
plt.show()


# In[150]:


the_first_period["Close"].mean()


# In[151]:


the_second_period["Close"].mean()


# In[152]:


the_third_period["Close"].mean()


# # the curve of the best close values in each period

# In[153]:


plt.plot(["1st period",'2nd period','3rd period'],[25.267157528135513,46.23608793019295,103.65677592513198])
plt.ylabel("Close")
plt.show()


# In[154]:


the_first_period["Volume"].mean()


# In[155]:


the_second_period["Volume"].mean()


# In[156]:


the_third_period["Volume"].mean()


# # the curve of the best volume in each period

# In[157]:


plt.plot(["1st period",'2nd period','3rd period'],[68370352.66666667,37333788.96882494,34967649.0396927])
plt.ylabel("Volume")
plt.show()


# In[158]:


the_first_period["difference"].mean()


# In[159]:


the_second_period["difference"].mean()


# In[160]:


the_third_period["difference"].mean()


# # the best differences in each period 

# In[161]:


plt.plot(["1st period",'2nd period','3rd period'],[-0.01314290364583346,0.004755806865738205,0.018804078828662536])
plt.ylabel("difference")
plt.show()


# In[162]:


the_first_period["difference2"].mean()


# In[163]:


the_second_period["difference2"].mean()


# In[164]:


the_third_period["difference2"].mean()


# In[165]:


plt.plot(["1st period",'2nd period','3rd period'],[-0.1917638400244334,-0.38717469170415625,-1.1978874646136761])
plt.ylabel("difference2")
plt.show()


# In[166]:


the_first_period["difference3"].mean()


# In[167]:


the_second_period["difference3"].mean()


# In[168]:


the_third_period["difference3"].mean()


# In[169]:


plt.plot(["1st period",'2nd period','3rd period'],[0.20077910498967252,0.4159028932249708,1.2378117052144189])
plt.ylabel("difference3")
plt.show()


# 
