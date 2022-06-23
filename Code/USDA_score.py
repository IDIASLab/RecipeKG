#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_USDA_score(dict):
    health_score=0
    
    if dict["nutrition"]:
        
        if dict["nutrition"]["carbohydrateContent"]:
            list=dict["nutrition"]["carbohydrateContent"].split() 
            if(float(list[0])<45):
                health_score=health_score+1
                
        if dict["nutrition"]["proteinContent"]:
            list=dict["nutrition"]["proteinContent"].split() 
            if(float(list[0])>10):
                health_score=health_score+1
                
        if dict["nutrition"]["fatContent"]:
            list=dict["nutrition"]["fatContent"].split()
            if(float(list[0])<8.888):
                health_score=health_score+1
                
        if dict["nutrition"]["saturatedFatContent"]:
            list=dict["nutrition"]["saturatedFatContent"].split()
            if(float(list[0])<4.444):
                health_score=health_score+1
                
        if dict["nutrition"]["sugarContent"]:
            list=dict["nutrition"]["sugarContent"].split() 
            if(float(list[0])<10):
                health_score=health_score+1
        
        if dict["nutrition"]["fiberContent"]:
            list=dict["nutrition"]["fiberContent"].split() 
            if((float(list[0])/1000)>5.6):
                health_score=health_score+1
        
        if dict["nutrition"]["sodiumContent"]:
            list=dict["nutrition"]["sodiumContent"].split() 
            if((float(list[0])/1000)<4.6):
                health_score=health_score+1
                
        return(health_score)

