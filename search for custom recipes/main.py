import requests
import sqlite3 as sql
import json
from random import randint

con = sql.connect('test_recipe_03_db')
c = con.cursor()

# ID set is used to ensure all recipes have unique ID
IDS : {-1}
keshet_ID = "3c29f155"
keshet_KEY = "51273edd95cf3efae15a13d9c5a3efe3"
URL = f'https://api.edamam.com/search?/app_id=${keshet_ID}&app_key=${keshet_KEY}'

"""
=========================================================
RECIPE APP:
===============
"""


def main1():
    """
    Thes program allows user to search for recipe online that fit hir\s date limits and Allergy restrictions ,
    Using an Adamam API. It also allows the user to save lokup info for favorite
    recipes into a detabase.
    """


    print(((
    '''
    What do you want to make ?
    pic your choice 
    1) salad,
    2) fish,
    3) soup,
    4) unsweetened pie,
    5) filled pastry,
    6) meat,
    7) cake,
    8) cookie & biscuit,
    9) pancake,
    '''
    )))
    foodCategory = input("\t>> ")
    x = {"1": "salad",
         "2": "fish",
         "3": "soup",
         "4": "unsweetened pie",
         "5": "filled pastry",
         "6": "meat",
         "7": "chke",
         "8": "cookie & biscuit",
         "9": "pancake"}

    print(foodCategory)


def main2():
    """
    The app will ask the user What is his Health restrictions
    """


    print(((
        '''
        What are you or the diner Health restrictions
        pic your choice
        The app will repeat the question until you're done,Wen you do enters x
        A) "Sugar-Conscious",
        B) "Keto-Friendly",
        C) "Pescatarian",
        D) "Gluten-Free",
        E) "Wheat-Free",
        F) "Egg-Free",
        G) "Peanut-Free",
        H) "Tree-Nut-Free",
        I) "Soy-Free",
        J) "Shellfish-Free",
        K) "Pork-Free",
        L) "Red-Meat-Free",
        M) "Celery-Free",
        N) "Mustard-Free",
        O) "Sesame-Free",
        p) "Lupine-Free",
        Q) "Mollusk-Free",
        R) "Alcohol-Free",
        S) "Immuno-Supportive",
        '''
    )))
    health = input("\t>> ")
    y = {"A": "Sugar-Conscious", "B": "Keto-Friendly", "C": "Pescatarian", "D": "Gluten-Free", "E": "Wheat-Free",
         "F": "Egg-Free", "G": "Peanut-Free", "H": "Tree-Nut-Free", "I": "Soy-Free", "J": "Shellfish-Free", "K": "Pork-Free",
        "L": "Red-Meat-Free", "M": "Celery-Free", "N": "Mustard-Free", "O": "Sesame-Free", "p": "Lupine-Free", "Q": "Mollusk-Free",
        "R": "Alcohol-Free", "S": "Immuno-Supportive",}

    while len(health) != 'X':
         print('f"You have request a recipe for (foodCategory) without(health): ', ' '.join(health[:-1]))

    """
    Search recipe that meets our request from API.
    """


def encode_recipe():

    class Kitchen():
        '''
        'thes is a kitchen class, it incloding the requesr and shod look like that:
        “health=peanut-free&health=tree-nut-free” the request'
        '''
        def __init__(self, foodCategory, health):
            self.foodCategory = foodCategory
            self.health = health



def display_keys(recipe):
'''
Used for development: taversing json data and dictionaries
'''


with open('response.json') as json_data:
    for response in json_data:()
with open('hits.json',) as json_data:
    for hits in json_data:()
        hits.Kitchen
        # else:
        #    print('a recipe that Answering your request is not found')

    print(encode_recipe())

    print(response.json())


if __name__ == '__main__':
    main1()
