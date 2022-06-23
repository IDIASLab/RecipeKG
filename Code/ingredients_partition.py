#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from recipe_parser import scrape, IngredientParser


# In[ ]:


#Some of the problems in the model observed manually and preprocesses were added
def preprocess(ingredient):
    
    ingredient=ingredient.replace("½", "1/2")
    ingredient=ingredient.replace("⅓", "1/3")
    ingredient=ingredient.replace("⅔", "2/3")
    ingredient=ingredient.replace("¼", "1/4")
    ingredient=ingredient.replace("¾", "3/4")
    ingredient=ingredient.replace("pounds", "pound")
    ingredient=ingredient.replace("cans", "can")
    ingredient=ingredient.replace("tablespoons", "tablespoon")
    ingredient=ingredient.replace("teaspoons", "teaspoon")
    ingredient=ingredient.replace("cups", "cup")

    return ingredient


# In[ ]:


#function take the ingredient and return parsed PRODUCT,QUANTITY,UNIT
def ingredient_partition(ingredient):
    ip = IngredientParser() 
    ingredient2=preprocess(ingredient)
    ingredient2=ingredient2.replace('\u2009', ' ')
    parsed=ip.parse(ingredient2)
    return parsed.ents

