# Introduction
The proliferation of recipes on the Web presents an opportunity for developing AI methods to promote healthy nutrition of people using the Internet as a source of food inspiration. Recent research endeavors have resulted in the development of ontologies related to food, and algorithmic solutions for ingredient substitution. However, there is a lack of a resource oriented towards promoting research in semantic-based algorithmic meal plan recommendation and/or individual ingredient substitution that explicitly incorporates healthiness into the recommendation process. To address this gap, we present a knowledge graph comprising a large collection of recipes sourced from Allrecipes.com, their ingredients and corresponding nutritional information, social interactions metadata, and healthiness information calculated based on two international nutritional standards. This repository provides the code and data used to populate RecipeKG, a recipe-based knowledge graph.

## Citation
If you use our code, or the Ontology in this repository, please cite our paper as follows:
> Charalampos Chelmis, and Bedirhan Gergin. A Knowledge Graph for Semantic-Driven Healthiness Evaluation of Recipes, May 2022.

BibTeX:
``` 
@inproceedings{recipekg2022,
  title = {A Knowledge Graph for Semantic-Driven Healthiness Evaluation of Recipes},
  author = {Chelmis, Charalampos and Gergin, Bedirhan},
  booktitle = {},
  series = {},
  pages = {},
  year = {2021},
  isbn = {},
  url = {},
  doi = {},
  organization={}
}
```

If you use the data please cite our data as follows:

BibTeX:
``` 
@data{DVN/99PNJ5_2022,
author = {Chelmis, Charalampos and Gergin, Bedirhan},
publisher = {Harvard Dataverse},
title = {{A Knowledge Graph for Semantic-Driven Healthiness Evaluation of Online Recipes}},
year = {2022},
version = {V2},
doi = {10.7910/DVN/99PNJ5},
url = {https://doi.org/10.7910/DVN/99PNJ5}
}
```

## Quick Overview



### Prerequisites
Python 3.8 or above and the following libraries

```
- request, json, BeautifulSoup
- nltk, glob, difflib
- rdflib
```

### Files
```
   Code: Include the codes for processes of scraping allrecipes.com website recipes into rdf data.

   Data: Includes two data: 
          a) json-data: Includes the recipes json-ld metadata that are scraped from allrecipes.com.  
          b) rdf-data: Includes the rdf data that is created in intermediate process as explained in code section.
            
   Ontology: RecipeKG ontology owl file 

```
Final clean and published data can be found at [Dataverse](https://doi.org/10.7910/DVN/99PNJ5).

### How to use

Please consult the readme files in corresponding dirrectories explaining how to run the code or use the Ontology.


### Contributions 
We encourage the collaborative extention of RecipeKG Ontology. To simplify the process we monitor this repository's Issue tracker for requests of new terms/classes. We also check for reported errors or specific concerns related to the ontology.

