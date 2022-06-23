#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def FSA_fat(a):
    x=float(a)
    if(x<=3):
        return("Green")
    elif(x>3 and x<=17.5):
        return("Amber")
    elif(x>17.5):
        return("Red")
    
def FSA_saturated_fat(a):
    x=float(a)
    if(x<=1.5):
        return("Green")
    elif(x>1.5 and x<=5):
        return("Amber")
    elif(x>5):
        return("Red")
    
def FSA_sugar(a):
    x=float(a)
    if(x<=5):
        return("Green")
    elif(x>5 and x<=22.5):
        return("Amber")
    elif(x>22.5):
        return("Red")
    
def FSA_sodium(a):
    if float(a)==0:
        x=float(a)
    else:
        x=float(a)/1000
        
    if(x<=0.3):
        return("Green")
    elif(x>0.3 and x<=1.5):
        return("Amber")
    elif(x>1.5):
        return("Red")
        

