import streamlit as st
from streamlit_option_menu import option_menu

# Dummy user database
USER_DATABASE = {
    'user1': {'password': 'pass123', 'name': 'User One', 'age': 25, 'allergies': ['peanut', 'gluten'], 'utensils': ['knife', 'spoon']},
    'user2': {'password': 'pass456', 'name': 'User Two', 'age': 30, 'allergies': ['dairy'], 'utensils': ['fork', 'spatula']}
}


# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user' not in st.session_state:
    st.session_state.user = {}
if 'user_info' not in st.session_state:
    st.session_state.user_info = {}

# Function to navigate to the next page
def navigate_to_page(next_page):
    st.session_state.page = next_page

def streamlit_menu():
    selected = option_menu(
        menu_title=None,  # required
        options=["Home", "Profile"],  # required
        orientation="horizontal",
        styles={
    "container": {"padding": "0!important", "background-color": "#eaeaea"},
    "icon": {"color": "black", "font-size": "25px", "display": "none"},
    "nav-link": {
        "font-size": "25px",
        "text-align": "left",
        "margin": "0px",
        "font-family": "Arial, sans-serif",
        "color": "black",
        "--hover-color": "#4CAF50",
    },
    "nav-link-selected": {"background-color": "#ccc", "color": "black"},
},
        )
    return selected


