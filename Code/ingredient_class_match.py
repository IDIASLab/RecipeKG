#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#ingredient classes added manually from heals Ontology
list={ "all purpose flour":"http://purl.org/heals/ingredient/AllPurposeFlour",
      "almond":"http://purl.org/heals/ingredient/Almond",
      "almond biscotti":"http://purl.org/heals/ingredient/AlmondBiscotti",
      "almond meal":"http://purl.org/heals/ingredient/AlmondMeal",
      "apple cider vinegar":"http://purl.org/heals/ingredient/AppleCiderVinegar",
      "bacon":"http://purl.org/heals/ingredient/Bacon",
      "baked chicken tender":"http://purl.org/heals/ingredient/BakedChickenTender",
      "baker's yeast":"http://purl.org/heals/ingredient/BakersYeast",
      "baking powder":"http://purl.org/heals/ingredient/BakingPowder",
      "baking soda":"http://purl.org/heals/ingredient/BakingSoda",
      "balsamic vinegar":"http://purl.org/heals/ingredient/BalsamicVinegar",
      "banana":"http://purl.org/heals/ingredient/Banana",
      "banana blueberry almond flour muffinni":"ttp://purl.org/heals/ingredient/BananaBlueberryAlmondFlourMuffin",
      "banana bread":"http://purl.org/heals/ingredient/BananaBread",
      "basil":"http://purl.org/heals/ingredient/Basil",
      "beef":"http://purl.org/heals/ingredient/Beef",
      "beef bouillonni":"http://purl.org/heals/ingredient/BeefBouillon",
      "beef nilaga":"http://purl.org/heals/ingredient/BeefNilaga",
      "beef stewni":"http://purl.org/heals/ingredient/BeefStew",
      "bitter":"http://purl.org/heals/ingredient/Bitter",
      "black pepper":"http://purl.org/heals/ingredient/BlackPepper",
      "black peppercorn":"http://purl.org/heals/ingredient/BlackPeppercorn",
      "blueberry":"http://purl.org/heals/ingredient/Blueberry",
      "braised balsamic chicken":"http://purl.org/heals/ingredient/BraisedBalsamicChicken",
      "brown sugar":"http://purl.org/heals/ingredient/BrownSugar",
      "brownies":"http://purl.org/heals/ingredient/Brownies",
      "butter":"http://purl.org/heals/ingredient/Butter",
      "cabbage":"http://purl.org/heals/ingredient/Cabbage",
      "cane sugar":"http://purl.org/heals/ingredient/CaneSugar",
       "canola oil":"http://purl.org/heals/ingredient/CanolaOil",
       "carrot":"http://purl.org/heals/ingredient/Carrot",
       "celery":"http://purl.org/heals/ingredient/Celery",
       "celsius":"http://purl.org/heals/ingredient/Celsius",
       "chayote squash":"http://purl.org/heals/ingredient/ChayoteSquash",
      "cheese":"http://purl.org/heals/ingredient/Cheese",
      "chicken":"http://purl.org/heals/ingredient/Chicken",
      "chicken broth":"http://purl.org/heals/ingredient/ChickenBroth",
      "chicken egg":"http://purl.org/heals/ingredient/ChickenEgg",
      "chicken salad":"http://purl.org/heals/ingredient/ChickenSalad",
      "chuck roast":"http://purl.org/heals/ingredient/ChuckRoast",
      "cilantro":"http://purl.org/heals/ingredient/Cilantro",
      "clove":"http://purl.org/heals/ingredient/Clove",
      "cocoa powder":"http://purl.org/heals/ingredient/CocoaPowder",
      "coconut":"http://purl.org/heals/ingredient/Coconut",
      "coconut milk":"http://purl.org/heals/ingredient/CoconutMilk",
      "corn syrup":"http://purl.org/heals/ingredient/CornSyrup",
      "corned beef":"http://purl.org/heals/ingredient/CornedBeef",
      "corned beef hash":"http://purl.org/heals/ingredient/CornedBeefHash",
      "cornstarch":"http://purl.org/heals/ingredient/Cornstarch",
      "cow milk":"http://purl.org/heals/ingredient/CowMilk",
      "creamy":"http://purl.org/heals/ingredient/Creamy",
      "crumbly":"http://purl.org/heals/ingredient/Crumbly",
      "crunchy":"http://purl.org/heals/ingredient/Crunchy",
      "dried cranberry":"http://purl.org/heals/ingredient/DriedCranberry",
      "fahrenheit":"http://purl.org/heals/ingredient/Fahrenheit",
      "flourless coconut and almond cake":"http://purl.org/heals/ingredient/FlourlessCoconutAndAlmondCake",
      "garlic":"http://purl.org/heals/ingredient/Garlic",
      "gluten free coconut cake":"http://purl.org/heals/ingredient/GlutenFreeCoconutCake",
      "gluten free flour":"http://purl.org/heals/ingredient/GlutenFreeFlour",
      "golden kamut bread":"http://purl.org/heals/ingredient/GoldenKamutBread",
      "gooey":"http://purl.org/heals/ingredient/Gooey",
      "greasy":"http://purl.org/heals/ingredient/Greasy",
      "green onion":"http://purl.org/heals/ingredient/GreenOnion",
      "green pepper":"http://purl.org/heals/ingredient/GreenPepper",
      "grilled chicken kabob":"http://purl.org/heals/ingredient/GrilledChickenKabob",
      "honey":"http://purl.org/heals/ingredient/Honey",
      "hour":"http://purl.org/heals/ingredient/Hour",
      "kamut":"http://purl.org/heals/ingredient/Kamut",
      "kamut flour":"http://purl.org/heals/ingredient/KamutFlour",
      "kamut muffin":"http://purl.org/heals/ingredient/KamutMuffin",
      "kamut pancake":"http://purl.org/heals/ingredient/KamutPancake",
      "lamb":"http://purl.org/heals/ingredient/Lamb",
      "lemon juice":"http://purl.org/heals/ingredient/LemonJuice",
      "mayonnaise":"http://purl.org/heals/ingredient/Mayonnaise",
      "minute":"http://purl.org/heals/ingredient/Minute",
      "moist":"http://purl.org/heals/ingredient/Moist",
      "mushy":"http://purl.org/heals/ingredient/Mushy",
      "nutty":"http://purl.org/heals/ingredient/Nutty",
      "oat":"http://purl.org/heals/ingredient/Oat",
      "olive oil":"http://purl.org/heals/ingredient/OliveOil",
      "onion":"http://purl.org/heals/ingredient/Onion",
      "oregano":"http://purl.org/heals/ingredient/Oregano",
      "paprika":"http://purl.org/heals/ingredient/Paprika",
      "parsley":"http://purl.org/heals/ingredient/Parsley",
      "peanut":"http://purl.org/heals/ingredient/Peanut",
      "pecan":"http://purl.org/heals/ingredient/Pecan",
      "pot roast with vegetables":"http://purl.org/heals/ingredient/PotRoastWithVegetables",
      "potato":"http://purl.org/heals/ingredient/Potato",
      "pumpkin seed":"http://purl.org/heals/ingredient/PumpkinSeed",
      "rosemary":"http://purl.org/heals/ingredient/Rosemary",
      "salt":"http://purl.org/heals/ingredient/Salt",
      "salty":"http://purl.org/heals/ingredient/Salty",
      "saucy shepherd pie":"http://purl.org/heals/ingredient/SaucyShepherdPie",
      "sesame oil":"http://purl.org/heals/ingredient/SesameOil",
      "smoky":"http://purl.org/heals/ingredient/Smoky",
      "smothered chicken breast":"http://purl.org/heals/ingredient/SmotheredChickenBreast",
      "soy sauce":"http://purl.org/heals/ingredient/SoySauce",
      "spicy":"http://purl.org/heals/ingredient/Spicy",
      "sweet":"http://purl.org/heals/ingredient/Sweet",
      "tapioca flour":"http://purl.org/heals/ingredient/TapiocaFlour",
      "tarragon":"http://purl.org/heals/ingredient/Tarragon",
      "tart":"http://purl.org/heals/ingredient/Tart",
      "thai chicken":"http://purl.org/heals/ingredient/ThaiChicken",
      "thyme":"http://purl.org/heals/ingredient/Thyme",
      "tomato":"http://purl.org/heals/ingredient/Tomato",
      "vanilla extract":"http://purl.org/heals/ingredient/VanillaExtract",
      "vegetable oil":"http://purl.org/heals/ingredient/VegetableOil",
      "walnut":"http://purl.org/heals/ingredient/Walnut",
      "water":"http://purl.org/heals/ingredient/Water",
      "white bread":"http://purl.org/heals/ingredient/WhiteBread",
      "white sugar":"http://purl.org/heals/ingredient/WhiteSugar",
      "white vinegar":"http://purl.org/heals/ingredient/WhiteVinegar",
      "whole grain banana pancake":"http://purl.org/heals/ingredient/WholeGrainBananaPancake",
      "whole grain mustard":"http://purl.org/heals/ingredient/WholeGrainMustard",
      "whole wheat flour":"http://purl.org/heals/ingredient/WholeWheatFlour" 
}


