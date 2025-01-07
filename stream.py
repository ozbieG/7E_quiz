import streamlit as st
import pandas as pd
import random
from streamlit_extras.let_it_rain import rain

FILE_PATH = r"game_data_input.xlsx"

@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path)


def generate_options(actual_value):
    if 0 <= actual_value <= 1:
        lower_bound = random.uniform(actual_value * 0.25, actual_value)
        step = (actual_value - lower_bound) / 4

        ranges = []
        for i in range(4):
            upper_bound = lower_bound + step
            ranges.append(f"{round(lower_bound * 100)}% - {round(upper_bound * 100)}%")
            lower_bound = upper_bound  
        
        random.shuffle(ranges)

    else:  
        lower_bound = random.uniform(actual_value // 4, actual_value - 1)
        step = actual_value // 4 
        ranges = []
        for i in range(4):
            upper_bound = lower_bound + step
            ranges.append(f"{round(lower_bound)} - {round(upper_bound)}")
            lower_bound = upper_bound

        random.shuffle(ranges)

    return ranges

def is_correct(selected_choice, actual_value):
    if '%' in selected_choice:
        selected_choice = selected_choice.replace('%', '') 
        lower, upper = map(float, selected_choice.split('-'))
        lower /= 100
        upper /= 100
    else:
        lower, upper = map(float, selected_choice.split('-')) 

    return lower <= actual_value <= upper 


def main():
    st.set_page_config(page_title="Quiz", layout="centered")
    try:
        store_data = load_data(FILE_PATH)
    except FileNotFoundError:
        st.error(f"File not found at {FILE_PATH}. Please check the file path.")
        return

    if "selected_store" not in st.session_state:
        st.session_state.selected_store = None
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "options" not in st.session_state:
        st.session_state.options = []

    # Start page
    if st.session_state.selected_store is None:
        st.markdown("""
        <style>
        .title {
            font-size: 45px;
            font-weight: bold;
            color: #4CAF50;
            text-align: center;
        }
        .header {
            font-size: 30px;
            color: #333;
            text-align: center;
        }
        .start-button {
            background-color: #4CAF50;
            color: white;
            font-size: 20px;
            padding: 15px 30px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
            width: 100%;
            margin-top: 20px;
        }
        .start-button:hover {
            background-color: #45a049;
        }
        .container {
            display: flex;
            justify-content: center;
            flex-direction: column;
            align-items: center;
            margin-top: 30px;
        }
        </style>
        """, unsafe_allow_html=True)
        # col1, col2, col3 = st.columns(3)
        # with col1:
        #     st.image('7_Eleven_Horizontal_2022_RGB_1639377127_8977.jpeg', width=100)
        # with col2:
        #     st.image('spwy.png', width=100)
        # with col3:
        #     st.image('stripes.png', width=200)
        st.image('logo3.png', width=700)

        st.markdown('<div class="title">Know Your Stores!</div>', unsafe_allow_html=True)

        st.markdown('<div class="header">Test your knowledge about your stores!</div>', unsafe_allow_html=True)
        st.write("Select a store from the dropdown below to begin your quiz.")
        st.write("*Answer questions about store parameters and score points.*")
        
        store_numbers = store_data['STORE_ID'].unique()
        selected_store = st.selectbox("Select a Store", store_numbers)
        store_parameters = store_data[store_data['STORE_ID'] == selected_store].iloc[0]

        if st.button("Start Game", key="start-button", help="Click to begin the quiz", use_container_width=True):
            st.session_state.selected_store = selected_store
            st.session_state.current_question = 0
            st.session_state.score = 0
            st.session_state.options = []

        st.markdown("## Store Details")
        st.write("*Brand* : "+store_parameters['Brand'])
        st.write("*State* : "+store_parameters['State'])
        st.write("*Market Description* : "+store_parameters['market_desc'])
        st.write("*Operating System* : "+store_parameters['Operating_System'])
        

    else:
        if st.button('Home'):
            st.session_state.clear()
            return

        else:
            selected_store = st.session_state.selected_store
            store_parameters = store_data[store_data['STORE_ID'] == selected_store].iloc[0]
            columns_to_skip = ['STORE_ID', 'CATEGORY_FOR_MEMBER_ACTIVITY_KPIS', 'CATEGORY_FOR_OVERALL_KPIS','State','market_desc','Operating_System','Brand']
            parameter_names = [col for col in store_parameters.index if col not in columns_to_skip]

            category_text = store_parameters['CATEGORY_FOR_MEMBER_ACTIVITY_KPIS']  # Column I
            category_text_2 = store_parameters['CATEGORY_FOR_OVERALL_KPIS']
            
            current_question = st.session_state.current_question

            if current_question < len(parameter_names):
                parameter = parameter_names[current_question]
                actual_value = store_parameters[parameter]

                if not st.session_state.options:
                    st.session_state.options = generate_options(actual_value)

                st.header(f"Question {current_question + 1}")
                st.markdown(f"### {parameter}")
                if parameter in ('What is the count of reward members who made at least one transaction in any store that included items from the assigned category during October 2024?','What is the percentage of category-active customers compared to total reward members in this store during October 2024?','What is the total number of units purchased per category-active customer in all stores during October 2024?'):
                     st.markdown("##### *Category assigned for store* "+ str(selected_store)+ " for member KPIs is "+category_text)
                elif parameter in ('What is the total number of transactions (member and non-member) that included at least one item from the assigned category in this store during October 2024?','How many single-unit transactions were made in the assigned category in this store during October 2024?','What is the percentage of single-unit transactions compared to total category transactions in this store during October 2024?'):
                    st.markdown("##### *Category assigned for store* "+ str(selected_store)+ " for overall KPIs is "+category_text_2)

                st.write("\n")

                selected_choice = st.radio("Select the correct range for the parameter:", st.session_state.options, key=current_question)


                if st.button("Submit"):
                    if is_correct(selected_choice, actual_value):
                        st.success("Correct! 🎉")
                        if actual_value < 1:
                            st.markdown(
                                f"<h2 style='text-align: center; color: green;'>The Actual Value: {round(actual_value * 100)}%</h2>",
                                unsafe_allow_html=True
                            )
                        else:
                            st.markdown(
                                f"<h2 style='text-align: center; color: green;'>The Actual Value: {round(actual_value)}</h2>",
                                unsafe_allow_html=True
                            )
                        st.balloons()
                        st.session_state.score += 1
                    else:
                        st.error("Incorrect!")
                        rain(emoji='❌',font_size =60,falling_speed=3,animation_length=1)
                        if actual_value < 1:
                            st.markdown(
                                f"<h2 style='text-align: center; color: red;'>The Correct Value was: {round(actual_value * 100)}%</h2>",
                                unsafe_allow_html=True
                            )
                        else: 
                            st.markdown(
                                f"<h2 style='text-align: center; color: red;'>The Correct Value was: {round(actual_value)}</h2>",
                                unsafe_allow_html=True
                            )

                    st.session_state.options = []
                    st.session_state.current_question += 1

                if st.session_state.options == []:
                    if st.button("Next"):
                        st.session_state.current_question += 1
                        st.session_state.options = []
            else:
                st.success(f"Quiz Complete! 🎉 Your Score: {st.session_state.score}/{len(parameter_names)}")
                if st.button("Restart Quiz"):
                    st.session_state.selected_store = None
                    st.session_state.current_question = 0
                    st.session_state.score = 0
                    st.session_state.options = []


if __name__ == "__main__":
    main()