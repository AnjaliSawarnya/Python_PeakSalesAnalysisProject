#!/usr/bin/env python
# coding: utf-8

# ## 1. Data check and data cleaning

# In[1]:


# !pip install numpy (once to install these)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
df = pd.read_csv('Diwali Sales Data.csv', encoding='ISO-8859-1')
# df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
#df = pd.read_csv('Diwali Sales Data.csv')
df.shape
# (rows,columns)


# ## Data Wrangling & Data Cleaning

# In[2]:


df.head()
df.head(10)


# In[3]:


df.info()


# In[4]:


# To drop unrelated/blank columns

df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[5]:


pd.isnull(df)
#gives true false on null, if not null will give false everywhere
#pd.isnull(df).sum()
#gives data on columns and count of null values


# In[7]:


pd.isnull(df).sum()


# In[8]:


# Checking if we dropped null values

df.dropna(inplace=True)
#df.shape : to check the size again, previous- (11251, 15)
pd.isnull(df).sum()
# inplace is to assign the updated data, if null is removed, and not assigned, it will appear, if used inplace, it would not appear 


# In[9]:


# change the data types
df['Amount'] = df['Amount'].astype('int')


# In[10]:


df['Amount'].dtypes


# In[11]:


df.columns


# In[12]:


# To get statistical description of data.
stats = df[['Age', 'Orders', 'Amount']].describe()
stats


# ## Exploratory Data Analytics

# - Gender

# In[12]:


sales_gen = df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by ='Amount', ascending=False)
sales_gen


# In[13]:


# We will check the Amount spend/ Shopping done by customer, order by Gender and conclude the outcome through Charts

ax = sns.countplot(x = 'Gender' , data = df)
#the below function id for value labels i.e 7842
for bars in ax.containers:
    ax.bar_label(bars)


# In[14]:


sales_gen = df.groupby(['Gender'], as_index = False)['Amount'].sum().sort_values(by ='Amount', ascending=False)
sns.barplot(x = 'Gender',y= 'Amount',data = sales_gen)

From above graph is it evident that the number of female buyer is more than that of male buyers, depicting the purchasing power of females greater than males
# - Age

# In[15]:


# Total Amount Vs Age Group

sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# In[16]:


ax = sns.countplot(data = df, x= 'Age Group', hue = 'Gender')
#hue facilitates seperate bars of male and female along with count on x axis
for bars in ax.containers:
    ax.bar_label(bars)


# As per the above graph, majority of the buyers are from the age group 26-35 years Females

# - State

# In[17]:


# Total number of orders from top 10 states
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[18]:


# Total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Amount')


# - Marital Status

# From below graphs we can see that most of the buyers are married (Women) and they have high purchasing power
# 

# In[19]:


ax = sns.countplot(data = df, x= 'Marital_Status')

sns.set(rc={'figure.figsize':(3,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[20]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')
# if run without hue, it will be a candlestick diagram


# - Occupation

# In[21]:


# Frequency of purchase as per occupation sector
sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x= 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[22]:


# Purchasing power grouped by sectors in occupation
sales_state = df.groupby(['Occupation', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# From above representation, a majority of buyers are working in IT, Healthcare and Aviation sector.

# - Product Category

# In[23]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x= 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[26]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# From the above two charts we can derive that the majorty of orders were made in Clothing & Apparel, then Food and then electronics and Gadget.
# 
# It can be seen that in terms of amount spent, top 3 categories are same as the order frequency, but in different chronology i.e, Food, then clothing & Apparel then electronics and Gadget.

# In[28]:


#sales_state = df.groupby(['Product_ID'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
#sns.set(rc={'figure.figsize':(20,5)})
#sns.barplot(data = sales_state, x = 'Product_ID',y= 'Amount')

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # Conclusion

# _______
# Married women in age group 26-35 from UP, Maharashtra and Karnataka, working in IT, Healthcare and aviation are more likely to buy products from Food, Clothing and Electronics category
# _______
Thank you!