#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

p1 = r'^([456]\d{3})(\-?)(\d{4})(\2)(\d{4})(\2)(\d{4})$'
p2 = r'^(?:([0-9])(?!\1{3,})){16}$'

for _ in range(int(input())):
    s = input()
    if re.match(p1, s):
        s = s.replace('-', '')
        if re.match(p2, s):
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')

