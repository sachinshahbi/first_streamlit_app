import streamlit
import pandas

streamlit.title('My parents first healthy dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Jowari Upma')
streamlit.text('🥗Ragi Dosa')
streamlit.text('🍞Thepla')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
