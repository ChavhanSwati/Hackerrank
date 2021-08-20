#!/usr/bin/env python
# coding: utf-8

# In[ ]:


p = input()
print(p.isdigit() and 100000 <= int(p) <= 999999 and 
      sum([p[i] == p[i+2] for i in range(0, 4)]) < 2)

