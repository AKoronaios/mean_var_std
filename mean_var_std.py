#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def calculate(arr):
    if len(arr) !=9:
        raise ValueError("List must contain nine numbers.")
    m = np.array(arr).reshape([3,3])
    r = {
        "mean": [m.mean(0).tolist(), m.mean(1).tolist(), m.mean()],
        "variance": [m.var(0).tolist(), m.var(1).tolist(), m.var()],
        "standard deviation": [m.std(0).tolist(), m.std(1).tolist(), m.std()],
        "max": [m.max(0).tolist(), m.max(1).tolist(), m.max()],
        "min": [m.min(0).tolist(), m.min(1).tolist(), m.min()],
        "sum": [m.sum(0).tolist(), m.sum(1).tolist(), m.sum()],
    }
    return r


# In[3]:


calculate([0,1,2,3,4,5,6,7,8])

