import re

'''
 break down ingredients
 # repo: https://github.com/tlitre/RecipeParser.git
'''

ingredients = ["1/8 teaspoon hot pepper sauce", "4 bone-in chicken breast halves, with skin",
"12 pounds spaghetti", "1 clove crushed garlic", "1/2 teaspoon salt", "2 1/2 cups white sugar",
"2 tablespoons butter", "2 1/3 teaspoons milk", "4 3/5 ounces goat's milk"]

measurements = [r'([a-z]+)spoons?', r'cloves?', r'cups?', r'pounds?', r'ounces?']

fraction_match = r"(\d+[\/\d. ]*|\d)" # /g means global match

def frac_to_float(frac_str):
    try:
        return float(frac_str)
    except ValueError:
        num, denom = frac_str.split('/')
        try:
            leading, num = num.split(' ')
            whole = float(leading)
        except ValueError:
            whole = 0
        frac = float(num) / float(denom)
        return whole - frac if whole < 0 else whole + frac


def find_ingredient_quantity(ing):
    ingredient_split_list = ing.split()
    amount = 0
    for num in ingredient_split_list:
        frac_match = re.search(fraction_match, num)
        if frac_match:
            amount += frac_to_float(frac_match.group(0))
    return amount


def find_ingredient_measurement(ing):
    ingredient_split_list = ing.split()
    measurement = ""
    no_nums_ingredient = [w for w in ingredient_split_list if not re.search(fraction_match, w)]
    i = no_nums_ingredient[0]
    measurement = i if re.search(r"(?=("+'|'.join(measurements)+r"))", i) else ""
    return measurement


def find_ingredient_preparation(ing):
    ingredient_split_list = ing.split(',')
    prep = ""
    if len(ingredient_split_list) > 1:
        prep = ingredient_split_list[1]
    return prep.strip()

def find_ingredient_name(ing):
    # remove meas, qty, and prep
    ingredient_split_list = ing.split()
    no_nums_ingredient = [w for w in ingredient_split_list if not re.search(fraction_match, w)]
    if find_ingredient_measurement(ing) in no_nums_ingredient:
        no_nums_ingredient.remove(find_ingredient_measurement(ing))
    name = ' '.join(no_nums_ingredient)
    # remove descriptor
    prep = find_ingredient_preparation(ing)
    if prep is not "":
        name = name.replace(prep, "")
    return name


# def find_ingredient_descriptor(ingredient_split_list):
#     # usually the next thing after measurement
#     # if find_ingredient_measurement(ingredient_split_list) is not "":
#         # the descriptor is the next thing if the len of list w/o measurement is > 1
#         return descriptor

for i in ingredients:
    print i
    print "NAME:", find_ingredient_name(i)
    print "QTY:", find_ingredient_quantity(i)
    print "MSRMNT:",  find_ingredient_measurement(i)
    print "PREP:", find_ingredient_preparation(i),'\n'

#
# class Ingredient:
#     def __init__(self, details):
#         self.name =
#         self.quantity = find_ingredient_quantity()
#         self.measurement
#         self.descriptor =
#         self.preparation =
