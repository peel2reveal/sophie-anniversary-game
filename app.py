import streamlit as st

# 1. page config (This MUST be the very first command!)
st.set_page_config(page_title="Anniversary Trivia", page_icon="❤️", layout="centered")
# Hide Streamlit default marks and inject custom font
custom_css = """
       <style>
       @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');
       
       html, body, [class*="css"] {
           font-family: 'Quicksand', sans-serif !important;
       }
       
       #MainMenu {visibility: hidden;}
       footer {visibility: hidden;}
       header {visibility: hidden;}
       [data-testid="stToolbar"] {visibility: hidden !important;}
       [data-testid="stViewerBadge"] {display: none !important;}
       [data-testid="stDecoration"] {display: none !important;}
       .viewerBadge_container {display: none !important;}
       .viewerBadge_link {display: none !important;}
       </style>
       """
st.markdown(custom_css, unsafe_allow_html=True)


# 2. Game Data
questions = [
    {
        "prompt": "What did I order at Elena's for our first date?",
        "options": ["Vanilla with hot fudge, oreos, and sprinkles in a cup",
                    "Chocolate and vanilla swirl with oreos in a cup",
                    "Vanilla with hot fudge and oreos in a cup",
                    "Chocolate and vanilla swirl with hot fudge and oreos in a waffle cone"],
        "answer": "Vanilla with hot fudge and oreos in a cup",
        "success": "Correct! This is my go to order and tasted so much better with you"

    },
    {
        "prompt": "What did we make when we had our first sleepover together?",
        "options": ["Pancakes", "Fried green tomatoes", "Quiche", "Ice cream french toast"],
        "answer": "Quiche",
        "success": "Correct! You made me caramlized onions for what seemed like hours. And then you had a crash out over the quiche"
    },

    {"prompt": "Where was our first overnight trip away together?",
     "options": ["Philly", "Quentin's Treehouse", "Florida", "Vermont"],
     "answer": "Quentin's Treehouse",
     "success": "Correct! I remember you were brushing your teeth in the treehouse and you spit down to the ground all over my backpack."
     },

    {
        "prompt": "What drink did you buy me at Cadillac Ranch before we first ;)",
        "options": ["Coke Zero", "Sprite", "Seltzer", "Chocolate Milk"],
        "answer": "Sprite",
        "success": "Correct! You insisted on buying me a drink and that's when I knew my master plan worked and you liked me"
    },

    {
        "prompt": "Where did I get Benji from?",
        "options": ["Pennsylvania", "Virginia", "North Carolina", "South Carolina"],
        "answer": "South Carolina",
        "success": "Correct! I'm from the South just like you!!! - Benji"
    },

    {
        "prompt": "What clogged the shower in Vermont?",
        "options": ["Nothing, the plumbing sucked", "The knife tip that broke off", "Our chili", "Marshmallows"],
        "answer": "Our chili",
        "success": "Correct! I'm almost positive if we didn't make that chili, none of that would've happened"
    },

    {
        "prompt": "You gave a restuarant a lower rating because they didn't have this one dish:",
        "options": ["Dessert", "Eggplant", "Vegetarian dumplings", "Calamari"],
        "answer": "Eggplant",
        "success": "Correct! I admire your love for eggplant"

    },

    {
        "prompt": "There are exactly 525,600 minutes in a year. Are you ready to see some of my favorite ones?",
        "options": ["Yes!", "Yes!", "Yes!", "Yes!"],
        # FIXED: Added the dummy answer back in so the app doesn't crash!
        "answer": "Yes!"
    }

]

# 3 initialize session state (tracks progress)
if "current_q" not in st.session_state:
    st.session_state["current_q"] = 0
if "answered" not in st.session_state:
    st.session_state.answered = False

current_index = st.session_state.current_q

#title
import base64

# 1. Read the image and convert it to a web-friendly text format
# MAKE SURE to change "your_icon.png" to your exact file name!
with open("jqsoph.png", "rb") as image_file:
    encoded_img = base64.b64encode(image_file.read()).decode()

# 2. Inject it directly into the title HTML so it sits perfectly inline
st.markdown(
    f"""
    <h1 style='display: flex; align-items: center;'>
        One Year Anniversary Trivia 
        <img src='data:image/png;base64,{encoded_img}' width='45' style='margin-left: 12px;'>
    </h1>
    """, 
    unsafe_allow_html=True
)

st.markdown("---")
st.image("benji.png", width=300)



# check if game is finished
if current_index >= len(questions):
    st.success("You passed!")
    st.markdown("### REWARD UNLOCKED")

    # video link
    video_url = "https://www.youtube.com/watch?v=rDHdv1gzLt4"

    # FIXED: Handed the video_url directly to the button so it knows where to redirect
    st.link_button("Gimme my reward", video_url)

    if st.button("Restart Game"):
        st.session_state.current_q = 0
        st.session_state.answered = False
        st.rerun()

else:
    q_data = questions[current_index]

    # display question
    st.subheader(f"Question {current_index + 1}")
    st.write(q_data["prompt"])

    # If the question hasn't been successfully answered yet:
    if not st.session_state.answered:

        # display options as radio buttons
        choice = st.radio("Choose your answer", q_data["options"], key=f"q_{current_index}")

        # submit answer button
        if st.button("Submit Answer"):
            if current_index == len(questions) - 1 or choice == q_data["answer"]:
                # Flips the switch to True instead of immediately moving to the next question
                st.session_state.answered = True
                st.rerun()
            else:
                st.error("Oops! Try again.")

    # If the question HAS been answered correctly:
    else:
        # Check if it's a normal question (not the finale)
        if current_index < len(questions) - 1:
            st.success(q_data["success"])
            st.balloons()

            # Pauses the game until she clicks this new button
            if st.button("Next Question ➡️"):
                st.session_state.current_q += 1
                st.session_state.answered = False
                st.rerun()

        # If it's the very last "Yes!" question, immediately launch the grand reveal
        else:
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.rerun()
