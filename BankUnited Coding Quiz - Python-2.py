#!/usr/bin/env python
# coding: utf-8

# In[31]:


import pandas as pd


# In[33]:


# have file names on hand
# loan_risk.csv
# loan_positions.csv


# In[37]:


pwd


# In[ ]:





# In[38]:


# read both csv files and create shortcut


# In[39]:


data1 = pd.read_csv('/users/nickdevv/desktop/loan risk.csv')
data2 = pd.read_csv('/users/nickdevv/desktop/loan positions.csv')


# In[ ]:





# In[40]:


# merge csv files together matching loan number column


# In[41]:


output3 = pd.merge(data1, data2,
                  on='LoanNumber',
                  how='outer')


# In[ ]:





# In[42]:


# 1. display merged csv file


# In[43]:


print(output3)


# In[ ]:





# In[44]:


# 2. replace missing data with average, or mean, in data set as requested
# I used this method because the mean is considered to be the average of a given data set.


# In[45]:


output3.fillna(output3.mean())


# In[ ]:





# In[46]:


# creating shortcut for completed data


# In[47]:


output4 = output3.fillna(output3.mean())


# In[48]:


print(output4)


# In[ ]:





# In[49]:


import numpy as np


# In[50]:


# 3. creating random uniform variables between 0-1 under column named RV


# In[51]:


output4['RV'] = np.random.uniform(0,1, len(output4))


# In[19]:


print(output4)


# In[ ]:





# In[20]:


# 3.5. add new "Flag" variable column and condition. If RV < PD = 1
# this flagged loan may represent a more trustworthy borrower since their values are lower than the given, or estimated, probability of default (PD).
# the lower the PD, the more trustworthy the borrower which may make the borrower eligible for a lower interest rate.


# In[21]:


output4['Flag'] = np.where(
    output4['PD'] == output4['RV'], 0, np.where(
    output4['PD'] >  output4['RV'], 1, 0)) 


# In[22]:


print(output4)


# In[ ]:





# In[23]:


# 4. mulitplying Flag with LGD
# this multiplied variable highlights the Loss Given Default (LGD) of the flagged loan, or the value the bank is at risk of losing if the borrower defaults on his loan. 


# In[24]:


output4['LGDxFlag'] = output4.LGD * output4.Flag


# In[25]:


print(output4)


# In[ ]:





# In[26]:


# 5. adding the new variable in the last step across all loans, storing it under dataset1. 
# adding all the highlted LGD values would give you an estimate of the total the bank is at risk of losing across all 11 loans.


# In[27]:


dataset1 = output4['LGDxFlag'].sum()
print(dataset1)


# In[ ]:





# In[28]:


# 6. for loop that runs steps 3-5 10,000 times


# In[ ]:


for i in range(10000):
    output4['RV'] = np.random.uniform(0,1, len(output4))
    output4['Flag'] = np.where(
        output4['PD'] == output4['RV'], 0, np.where(
        output4['PD'] >  output4['RV'], 1, 0)) 
    output4['LGDxFlag'] = output4.LGD * output4.Flag
    total = output4['LGDxFlag'].sum()
    print(output4)


# In[ ]:




