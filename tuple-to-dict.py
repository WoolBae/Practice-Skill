
# coding: utf-8

# ** Make dict with two tuple**

# In[1]:


from collections import OrderedDict


# In[2]:


keys = ('oen','two','three')
values = (24,232,12)


# In[3]:


myzip = zip(keys,values)


# In[5]:


mydict = OrderedDict(myzip)


# In[6]:


mydict

