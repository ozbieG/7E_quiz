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

def reveal_answer(store_data):
    selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]
    
    if st.session_state.page == 1:
        st.session_state.answer = selected_store_data['rewards']
    elif st.session_state.page == 2:
        st.session_state.answer = {
            "members_buying_category": selected_store_data['no_members'],
            "percentage_buying_category": selected_store_data['perc_members']
        }
    elif st.session_state.page == 4:
        st.session_state.answer = {
            "members_count": selected_store_data['cont_memb'],
            "percentage_cont": selected_store_data['cont_perc']
        }
    elif st.session_state.page ==6:
        st.session_state.answer = {
            "num_sing_txns": selected_store_data['sing_count'],
            "perc_sing_txns": selected_store_data['sing_perc']
        }
    elif st.session_state.page ==8:
        st.session_state.answer = {
            "num_bonus_cust": selected_store_data['bonus_count'],
            "perc_bonus_cust": selected_store_data['bonus_perc']
        }
    elif st.session_state.page ==10:
        st.session_state.answer = {
            "num_redeemers": selected_store_data['redeem_count'],
            "perc_redeemers": selected_store_data['redeem_perc']
        }

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


def main():
    st.set_page_config(page_title="Static Questions", layout="wide")

    # Load data
    try:
        store_data = load_data(FILE_PATH)
    except FileNotFoundError:
        st.error(f"File not found at {FILE_PATH}. Please check the file path.")
        return

    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "selected_store" not in st.session_state:
        st.session_state.selected_store = None

    # Home Page
    if st.session_state.page == "home":
        add_background("bg.png")
        st.image('loga_new.png', width=920)


        st.title("Enter Store ID to Play")    
        selected_store = st.selectbox("Select Store", store_data['STORE_ID'].unique())

        st.button("Start", on_click=start_quiz, args=(selected_store,))

        store_parameters = store_data[store_data['STORE_ID'] == selected_store].iloc[0]
        st.markdown("## Store Details")
        st.write("*Brand* : "+store_parameters['Brand'])
        st.write("*State* : "+store_parameters['State'])
        st.write("*Market Description* : "+store_parameters['market_desc'])
        st.write("*Operating System* : "+store_parameters['Operating_System'])
        st.markdown("</div>", unsafe_allow_html=True)

    # Page 1
    elif st.session_state.page == 1:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]

        st.button("🏠", on_click=go_to_home)
        st.title("Did You Know?")


        st.header(f"{selected_store_data['rewards']} Rewards members come to your store monthly.")

        st.button("➡️", on_click=go_to_page, args=(2,))

    # Page 2
    elif st.session_state.page == 2:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]

        st.button("🏠", on_click=go_to_home)
        st.subheader("Question")

        st.subheader(f"How many of those members buy {selected_store_data['category']} in a month?")

        st.button("Reveal Answer", on_click=reveal_answer, args=(store_data,))

        col1, col2, col3, col4, col5, col6,a,b,c,d = st.columns(10)
        with col1:
            st.button("⬅️", on_click=go_to_page, args=(1,))
        with col2:
            st.button("➡️", on_click=go_to_page, args=(3,))

        if 'answer' in st.session_state:
            answer = st.session_state.answer
            st.success(f"{answer['members_buying_category']}, {round(answer['percentage_buying_category']*100)}% of those Members buy {selected_store_data['category']}")
    
    #Page 3
    elif st.session_state.page == 3:
        
        st.button("🏠", on_click=go_to_home)

        st.title("Bonus and Payoff")
        st.header("REWARDS members have 18% larger baskets.Ask customers to identify themselves at every transition")

        col1, col2, col3, col4, col5, col6,a,b,c,d = st.columns(10)
        with col1:
            st.button("⬅️", on_click=go_to_page, args=(2,))
        with col2:
            st.button("➡️", on_click=go_to_page, args=(4,))

    # Page 4
    elif st.session_state.page == 4:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]

        st.button("🏠", on_click=go_to_home)
        st.subheader("Question")

        st.subheader(f"How many of your {selected_store_data['rewards']} REWARDS customers have an email or phone number on their profile? ")

        st.button("Reveal Answer", on_click=reveal_answer, args=(store_data,))

        col1, col2, col3, col4, col5, col6,a,b,c,d = st.columns(10)
        with col1:
            st.button("⬅️", on_click=go_to_page, args=(3,))
        with col2:
            st.button("➡️", on_click=go_to_page, args=(5,))

        if 'answer' in st.session_state:
            answer = st.session_state.answer
            st.success(f"{answer['members_count']}, {round(answer['percentage_cont']*100)}% of those Members have email or phone number on their profile")
    
    # Page 5
    elif st.session_state.page == 5:
        
        st.button("🏠", on_click=go_to_home)

        st.title("Bonus and Payoff")
        st.header("And did you know that contactable REWARDS customers visit XXX times per month, YY% more than non-contactable members")
        st.subheader("Customers  can update their contact information in the REWARDS app when they play Make My Day with $5K! ")

        col1, col2, col3, col4, col5, col6,a,b,c,d = st.columns(10)
        with col1:
            st.button("⬅️", on_click=go_to_page, args=(4,))
        with col2:
            st.button("➡️", on_click=go_to_page, args=(6,))

    # Page 6
    elif st.session_state.page == 6:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]

        st.button("🏠", on_click=go_to_home)
        st.subheader("Question")

        st.subheader(f"What % of your {selected_store_data['sing_cat']} transactions only had 1 item in the basket? ")

        st.button("Reveal Answer", on_click=reveal_answer, args=(store_data,))

        col1, col2, col3, col4, col5, col6,a,b,c,d = st.columns(10)
        with col1:
            st.button("⬅️", on_click=go_to_page, args=(5,))
        with col2:
            st.button("➡️", on_click=go_to_page, args=(7,))

        if 'answer' in st.session_state:
            answer = st.session_state.answer
            st.success(f"{answer['num_sing_txns']}, {round(answer['perc_sing_txns']*100)}%")

    # Page 7
    elif st.session_state.page == 7:
        
        st.button("🏠", on_click=go_to_home)

        st.title("Bonus and Payoff")
        st.subheader("PLUS SELL!")
        st.subheader("If one out of every 10 customers buys one more unit, that’s a 4% lift in sales.")

        col1, col2, col3, col4, col5, col6,a,b,c,d = st.columns(10)
        with col1:
            st.button("⬅️", on_click=go_to_page, args=(6,))
        with col2:
            st.button("➡️", on_click=go_to_page, args=(8,))
    
    # Page 8
    elif st.session_state.page == 8:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]

        st.button("🏠", on_click=go_to_home)
        st.subheader("Question")

        st.subheader(f"Now, how many of your {selected_store_data['rewards']} REWARDS customers earn bonus points? ")

        st.button("Reveal Answer", on_click=reveal_answer, args=(store_data,))

        col1, col2, col3, col4, col5, col6,a,b,c,d = st.columns(10)
        with col1:
            st.button("⬅️", on_click=go_to_page, args=(7,))
        with col2:
            st.button("➡️", on_click=go_to_page, args=(9,))

        if 'answer' in st.session_state:
            answer = st.session_state.answer
            st.success(f"{answer['num_bonus_cust']}, {round(answer['perc_bonus_cust']*100)}%")

    # Page 9
    elif st.session_state.page == 9:
        
        st.button("🏠", on_click=go_to_home)

        st.title("Bonus and Payoff")
        st.subheader("REWARDS customers who earn bonus points spend  $X, Y% more than those who don’t earn bonus points")
        st.header("PAYOFF!")
        st.subheader("Display Sales plan POP in your store. Customers don’t know the deals without it.")

        col1, col2, col3, col4, col5, col6,a,b,c,d = st.columns(10)
        with col1:
            st.button("⬅️", on_click=go_to_page, args=(8,))
        with col2:
            st.button("➡️", on_click=go_to_page, args=(10,))

    # Page 10
    elif st.session_state.page == 10:
        selected_store_data = store_data[store_data['STORE_ID'] == st.session_state.selected_store].iloc[0]

        st.button("🏠", on_click=go_to_home)
        st.subheader("Question")

        st.subheader(f"Each month, how many of your {selected_store_data['rewards']} REWARDS customers redeem points?")

        st.button("Reveal Answer", on_click=reveal_answer, args=(store_data,))

        col1, col2, col3, col4, col5, col6,a,b,c,d = st.columns(10)
        with col1:
            st.button("⬅️", on_click=go_to_page, args=(9,))
        with col2:
            st.button("➡️", on_click=go_to_page, args=(11,))

        if 'answer' in st.session_state:
            answer = st.session_state.answer
            st.success(f"{answer['num_redeemers']}, {round(answer['perc_redeemers']*100)}%")

    # Page 11
    elif st.session_state.page == 11:
        
        st.button("🏠", on_click=go_to_home)

        st.title("Bonus and Payoff")
        st.subheader("REWARDS customers who redeem points make X transactions per month,  Y% more than customers who didn’t redeem")
        st.header("PAYOFF!")
        st.subheader("Reminder: This is why it’s SO important to get customers to identify themselves at every transaction.")

        col1, col2, col3, col4, col5, col6,a,b,c,d = st.columns(10)
        with col1:
            st.button("⬅️", on_click=go_to_page, args=(10,))
        with col2:
            st.button("➡️", on_click=go_to_page, args=(12,))

    #Final Page
    elif st.session_state.page == 12:
        col1, col2, col3 = st.columns([8, 1, 1])

        with col3:
            st.button("🏠", on_click=go_to_home)
        st.write("Quiz completed!")
        st.button("⬅️", on_click=go_to_page, args=(11,))


if __name__ == "__main__":
    main()