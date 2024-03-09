from openai import OpenAI
#from d import data_retrieve
from dotenv import load_dotenv
import os


load_dotenv()
OPENAI_API_KEY = os.getenv('OPEN_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

def toList(string):
    return string.split(',')

#utensil,allergy=data_retrieve()
# def recipeGenerator(allergies, utensils, ingredients, cooking_time, preference):
def recipeGenerator(allergy, utensil, ingredients, preferences,cooking_time):
    allergies = allergy
    utensils = utensil
    ingredients = "eggs, cabbage, tomato, cheeese, spices"
    preferences = "Indian Cuisine"
    cooking_time = "20 mins"
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {"role": "system", "content": "You are a recipe generator who generates recipes based on users ingredients, their allergies, prefernces, and available utensils"},
    {"role": "user", "content": "Make me a recipe with" + ingredients + " and " + utensils + " in the style of "+ preferences +" that i can finish in " + cooking_time + " and i have these allergies: " + allergies}
    
    ]
    )
    message = completion.choices[0].message.content
    print(message)

recipeGenerator()