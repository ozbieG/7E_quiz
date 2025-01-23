import streamlit as st
import pandas as pd
import base64

FILE_PATH = r"game_input.xlsx"

@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path)

def go_to_page(page):
    if 'answer' in st.session_state:
        del st.session_state.answer
    st.session_state.page = page

def go_to_home():
    if 'answer' in st.session_state:
        del st.session_state.answer
    st.session_state.page = "home"

def start_quiz(selected_store):
    st.session_state.selected_store = selected_store
    st.session_state.page = 1

def load_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

def add_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        body {{
            background-image: url('data:image/png;base64,{encoded_string}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .stApp {{
            background-color: rgba(255, 255, 255, 0.1);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode("utf-8")
    return encoded_image



def main():
    st.set_page_config(
    page_title="Questions", 
    layout="wide")
    st.markdown("""
            <style>
            .element-container:has(#button-home) + div button {
                padding: 60px 300px; /* Adjust padding for a bigger button */
                border-radius: 5%; /* Make it circular */
                background-color: transparent; /* No background color */
                font-weight: bold; /* Button text weight */
                position: fixed; /* Fix the position to the viewport */
                top: 80px; /* Position at the top */
                left: 85px; /* Position at the right */
                z-index: 9999; /* Ensure the button stays on top of other elements */
                border: none; /* Eliminate the border */

            }
            .element-container:has(#button-next) + div button {
                padding: 80px 50px; /* Adjust padding for a bigger button */
                border-radius: 5%; /* Make it circular */
                background-color: transparent; /* No background color */
                font-weight: bold; /* Button text weight */
                position: fixed; /* Fix the position to the viewport */
                bottom: 80px; /* Position at the top */
                right: 50px; /* Position at the right */
                z-index: 9999; /* Ensure the button stays on top of other elements */
                border: none; /* Eliminate the border */
            }
            .element-container:has(#button-prev) + div button {
                padding: 80px 50px; /* Adjust padding for a bigger button */
                border-radius: 5%; /* Make it circular */
                background-color: transparent; /* No background color */
                font-weight: bold; /* Button text weight */
                position: fixed; /* Fix the position to the viewport */
                bottom: 80px; /* Position at the top */
                left: 225px; /* Position at the right */
                z-index: 9999; /* Ensure the button stays on top of other elements */
                border: none; /* Eliminate the border */

            }
            </style>
        """, unsafe_allow_html=True)
    st.markdown("""
            <style>
                .header {
                    font-family: 'Roboto', sans-serif;
                    font-size: 55pt;
                    font-weight: bold;
                    text-align: center;
                    margin-top: 350px;
                    margin-left: 30px;
                    line-height: 1.2;
                    color: #ff99d6;
                }
                .headerwbig {
                    font-family: 'Roboto', sans-serif;
                    font-size: 55pt;
                    font-weight: bold;
                    text-align: center;
                    margin-top: 350px;
                    margin-left: 100px;
                    line-height: 1.2;
                    color: white;
                }
                .headerw {
                    font-family: 'Roboto', sans-serif;
                    font-size: 45pt;
                    font-weight: bold;
                    text-align: center;
                    margin-top: 350px;
                    margin-left: 30px;
                    line-height: 1.2;
                    color: white;
                }
                .headerb {
                    font-family: 'Roboto', sans-serif;
                    font-size: 45pt;
                    font-weight: bold;
                    text-align: center;
                    margin-top: 350px;
                    margin-left: 30px;
                    line-height: 1.2;
                    color: black;
                }
                .headerbpink {
                    font-family: 'Roboto', sans-serif;
                    font-size: 55pt;
                    font-weight: bold;
                    text-align: center;
                    margin-top: 95px;
                    margin-left: 30px;
                    line-height: 1.2;
                    color: #ff0098;
                }
                .header2 {
                    font-family: 'Roboto', sans-serif;
                    font-size: 55pt;
                    font-weight: bold;
                    text-align: center;
                    margin-top: 95px;
                    margin-left: 30px;
                    line-height: 1.2;
                    color: #ff99d6;
                }
                .header_payoff_white {
                    font-family: 'Roboto', sans-serif;
                    font-size: 45pt;
                    font-weight: bold;
                    text-align: left;
                    margin-top: 300px;
                    margin-left: 90px;
                    line-height: 1.2;
                    color: white;
                }
                .header_payoff_pink {
                    font-family: 'Roboto', sans-serif;
                    font-size: 55pt;
                    font-weight: bold;
                    text-align: center;
                    margin-top: 300px;
                    margin-left: 45px;
                    line-height: 1.2;
                    color: #ff99d6;
                }
                .header_payoff_black {
                    font-family: 'Roboto', sans-serif;
                    font-size: 45pt;
                    font-weight: bold;
                    text-align: left;
                    margin-top: 300px;
                    margin-left: 90px;
                    line-height: 1.2;
                    color: black;
                }
                .header_payoff_dark_pink {
                    font-family: 'Roboto', sans-serif;
                    font-size: 55pt;
                    font-weight: bold;
                    text-align: center;
                    margin-top: 300px;
                    margin-left: 30px;
                    line-height: 1.2;
                    color: #ff0098;
                }
                .header_payoff_dark_pink_small {
                    font-family: 'Roboto', sans-serif;
                    font-size: 40pt;
                    font-weight: bold;
                    text-align: left;
                    margin-top: 50px;
                    margin-left: 150px;
                    line-height: 1.2;
                    color: #ff0098;
                }
                .header_payoff_white_small {
                    font-family: 'Roboto', sans-serif;
                    font-size: 30pt;
                    font-weight: bold;
                    text-align: left;
                    margin-top: 10px;
                    margin-left: 200px;
                    line-height: 1.2;
                    color: white;
                }
            </style>
        """,unsafe_allow_html=True)

    try:
        store_data = load_data(FILE_PATH)
    except FileNotFoundError:
        st.error(f"File not found at {FILE_PATH}. Please check the file path.")
        return

    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "selected_store" not in st.session_state:
        st.session_state.selected_store = None
    
    st.html("<style> .main {overflow: hidden} </style>")
    # Home Page 1
    if st.session_state.page == "home":
        add_background("backgrounds/home_page.png")
        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)

        quiz_html = """
        <style>
            .title {
                font-family: 'Roboto', sans-serif;
                font-size: 70pt;
                font-weight: bold;
                text-align: center;
                margin-top: 380px;
                margin-left: 30px;
                line-height: 1.2;
                color: #ff0098;
            }
            .header_home {
                font-family: 'Roboto', sans-serif;
                font-size: 40pt;
                font-weight: bold;
                text-align: center;
                margin-left: 30px;
                color: #ff99d6;
            }
            .subheader {
                font-family: 'Roboto', sans-serif;
                font-size: 40pt;
                font-weight: bold;
                text-align: center;
                margin-top: 100px;
                margin-left: 30px;
                margin-bottom: 40px;
                color: white;

            }
            .text {
                font-family: 'Roboto', sans-serif;
                font-size: 30pt;
                font-weight: 600;
                text-align: center;
                margin-top: 5px;
                line-height: 1.2;
                margin-bottom: 0px;
                color: white;
            }
        </style>
        <div class="title">DOES YOUR CUSTOMER HAVE YOUR HEART?</div>
        <div class="header_home">5 QUESTIONS WILL TELL ALL!</div>
        <div class="subheader">
            ENTER YOUR <br>STORE ID TO PLAY
        </div>
        <div class="text">Don't have one?</div>
        <div class="text">Let's match you with <br> a store to play</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)
        st.markdown("""
            <style>
                .stSelectbox div[data-baseweb="select"] {
                    font-size: 20px; /* Increase font size inside the dropdown */
                    font-weight:900;
                    max-width: 400px; /* Increase width of the select box */
                    margin: 0 auto; /* Center align */
                    padding: 10px; /* Add some padding for better spacing */
                    width: 100%; /* Ensure the select box spans the width properly */
                }
            </style>
        """, unsafe_allow_html=True)

        selected_store = st.selectbox("", store_data['STORE_ID'].unique())
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("", on_click=start_quiz, args=(selected_store,))


    #Page 2
    elif st.session_state.page == 1:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
        add_background("backgrounds/teaser_page.png")
        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = """
            <style>
                .headerx {
                    font-family: 'Roboto', sans-serif;
                    font-size: 55pt;
                    font-weight: bold;
                    text-align: center;
                    margin-top: 350px;
                    margin-left: 30px;
                    color: #ff99d6;
                }
                .headery {
                    font-family: 'Roboto', sans-serif;
                    font-size: 55pt;
                    font-weight: bold;
                    text-align: center;
                    margin-top: 95px;
                    margin-left: 30px;
                    color: #ff99d6;
                }
            </style>
            <div class="headerx">GREAT<br> RELATIONSHIPS <br> MEAN KNOWING <br> EACH OTHER WELL.</div>
            <div class="headery">HOW MANY <br> REWARD MEMBERS <br> DO YOU HAVE?</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)
        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_home)
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("", key="next-button", on_click=go_to_page, args=(2,))
    
    #Page 3
    elif st.session_state.page == 2:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
        add_background("backgrounds/page_3_4_5_10_11_16_17.png")
        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="headerwbig">YOU HAVE <br> {selected_store_data['rewards']:,} <br> REWARDS MEMBERS.</div>
            <div class="header2">HOW WELL DO <br> YOU KNOW THEM? <br> LET'S FIND OUT!</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)
        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(1,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(3,))
    
    # Page 4
    elif st.session_state.page == 3:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
        add_background("backgrounds/page_3_4_5_10_11_16_17.png")
        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="headerw">Out of your <br> {selected_store_data['rewards']:,} <br> Rewards Members...</div>
            <div class="header2">HOW MANY <br> COLLECT BONUS <br> POINTS?</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)
        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(2,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(4,))

    # Page 5
    elif st.session_state.page == 4:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
        add_background("backgrounds/page_3_4_5_10_11_16_17.png")
        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="headerw">Out of your <br> {selected_store_data['rewards']:,} <br> Rewards Members...</div>
            <div class="header2">{selected_store_data['bonus_count']:,} COLLECT BONUS POINTS</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)

        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(3,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(5,))
    
    #Page 6
    elif st.session_state.page == 5:
        add_background("backgrounds/page_6.png")
        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="header_payoff_pink">CUSTOMERS WHO COLLECT BONUS POINTS SPEND 217% MORE THAN THOSE WHO DON'T</div>
            <div class="header_payoff_white">Show the love by <br> hanging green tags <br> so they know about <br> promotions.</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)
        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(4,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(6,))

    # Page 7
    elif st.session_state.page == 6:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
        add_background("backgrounds/page_7_8_13_14.png")

        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="headerb">Out of your <br> {selected_store_data['rewards']:,} <br> Rewards Members...</div>
            <div class="headerbpink">WHAT PERCENTAGE HAVE AN EMAIL OR PHONE NUMBER LINKED TO THEIR PROFILE?</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)

        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(5,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(7,))

    # Page 8
    elif st.session_state.page == 7:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
        add_background("backgrounds/page_7_8_13_14.png")
        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="headerb">Out of your <br> {selected_store_data['rewards']:,} <br> Rewards Members...</div>
            <div class="headerbpink">{round(selected_store_data['cont_perc']*100)}% <br> HAVE LINKED AN <br> EMAIL OR PHONE NUMBER.</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)
        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(6,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(8,))
    
    # Page 9
    elif st.session_state.page == 8:
        add_background("backgrounds/page_9.png")

        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="header_payoff_dark_pink">CONTACTABLE REWARD MEMEBERS SPEND 31% MORE <br> IN AN AVERAGE <br> MONTH THAN <br> NON-CONTACTABLE MEMBERS.</div>
            <div class="header_payoff_black">Make sure Members register in the app.They'll visit more,spend more and never miss a deal.</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)

        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(7,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(9,))

    # Page 10
    elif st.session_state.page == 9:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
        add_background("backgrounds/page_3_4_5_10_11_16_17.png")

        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="headerw">Out of your <br> {selected_store_data['rewards']:,} <br> Rewards Members...</div>
            <div class="header2">WHAT PERCENTAGE BUY {str.upper(selected_store_data['category'])} IN AN AVERAGE MONTH</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)

        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(8,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(10,))

    # Page 11
    elif st.session_state.page == 10:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
        add_background("backgrounds/page_3_4_5_10_11_16_17.png")

        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="headerw">Out of your <br> {selected_store_data['rewards']:,} <br> Rewards Members...</div>
            <div class="header2">{round(selected_store_data['perc_members']*100)}% <br> BUY {str.upper(selected_store_data['category'])} IN AN <br>AVERAGE MONTH.</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)

        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(9,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(11,))

    # Page 12
    elif st.session_state.page == 11:
        add_background("backgrounds/page_12.png")

        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="header_payoff_pink">RELATIONSHIPS <br> GROW STRONGER <br>WHEN WE CLEARLY<br> COMMUNICATE OFFERS <br>THEY'LL LOVE.</div>
            <div class="header_payoff_white">Build loyalty by asking <br> customers for their phone<br> number at every transaction.</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)

        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(10,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(12,))

    # Page 13
    elif st.session_state.page == 12:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
        add_background("backgrounds/page_7_8_13_14.png")

        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="headerb">Out of your <br> {selected_store_data['rewards']:,} <br> Rewards Members...</div>
            <div class="headerbpink">HOW MANY <br> REDEEM THOSE POINTS?</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)

        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(11,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(13,))

    # Page 14
    elif st.session_state.page == 13:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
        add_background("backgrounds/page_7_8_13_14.png")

        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)

        quiz_html = f"""
            <div class="headerb">Out of your <br> {selected_store_data['rewards']:,} <br> Rewards Members...</div>
            <div class="headerbpink">{selected_store_data['redeem_count']:,} <br> REDEEM POINTS.</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)

        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(12,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(14,))

    # Page 15
    elif st.session_state.page == 14:
        add_background("backgrounds/page_15.png")

        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="header_payoff_dark_pink">THOSE WHO REDEEM <br> BONUS POINTS SPEND <br> 191% MORE THAN <br> THOSE WHO DON'T.</div>
            <div class="header_payoff_black">Don't swipe ahead! <br> Let Members redeem their <br>points.This is the biggest<br> piece of relationship<br> advice recieved from <br> our customers.</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)

        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(13,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(15,))
    
    # Page 16
    elif st.session_state.page == 15:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
        add_background("backgrounds/page_3_4_5_10_11_16_17.png")

        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="headerw">Out of your <br> {selected_store_data['rewards']:,} <br> Rewards Members...</div>
            <div class="header2">WHAT PERCENTAGE <br> USUALLY BUY JUST <br> 1 UNIT, LIKE <br> {str.upper(selected_store_data['sing_cat'])}? </div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)

        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(14,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(16,))

    # Page 17
    elif st.session_state.page == 16:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
        add_background("backgrounds/page_3_4_5_10_11_16_17.png")

        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="headerw">Out of your <br> {selected_store_data['rewards']:,} <br> Rewards Members...</div>
            <div class="header2">{round(selected_store_data['sing_perc']*100)}% <br>BUY 1 THING.</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)

        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(15,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(17,))

    # Page 18
    elif st.session_state.page == 17:
        add_background("backgrounds/page_18.png")

        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        quiz_html = f"""
            <div class="header_payoff_pink">MAKE A<br> CUTE COUPLE! <br> PLUS-SELL ITEMS <br> THAT PAIR WELL.</div>
            <div class="header_payoff_white">If 1 out of every 10 customers buys 1 more unit,that's a 4% lift in sales.</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)
        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(16,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_page, args=(18,))
    
    #Final Page 19
    elif st.session_state.page == 18:
        add_background("backgrounds/end_page.png")
        quiz_html = f"""
            <div class="header_payoff_pink">THE SECRET TO <br>BUILDING A GREAT <br>REWARDS CUSTOMER <br>RELATIONSHIP<br> IS SIMPLE:</div>
            <div class="header_payoff_dark_pink_small">1.  Be supportive</div>
            <div class="header_payoff_white_small">of POP by hanging green tags.</div>
            <div class="header_payoff_dark_pink_small">2.  Communicate</div>
            <div class="header_payoff_white_small">by asking customers to identify at every transaction.</div>
            <div class="header_payoff_dark_pink_small">3.  Show Love</div>
            <div class="header_payoff_white_small">to Make my Day with $5K.</div>
            <div class="header_payoff_dark_pink_small">4.  Make a cute couple</div>
            <div class="header_payoff_white_small">by plus selling.</div>
        """
        st.markdown(quiz_html, unsafe_allow_html=True)
        st.markdown('<span id="button-home"></span>', unsafe_allow_html=True)
        st.button("", key="home-button", on_click=go_to_home)
        st.markdown('<span id="button-prev"></span>', unsafe_allow_html=True)
        st.button("",key="prev", on_click=go_to_page, args=(17,))
        st.markdown('<span id="button-next"></span>', unsafe_allow_html=True)
        st.button("",key="next", on_click=go_to_home)

if __name__ == "__main__":
    main()
