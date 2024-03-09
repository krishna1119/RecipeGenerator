from pymongo import MongoClient
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
mongo_user = os.getenv("MONGO_USERNAME")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_cluster = os.getenv("MONGO_CLUSTER")
OPENAI_API_KEY = os.getenv("OPEN_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

def ReturnForPrompt(username):
    collection = DatabaseConnection()
    # from pymongo import MongoClient
        # Specify the user for whom you want to retrieve data
    user_to_find = {"name": username}  # Replace with the actual username

    # Retrieve the document with only the "age" field from MongoDB
    keys_to_retrieve = {"Utensils": 1, "_id": 0, "allergies":1}  # Projection: 1 includes, 0 excludes

    # Find the user and retrieve specific keys
    user_data = collection.find_one(user_to_find, keys_to_retrieve)
    utensils=user_data['Utensils']
    allergies=user_data['allergies']

    # Print or process the retrieved data
    return utensils,allergies

def DatabaseConnection():
 
    atlas_connection_string = "mongodb+srv://" + mongo_user + ":" + mongo_password + "@" + mongo_cluster

    client = MongoClient(atlas_connection_string)

    db = client["test"]
    collection = db["user"]
    return collection

def AddUser(name, age, utensils, allergies):
    collection = DatabaseConnection()
    data = {
        "name" : name,
        "age" : age,
        "Utensils" : utensils,
        "allergies" : allergies
    }
    result = collection.insert_one(data)


def UserAuthetication(username):

    collection = DatabaseConnection()
    user = collection.find_one({"name": username})
    if user:
        flag=0
    else:
        flag=1
    return flag


def RecipeGenerator(username, ingredients, preferences,cooking_time):
    allergies, utensils = ReturnForPrompt(username)
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
    return message


print(RecipeGenerator("Aleena", "eggs, tomato, bread", "indian cuisine", "30"))
