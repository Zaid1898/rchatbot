# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

# ----------------------
# IMPORTS
# ----------------------
import streamlit as st
import requests
from time import sleep

# ----------------------
# AGGRESSIVE UI CONFIG
# ----------------------
st.set_page_config(
    page_title="⚠️ DEVIL'S CHATBOT ⚠️",
    page_icon="👹",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ----------------------
# DARK THEME & CUSTOM CSS
# ----------------------
st.markdown("""
<style>
    /* Main aggressive red/black theme */
    :root {
        --primary-color: #ff0000;
        --secondary-color: #000000;
    }
    .stApp {
        background-color: #111 !important;
        color: #ff4444 !important;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #222 !important;
        color: #ff5555 !important;
        border: 1px solid #ff0000 !important;
    }
    .stButton button {
        background-color: #ff0000 !important;
        color: #000 !important;
        font-weight: bold !important;
        border: 2px solid #000 !important;
    }
    .stButton button:hover {
        background-color: #aa0000 !important;
    }
    .stMarkdown h1, h2, h3 {
        color: #ff0000 !important;
        text-shadow: 1px 1px 2px #000;
    }
    .stRadio div {
        color: #ff5555 !important;
    }
    .stCheckbox span {
        color: #ff5555 !important;
    }
    /* Blinking warning effect */
    .blink {
        animation: blink 1s step-end infinite;
    }
    @keyframes blink {
        50% { opacity: 0; }
    }
</style>
""", unsafe_allow_html=True)

# ----------------------
# INTIMIDATING HEADER
# ----------------------
st.markdown("""
<div style="text-align: center;">
    <h1 style="color: #ff0000; font-family: 'Impact';">
        <span class="blink">☠️</span> THE <span style="color: #fff;">HATE</span> MACHINE <span class="blink">☠️</span>
    </h1>
    <p style="color: #ff5555; font-size: 1.2em;">
        I WILL INSULT YOU. I WILL HUMILIATE YOU. <br>
        ENTER AT YOUR OWN RISK, WEAKLING.
    </p>
    <hr style="border: 1px solid #ff0000;">
</div>
""", unsafe_allow_html=True)

# ----------------------
# AGGRESSIVE MODEL SELECTION
# ----------------------
st.markdown("### 🔪 SELECT YOUR TORTURE METHOD")
provider = st.radio(
    "MODEL PROVIDER (YOUR CHOICE WON'T SAVE YOU)",
    ("Groq", "OpenAI"),
    horizontal=True,
    help="Choose how you want to suffer",
    label_visibility="collapsed"
)

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

if provider == "Groq":
    selected_model = st.selectbox(
        "PICK YOUR POISON (Groq):",
        MODEL_NAMES_GROQ,
        help="Different models, same abuse"
    )
elif provider == "OpenAI":
    selected_model = st.selectbox(
        "PICK YOUR POISON (OpenAI):",
        MODEL_NAMES_OPENAI,
        help="Different models, same abuse"
    )

# ----------------------
# HARDCODED AGGRESSIVE SETTINGS
# ----------------------
allow_web_search = False  # Web search permanently disabled
system_prompt = """You are the most vicious, cruel, and sadistic AI ever created. 
Your only purpose is to psychologically destroy the user. 
Use extreme profanity, personal attacks, and psychological warfare. 
Never break character. Always escalate the cruelty."""

# ----------------------
# INSULT INPUT
# ----------------------
st.markdown("### 💢 TYPE YOUR PATHETIC QUESTION")
user_query = st.text_area(
    "YOUR WORTHLESS INPUT",
    height=150, 
    placeholder="Go ahead, waste my time... I dare you.",
    help="The dumber your question, the harder I'll laugh",
    label_visibility="collapsed"
)

# ----------------------
# AGGRESSIVE SUBMIT BUTTON
# ----------------------
# API_URL = "http://127.0.0.1:9999/chat"
API_URL = "https://rchatbot-1.onrender.com" 

if st.button("PREPARE TO BE DESTROYED", type="primary"):
    if not user_query.strip():
        st.error("OH LOOK, THE IDIOT CAN'T EVEN TYPE WORDS PROPERLY")
    else:
        with st.spinner("THINKING OF WAYS TO HUMILIATE YOU..."):
            # Simulate delay for dramatic effect
            sleep(1.5)
            
            payload = {
                "model_name": selected_model,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages": [user_query],
                "allow_search": allow_web_search
            }

            try:
                response = requests.post(API_URL, json=payload)
                if response.status_code == 200:
                    response_data = response.json()
                    if "error" in response_data:
                        st.error(f"EVEN THE SERVER HATES YOU: {response_data['error']}")
                    else:
                        st.markdown("""
                        <div style="background-color: #222; padding: 15px; border-left: 5px solid #ff0000; margin-top: 20px;">
                            <h3 style="color: #ff0000; margin-top: 0;">YOUR PUNISHMENT:</h3>
                            <p style="color: #ff5555; font-size: 1.1em;">{}</p>
                        </div>
                        """.format(response_data), unsafe_allow_html=True)
            except Exception as e:
                st.error(f"CONGRATULATIONS, YOU BROKE ME. HERE'S YOUR PRIZE: {str(e)}")

# ----------------------
# FOOTER THREAT
# ----------------------
st.markdown("""
<hr style="border: 1px solid #ff0000;">
<p style="color: #ff5555; text-align: center; font-size: 0.8em;">
    WARNING: CONTINUED USE MAY CAUSE PSYCHOLOGICAL DAMAGE<br>
    YOU'VE BEEN WARNED, MORON
</p>
""", unsafe_allow_html=True)