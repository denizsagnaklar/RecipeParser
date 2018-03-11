import requests
from bs4 import BeautifulSoup

def scrapeRecipe(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    #ingredientsLeft = soup.find_all(id="lst_ingredients_1")
    #ingredientsRight = soup.find_all(id="id=lst_ingredients_2")
    ingredients = []
    ingredientSoup = soup.find_all("span", itemprop="ingredients")
    ingredients = [i.text for i in ingredientSoup]
    stepSoup = soup.find_all(class_="step")
    steps = [s.text for s in stepSoup]
    
    return([ingredients, steps])
    