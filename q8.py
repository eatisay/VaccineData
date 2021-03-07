#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# In[8]:


df.apply(lambda x: re.search(r"//(.*?)</url>",x["Stats_Access_Link"])[1], axis=0)

