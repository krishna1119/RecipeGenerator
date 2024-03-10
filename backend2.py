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

def RetrieveAllInfo(username):
    collection = DatabaseConnection()
    
    query = {"name": username}
    result = collection.find_one(query)

# Check if the document for the user exists
    if result:
        # Extract values from the retrieved document
        # name = result.get("name", "")
        # password = result.get("password", "")
        age = result.get("age", "")
        utensils = result.get("Utensils", "")
        allergies = result.get("allergies", "")

        return [ age, utensils,allergies]

def DatabaseConnection():
 
    atlas_connection_string = "mongodb+srv://" + mongo_user + ":" + mongo_password + "@" + mongo_cluster

    client = MongoClient(atlas_connection_string)

    db = client["test"]
    collection = db["user"]
    return collection
    

def AddUser(name, password, age, utensils, allergies):
    collection = DatabaseConnection()
    data = {
        name: {
            "password" : password,
            "age": age,
            "name":name,
            "allergies" : allergies,
            "utensils" : utensils
        }
    }
    result = collection.insert_one(data)
    return name


def UserAuthetication(username):

    collection = DatabaseConnection()
    query = {username: {'$exists': True}}
    result = collection.find_one(query)

   # Check if the document for the user exists
    if result:
        # Extract the nested dictionary for the username
        user_data = result.get(username, {})
    
        # Retrieve the value of the 'password' key from the nested dictionary
        password = user_data.get('password', '')
    
    return username,password


def RecipeGenerator(username, ingredients, preferences,cooking_time):
    utensils, allergies = ReturnForPrompt(username)
    # utensils ="pans,pots"
    # allergies ="seafood, peanuts"
    # ingredients = "eggs, cabbage, tomato, cheeese, spices"
    # preferences = "Indian Cuisine"
    # cooking_time = "20 mins"
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