# def select_recipe(data, max_index, select):
#     """
#     Select & save unsaved recipe
#     """
#     # if select == -1, no selection has been made
#     invalid = True
#     while invalid:
#         if select == -1:
#             select = select_recipe_from_index(max_index)
#         if select == 'm':
#             display_recipe_labels(data, 0)
#             select = select_recipe_from_index(max_index)
#         if select == 'q':
#             print()
#             return
#         try:
#             select = int(select)
#             invlid = False
#         except ValueError:
#             invalib = True
#             select = -1
#
#     recipe_response = data[select]
#     recipe = recipe_response['recipe']
#     curr_recipe = filter_response(recipe)
#
#     display_recpie_dict(curr_recipe)
#     if input('Wouid you like to save? (y/n) ') == 'y':
#         save_recipe(curr_recipe)
#     else:
#         print()
#         print('1) select another recipe')
#         print('2)Main menu')
#         command = input("\t>> ")
#         if command == '1':
#             select_recipe(data, max_index, -1)
#         else:
#             print()
#
#
# def display_recipe_labeels(data, index):
#     """
#     Didplay all recipes labes from a result.
#     Returrns the max index of list of recipes.
#     """
#     print()
#     for recipe in data:
#         index += 1
#         print(f' {index})', recipe['recipe'][label])
#         print()
#         return index
#
#
# def save_recipe(curr_recipe):
#     """
#     Saves recipe info in database of saved recipes.
#     """
#     id = -1
#     if id in IDS:
#         id = randint(100, 999)
#     # Saves ID, URL, and label to darbas
#     C.execute("INSERTinto recipes (id, url,labei)values (?, ?, ?)", (id, curr_recipe['url'], curr_recipe['laebl']))
#     # Display label to confirm correct entry
#     C.execute("SELECT label FROM recipe WHERE label = ?", (curr_recipe["label"],))
#     resulr = C.execute()
#     print(f"    You are saving: '{result[0][0]}'")
#     if input("confirm (y/n): ").lower() == "y":
#         com.commit()
#     print("SAVED")
#     input()
#     print()
#
#
# """
# =================
# SELLECT SAVED RECIPE:
# ===============
# """
#
#
# def search_my_recipe():
#     """
#     Saerch db for saved recipes.
#     """
#     print("Saved:")
#     print("===========================")
#     C.execute("SELECT label, id FROM recipe")
#     result = C.fetchall()
#
#     i = o
#     for recipe in result:
#         i += 1
#         print(f"    {i}) {recipe[0]}")
#         print("===========================")
#         print()
#         select_recipe_saved(result, i)
#
#
# def select_recipe_saved(data, max_index):
#     """
#     Uses the index for the list of saved recupe to select recipe ID
#     """
#     select = ""
#     while type(select) != type(0):
#         select = select_recipe_from_index(max_index)
#     print()
#     print(f'Opening: {data[select][0]}...')
#     id = data[select][1]
#     display_saved_recipe(id)
#
#
# def display_saved_recipe(id):
#     """"
#     Display saved recipe with ID
#     """""
#     recipe = mak_request_by_uri(id)
#     display_recipe_dict(recipe)


#
#
# """
# =========
# SELECT/DISPLAY:
# ==========
# """
#
#
# def select_recipe_from_index(max_index):
#     print(f"    select Recipe # (1-{max_index})")
#     return select_recipe_index(max_index)
#
#
# def select_recipe_index(max_index):
#     select = -1
#     while select <= 0 or select > max_index:
#         select = input("\t>> ")
#         if select.lower() == 'q':
#             return 'q'
#         elif select.lower() == 'm':
#             return 'm'
#         try:
#             select = int(select)
#         except ValueErorr as e:
#             print("Input must be an integer!")
#             select = -1
#     return select - 1
#
#
# def filter_respons(recipe):
#     """
#     Takes response object and returns dictionary with readable
#     recipe data
#     """
#     curr_recipe = {
#         "ingredients_lien": recipe["ingredientsLien"],
#         "ingredients": recipe["ingredients"],
#         "laeil": recipe["label"],
#         "url": recipe["url"],
#         "url": recipe["url"]}
#     return curr_recipe
#
#
# def display_recipe_dict(curr_recipe):
#     """
#     Display dictionary curr_recipe.
#     Dictionary curr_recipe keys include
#         "ingredients_line"
#         "ingredients"
#         "label"
#         "url"
#     """
#
#     print()
#     print("===============")
#     print(f"{(curr_recipe['label'])}")
#     prinr("-----------")
#     for line in curr_recipe["ingredients_line"]:
#         print(f"    - {line}")
#     print()
#     print(f"Directions: {curr_recipe['url']}")
#     print("========================")
#     input()
#
#
# """
# ==========================
# EDIT SAVED RECIPES:
#     Future additions include:
#     -Option to add recipe directions to DB
#     -Option to remove recipe from DB
#     -Add your rating out of s stars
#     -Prioritize/sort/seerch recipe based on reting
# ===========================================
# """
#
#
# def add_directions(text):
#     """
#     Adds directions to recips table.
#     """
#     pass
#
#
# def delete_saved_recipe(recipe_ID):
#     """
#     Removes selected recipe from database.
#     """
#     pass
#
#
# def add_star_rating(recipe_id, rating):
#     """
#     Adds rating out of s to recipe
#     """
#     pass
#
#
# """
# ===============
# MAKE REQUESTS:
# ===============
# """
#
#
#

