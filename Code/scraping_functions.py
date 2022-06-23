#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#These are small helper functions, especially can help in the test
import requests
from bs4 import BeautifulSoup
import json


# In[ ]:


#give sitemap URL, return all the recipe-url as list
def get_sitemap_url_list(sitemap_url):
    page = requests.get(sitemap_url)
    soup = BeautifulSoup(page.content, "html.parser")
    urls=soup.find_all("loc")
    #put urls into list
    url_list=[]
    for url in urls:
        url_list.append(url.text)
    return(url_list)


# In[ ]:


#give recipe url and take the ld+json as dictionary
def get_recipe_jsonld(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    result=soup.find("script", type="application/ld+json")  
    a=json.loads(result.text)
    dict=a[1]
    return(dict)


# In[ ]:


#open a local json recipe file and output as dictionary
def open_recipe_jsonfile(recipe_path):
    # Opening JSON file
    f = open(recipe_path,)

    # returns JSON object as 
    # a dictionary
    dict = json.load(f)
    f.close()
    return (dict)

