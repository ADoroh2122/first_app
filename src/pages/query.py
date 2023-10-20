# Imports

import streamlit as st
import pandas as pd
from pathlib import Path

# Establish a filepath to the file:
folder_dir = f'{Path(__file__).parents[1]}\\data'

# Read in the csv:

d2=pd.read_csv(r"C:\Users\adoro\OneDrive\Documents\GitHub\first_app\src\data\student-por.csv", sep=";", header= None)

d2.columns = d2.iloc[0]

d2= d2.drop(index=0)

d2.columns = d2.columns.str.lower().str.strip().str.replace(' ', '_')

d2['id'] = range(1, len(d2) +1) 

# This will be the actual page:

st.header('Query Page')
st.write(
    '''
    This database will search for any student information based on the student's id.

    Please select a number between 1 and 649!
    '''
)

try:
    answer = int(st.text_input('Please select a student id:'))
    st.write(d2[d2['id'] == answer])
except:
    st.error('There was an issue with your id number. Please make sure to select a number between 1 and 649')

   



