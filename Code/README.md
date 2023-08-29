### Prerequisites
Python 3.8 or above and the following libraries

```
- request, json, BeautifulSoup
- nltk, glob, difflib
- rdflib
```

### Files
``` 
   1-scrape_sitemap.ipynb: for getting recipes as json files into a local file.
   2-json_to_ttl.ipynb: transformation of recipes from json to rdf data.
   3-ingredients_partition.ipynb: has functions for partitioning ingredients as quantity,unit, name. 
   4-ingredient_class_match.ipynb: create URI's for recipes. 
   5-FSA_color.ipynb: include function for determining FSA color of specific nutritions.
   6-USDA_score.ipynb: include function for determining USDA score of recipes.
   7-scraping_functions.ipynb: helper functions for various scraping methods.
```
recipe_parser: CRF model developed for identifying and partitioning ingredients from text strings. Model was trained and used in the project. For further details and training refer to [here](https://github.com/tyler-a-cox/recipe-parsing).

### How to use
This data can be directly run through the jupyter notebook files for the following purposes:

1. You can run the 1-scrape_sitemap.ipynb and get the recipes as json files into a local repository.
2. You can transform json files into rdf data according to recipeKG ontology by 2-json_to_ttl.ipynb.
    While doing that, it benefits from different functions from different files: 
    
      3. ingredients_partition.ipynb have the function which takes an ingredient and output the quantity,unit,name by the help of CRF model and some preprocessing.
     
      4. ingredient_class_match.ipynb create the URI's for recipes by comparing with another ontology.
      
      5. FSA_color.ipynb have the function to identfy the FSA color of the nutrient according to FSA standarts.
      
      6. scraping_functions.ipynb has some functions to automate the process of scraping a sitemap and json files. 
