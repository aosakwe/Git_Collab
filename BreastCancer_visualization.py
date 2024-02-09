#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import os
import matplotlib.pyplot as plt


# In[7]:


os.chdir('/Users/jennacleyle/Desktop/Git_Collab/')


# In[10]:


df = pd.read_csv('BreastCancerData.csv')


# In[11]:


df.head()


# In[14]:


df['diagnosis']


# ## Plotting diagnosis histogram

# In[24]:


plt.hist(df['diagnosis'])


# ## Overall radius mean

# In[34]:


plt.hist(df['radius_mean'])
plt.show()


# ## Diagnosis == B radius mean

# In[38]:


plt.hist(df[df['diagnosis']=='B']['radius_mean'])


# ## Diagnosis == M radius mean

# In[39]:


plt.hist(df[df['diagnosis']=='M']['radius_mean'])