def homepage():
    st.set_page_config(page_title="Recipe Generator", page_icon="🍳",layout="wide")

    col1, col2,col3= st.columns([0.4,0.45,6])
    st.markdown(
            """
            <style>
                div.stButton > button {
                    color:#4CAF50 ;
                    background-color:white;
                    border: none;
                    //padding: 10px 20px;  /* Adjust padding as needed */
                    cursor: pointer;
                }
            </style>
            """,
        unsafe_allow_html=True
    )
    with col1:
        hombutton = st.button("Home")
        if hombutton:
            navigate_to_page('homepage')
    with col2:
        signup = st.button("Signup")
        if signup:
            navigate_to_page('signup')
    with col3:
        profileebutton = st.button("Login")
        if profileebutton:
            navigate_to_page('login')
   

    # Custom CSS for styling
    st.markdown(
        """
        <style>
            .title {
                font-size: 36px;
                font-weight: bold;
                margin-bottom: 5px;
                color: #4CAF50; /* Green color */
                font-family: 'Helvetica', sans-serif;
                font-size: 60px;
                text-align: center;
                -webkit-text-stroke: 0.5px rgba(1, 50, 32, 0.5);
            }

            .subtitle {
                font-size: 24px;
                margin-bottom: 30px;
                font-family: 'Helvetica', sans-serif;
                font-weight: bold;
                font-size: 35px;
                text-align: center;
            }

            .description {
                font-size: 18px;
                margin-bottom: 20px;
                font-family: 'Helvetica', sans-serif;
                text-align: center;
                font-style: italic;
            }

            .image-container img {
                width: 100%;
                border-radius: 10px;
                margin-bottom: 20px;
            }

            .tagline {
                font-size: 24px;
                font-weight: bold;
                color: #4CAF50; /* Green color */
                font-family: 'Helvetica', sans-serif;
                text-align: center;
                margin-bottom: 20px;
            }

            .heading2 {
                margin-top: 10px;
                font-family: 'Helvetica', sans-serif;
                font-weight: bold;
                font-size: 30px;
                text-align: center;
            }

            .recipe-info {
                text-align: center;
                margin-bottom: 20px;
                border-bottom: 2px solid #4CAF50;
                padding-bottom: 10px;
            }

            .recipe-name {
                font-size: 25px;
                font-weight: bold;
                margin-bottom: 5px;
            }

            .recipe-description {
                font-size: 16px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Title and introductory text
    st.markdown("<div class='title'>🐼 Hungry Panda 🐼</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Recipe Generator</div>", unsafe_allow_html=True)
    st.markdown("<div class='description'>A quick and easy way to discover delicious recipes for every mood and occasion</div>", unsafe_allow_html=True)

    # Some Recipes Title

    # Display the image
    image_url = "https://i.pinimg.com/564x/5d/9f/69/5d9f69a552b37e9909f9d825edc56f11.jpg"
    st.markdown(f"<div class='image-container'><img src='{image_url}'></div>", unsafe_allow_html=True)

    # Tagline
    st.markdown("<div class='tagline'>Discover, Cook, Enjoy – Your Ultimate Recipe Companion.</div>", unsafe_allow_html=True)

    st.markdown("<div class='heading2'>Some Recipes</div>", unsafe_allow_html=True)


    recipes = [
        {"name": "Spaghetti Carbonara", "description": "A classic Italian pasta dish made with eggs, cheese, pancetta, and black pepper."},
        {"name": "Chicken Parmesan", "description": "Breaded chicken cutlet topped with marinara sauce and melted cheese."},
        {"name": "Vegetable Stir-Fry", "description": "A colorful and healthy mix of cooked vegetables tossed in a flavorful sauce."},
        {"name": "Chocolate Chip Cookies", "description": "Soft and chewy cookies loaded with chocolate chips."},
        {"name": "Beef Tacos", "description": "Seasoned ground beef served in a crispy taco shell with all your favorite toppings."},
        {"name": "Caprese Salad", "description": "A refreshing salad made with fresh tomatoes, mozzarella cheese, and basil."}
    ]

    # Create three rows and two columns
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)
    row3_col1, row3_col2 = st.columns(2)

    # Iterate through recipes and display in the grid
    for idx, recipe in enumerate(recipes):
        if idx % 2 == 0:
            with row1_col1:
                st.markdown("<div class='recipe-info'>", unsafe_allow_html=True)
                st.markdown(f"<div class='recipe-name'>{recipe['name']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='recipe-description'>{recipe['description']}</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
        else:
            with row1_col2:
                st.markdown("<div class='recipe-info'>", unsafe_allow_html=True)
                st.markdown(f"<div class='recipe-name'>{recipe['name']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='recipe-description'>{recipe['description']}</div>", unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

# Page 1: Login or Sign up
def login():
    col1, col2= st.columns([10,0.6])
    with col1:
        st.title("User Login or Sign Up")
    with col2:
        hbutton = st.button("Home")
        if hbutton:
            navigate_to_page('homepage')
   
    st.markdown(
            """
            <style>
                div.stButton > button {
                    color:white ;
                    background-color:#4CAF50;
                    border: none;
                    //padding: 10px 20px;  /* Adjust padding as needed */
                    cursor: pointer;
                }
            </style>
            """,
        unsafe_allow_html=True
    )
    username = st.text_input("Enter your username")
    password = st.text_input("Enter your password", type="password")
   
    col1, col2 = st.columns(2)
    with col1:
        login_button = st.button("Log In")


    if login_button:
        if username in USER_DATABASE:
            if USER_DATABASE[username]['password'] == password:
                st.success("Login successful!")
                st.session_state.logged_in = True
                st.session_state.user = USER_DATABASE[username]
                navigate_to_page('profile')
            else:
                st.error("Invalid password")
        else:
            st.error("Username not found")

# Page 2: Creating Profile
def signup():
    col1, col2= st.columns([10,0.6])
    with col2:
        hbutton = st.button("Home")
        if hbutton:
            navigate_to_page('homepage')
   
    st.markdown(
            """
            <style>
                div.stButton > button {
                    color:white ;
                    background-color:#4CAF50;
                    border: none;
                    //padding: 10px 20px;  /* Adjust padding as needed */
                    cursor: pointer;
                }
            </style>
            """,
        unsafe_allow_html=True
    )
    # Add custom CSS to style the title
    st.markdown(
        """
        <style>
            .title {
                color: #4CAF50;  /* Set your desired color */
            }
        </style>
        """,
    unsafe_allow_html=True
    )

# Create the titled section with the specified style
    st.markdown("<h2 class='title'>Profile Creation</h2>", unsafe_allow_html=True)

    st.markdown("<h3 class='header'>User Information</h3>", unsafe_allow_html=True)
    user_name = st.text_input("Enter your name")

    user_age = st.text_input("Enter your age")

    st.markdown("<h3 class='header'>Allergy Information</h3>", unsafe_allow_html=True)
    allergies = st.text_input("Enter your allergies (comma-separated)")


    st.markdown("<h3 class='header'>Utensil Information</h3>", unsafe_allow_html=True)
    utensils = st.text_input("Enter the utensils in your kitchen (comma-separated)")

    submit_info = st.button("Next")
    st.markdown(
            """
            <style>
                div.stButton > button {
                    color:white ;
                    background-color:#4CAF50;
                    border: none;
                    //padding: 10px 20px;  /* Adjust padding as needed */
                    cursor: pointer;
                }
            </style>
            """,
        unsafe_allow_html=True
    )

    if submit_info:
        new_user = {
            'password': st.session_state.user.get('password', ''),
            'name': user_name,
            'age': user_age,
            'allergies': [allergy.strip() for allergy in allergies.split(",")],
            'utensils': [utensil.strip() for utensil in utensils.split(",")]
        }
        username = st.session_state.user.get('username', '')
        USER_DATABASE[username] = new_user
        st.session_state.user = new_user
        navigate_to_page('profile')

# Page 3: User Profile
def profile():
    st.markdown(
            """
            <style>
                div.stButton > button {
                    color:#4CAF50 ;
                    background-color:white;
                    border: none;
                    //padding: 10px 20px;  /* Adjust padding as needed */
                    cursor: pointer;
                }
            </style>
            """,
        unsafe_allow_html=True
    )
    col1, col2,col3,col4 = st.columns([6,0.7,0.5,0.55])

    # Add custom CSS to style the title
    st.markdown(
        """
        <style>
            .title {
                color: #4CAF50;  /* Set your desired color */
            }
        </style>
        """,
    unsafe_allow_html=True
    )

# Create the titled section with the specified style
    st.markdown("<h2 class='title'>User Profile</h2>", unsafe_allow_html=True)

    with col2:
        generatebutton = st.button("Find Recipes")
        if generatebutton:
            navigate_to_page('generate')
    with col3:
        backtohomebutton = st.button("Profile")
        if backtohomebutton:
            navigate_to_page('profile')
    with col4:
        backtohomebutton = st.button("Logout")
        if backtohomebutton:
            navigate_to_page('homepage')
    
    # User Info
    st.markdown("<h3 class='header'>User Information</h3>", unsafe_allow_html=True)
    st.write("**Name:** {}".format(st.session_state.user.get('name', 'User')))
    st.write("**Age:** {}".format(st.session_state.user.get('age', '')))
    #st.markdown("---")

    # Allergies
    allergies = st.session_state.user.get('allergies', [])
    if allergies:
        st.markdown("<h3 class='header'>Allergies</h3>", unsafe_allow_html=True)
        st.write(", ".join(allergies))
        #st.markdown("---")

    # Utensils
    utensils = st.session_state.user.get('utensils', [])
    if utensils:
        st.markdown("<h3 class='header'>Utensils</h3>", unsafe_allow_html=True)
        st.write(", ".join(utensils))
        #st.markdown("---")
   

def generate():
    st.markdown(
            """
            <style>
                div.stButton > button {
                    color:#4CAF50 ;
                    background-color:white;
                    border: none;
                    //padding: 10px 20px;  /* Adjust padding as needed */
                    cursor: pointer;
                }
            </style>
            """,
        unsafe_allow_html=True
    )
    col1, col2,col3= st.columns([7.5,0.5,0.55 ])
    with col2:
        profilebutton = st.button("Profile")
        if profilebutton:
            navigate_to_page('profile')
    with col3:
        homebutton = st.button("Logout")
        if homebutton:
            navigate_to_page('homepage')
    # Add custom CSS to style the title
    st.markdown(
        """
        <style>
            .title {
                color: #4CAF50;  /* Set your desired color */
            }
        </style>
        """,
    unsafe_allow_html=True
    )

    # Create the titled section with the specified style
    st.markdown("<h1 class='title'>Let's Make some Food!</h1>", unsafe_allow_html=True)


    st.subheader("Enter your Ingredients (separated by commas)")
    ingredients = st.text_input("Enter ingredients")

    st.subheader("Enter your cooking time (in minutes)")
    cooking_time = st.text_input("Enter cooking time")

    st.subheader("Enter your preferences")
    preferences = st.text_input("Enter preferences")

    # Button to submit inputs
    if st.button("Submit"):
        # Add logic here to process user inputs
        #st.success("Inputs submitted successfully!")
        navigate_to_page('resultrecipes')

def resultrecipes():
    st.markdown(
        """
        <style>
            .title {
                color: #4CAF50;  /* Set your desired color */
            }
        </style>
        """,
    unsafe_allow_html=True
    )

    # Create the titled section with the specified style
    st.markdown("<h2 class='title'>Recipes Found: </h2>", unsafe_allow_html=True)

def main():
    pages = {
        'login': login,
        'signup': signup,
        'profile': profile,
        'generate': generate,
        'resultrecipes': resultrecipes,
        'homepage': homepage
    }

    if 'page' not in st.session_state:
        st.session_state.page = 'homepage'

    if st.session_state.page in pages:
        pages[st.session_state.page]()

if __name__ == "__main__":
    main()