# In[ ]:


from difflib import SequenceMatcher
import nltk
import requests
from bs4 import BeautifulSoup
import json
import urllib.parse
import glob
from scraping_functions import * 

def find_ingredient_URI(ingredient):

    highestScore=0
    highestKey=""
    p = nltk.PorterStemmer()
    #w = nltk.WordNetLemmatizer()

    #for every word in ingredient compare with every healsIngredient in the list if it exist in it
    #if the part of the ingredient exist in an healsIngredient
    #compare similarity between whole ingredient name and healsIngredient
    for a1 in list:
        a2=p.stem(a1)
        for x1 in ingredient.split():
            x2=p.stem(x1)
            if x2 in a2:
                s=SequenceMatcher(None, p.stem(ingredient), a2)
                ratio=s.ratio()

                if ratio>highestScore:
                    highestScore=ratio
                    highestKey=a1
    
    #if there is a match return ingredient name and ingredient URI
    if highestKey and highestScore>=0.7 :
        return(highestKey,list[highestKey])
    
    #if there is no match create new URI and return ingredient name and ingredient URI
    else:
        baseURI="http://purl.org/recipekg/recipe/ingredient/"
        #encoding=urllib.parse.quote(ingredient)
        ingredientURI=baseURI+ingredient.title().replace(" ", "")
        #list[ingredient]=ingredientURI
        return(ingredient,ingredientURI)

