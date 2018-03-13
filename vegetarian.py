from bs4 import BeautifulSoup
import re
from ingredients_parser import *
from scraper import *

recipeList = scrapeRecipe('https://www.allrecipes.com/recipe/8661/chicken-wings/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%202')

ingredients = recipeList[0]
print ingredients
ingNames =[]

for i in ingredients:
	ingNames.append(Ingredient(i).name_with_descriptor)

print ingNames

'''meats= ['chicken','wings', 'beef', 'ground beef', 'duck', 'pork', 'ham','prosciutto', 'fish', 'sea bass', 'tilapia', 'salmon', 'halibut', 'trout','flounder',
'turkey', 'meat stock', 'liver', 'crab', 'shrimp', 'liver', 'bacon', 'lamb']'''
meat_substitutes = {'chicken': 'eggplant', 'wings': 'eggplant', 'beef': 'tofu', 'ground beef': 'lentils', 'duck': 'tempeh', 'pork': 'seitan', 'ham': 'jackfruit',
'prosciutto': 'mushroom', 'fish': 'tofu', 'sea bass': 'cauliflower', 'tilapia': 'seitan', 'salmon': 'eggplant', 'halibut': 'tempeh', 'trout': 'tofu','flounder': 'jackfruit',
'turkey': 'seitan', 'meat stock': 'vegetable stock', 'liver': 'jackfruit', 'crab': 'cauliflower', 'shrimp': 'tofu', 'liver': 'tempeh', 'bacon': 'fried shallots', 'lamb': 'eggplant'}


for i in ingNames:
	i =[ v for k,v in meat_substitutes.items() if k in i]

print ingNames

for n, i in enumerate(ingNames):
	for j in meats:
		if i == j:
			ingNames[n] = meat_substitutes[j]

print ingNames

'''for i in ingredients:
	Ingredient(i).name = ingNames[i]

print ingredients

recipeList[0]=ingNames

for key in meat_match:
    ingNames = ingNames.replace(key, meat_substitutes[key])

print ingNames
matching = [v for k, v in meat_substitutes.items() if k in ingNames]
print matching
'''


