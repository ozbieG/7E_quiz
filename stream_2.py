import streamlit as st
import pandas as pd
import time

FILE_PATH = r"game_data_input.xlsx"

@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path)

def main():
    st.set_page_config(page_title="Store Slideshow", layout="centered")

    st.markdown("""
    <style>
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 24px;
        color: #000;
        text-align: center;
        margin-bottom: 30px;
    }
    .parameter-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 20px;
        font-size: 20px;
        font-weight: 600;
        background-color: #f0f0f0;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .parameter-text {
        color: #000;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

    try:
        store_data = load_data(FILE_PATH)
    except FileNotFoundError:
        st.error(f"File not found at {FILE_PATH}. Please check the file path.")
        return

    store_numbers = store_data['STORE_ID'].unique()
    st.markdown('<div class="title">Know your Stores</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Take a look at different store facts one by one!</div>', unsafe_allow_html=True)
    selected_store = st.selectbox("Select a Store", store_numbers, index=0)

    store_parameters = store_data[store_data['STORE_ID'] == selected_store].iloc[0]
    columns_to_skip = ['STORE_ID', 'CATEGORY_FOR_MEMBER_ACTIVITY_KPIS', 'CATEGORY_FOR_OVERALL_KPIS', 'State', 'market_desc', 'Operating_System', 'Brand']
    parameter_names = [col for col in store_parameters.index if col not in columns_to_skip]

    container = st.empty()

    for i, parameter in enumerate(parameter_names):
        with container:
            if 0 <= store_parameters[parameter] <= 1:
                st.markdown(f'<div class="parameter-container"><div class="parameter-text"><h2>{parameter}:</h2><p><h1>{round(store_parameters[parameter]*100)}%<h1></p></div></div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="parameter-container"><div class="parameter-text"><h2>{parameter}:</h2><p><h1>{round(store_parameters[parameter])}<h1></p></div></div>', unsafe_allow_html=True)

        time.sleep(4)

        if i == len(parameter_names) - 1:
            st.session_state.show_end_message = True

    if 'show_end_message' in st.session_state and st.session_state.show_end_message:
        st.markdown("<h2 style='text-align: center; color: #4CAF50;'>End of Facts 🎉</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Why don't you Try another store!</p>", unsafe_allow_html=True)

    if selected_store != st.session_state.get("last_selected_store", None):
        st.session_state.show_end_message = False

    st.session_state.last_selected_store = selected_store

if __name__ == "__main__":
    main()
