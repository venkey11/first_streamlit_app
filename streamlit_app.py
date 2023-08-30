import streamlit as sm
import pandas as pd

sm.title('This is our new webpage using snowflake - the journey of two analysts becoming data engineers and a nice cook')

sm.header('How to become a data engineer')
sm.text('Finish snowflake badges')
sm.text('Data Factory')
sm.text('Databricks')
sm.text('Finish Certifications of the above')

#Breakfast cooking time
sm.header('This is cooking session - Time to cook!')
sm.text('🥗 Omega 3 & Blueberry Oatmeal')
sm.text('🥑 Kale, Spinach & Rocket Smoothie')
sm.text('🐔🍞 Hard-Boiled Free-Range Egg')

#import using pandas
fruits_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')

#setting up a pick list
fruits = fruits_list.set_index('Fruit')
sm.multiselect('Pick up the fruits you like',list(fruits.index))

sm.dataframe(fruits_list)

          
