#!/usr/bin/env python
# coding: utf-8

# 
# ### Parvin Salamzade
# ### I am interested in data science because I am chemical engineer and data science has lots of aplications in engineering
# 
# ### My code will create  a fibonacci sequence 

# In[ ]:


nterms = int(input("How many terms? "))


# In[ ]:


if nterms <= 0:
   print("Enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

