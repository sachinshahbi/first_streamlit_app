import streamlit
import pandas

streamlit.title('My parents first healthy dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣Jowari Upma')
streamlit.text('🥗Ragi Dosa')
streamlit.text('🍞Thepla')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.

streamlit.dataframe(my_fruit_list)
