import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Diner')



streamlit.header('🥣 Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
def get_fruitvice_data(thisfruitchoice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit of your choice")
  else:
    back_from_function = get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLerror as e:
  streamlit.error()



def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("use warehouse pc_rivery_wh")
    my_cur.execute("select * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST")
    return my_cur.fetchall()

if streamlit.button('Get the fruit load list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_row = get_fruit_load_list()
  streamlit.dataframe(my_data_row)
  

def insert_row_snowflake(fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values('from streamlit')")
    return "Thanks for adding" + new_fruit

fruit_advice = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(fruit_advice)
  streamlit.text(back_from_function)
  

