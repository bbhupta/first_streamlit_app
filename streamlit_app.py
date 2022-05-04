import streamlit
import pandas as pd

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega 3 Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑 🍞 Avocado Toast")

streamlit.title("🍇 🥝 Build your Own Fruit Smoothie 🍌 🍍")
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit') #setting fruit as index
#Mulit-pickup list
fruit_selected = streamlit.multiselect("Pickup some fruit : ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruit_to_show = my_fruit_list.loc[fruit_selected]
streamlit.dataframe(fruit_to_show)
#streamlit.dataframe(my_fruit_list)
