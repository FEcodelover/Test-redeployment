import streamlit as st
import pandas as pd

# Read the CSV in the same directory
df = pd.read_csv("secure_data.csv")
df=df[['SETTLEMENTDATE','REGIONID', 'PERIODID', 'RRP']]
st.title("My Posit Connect App")
st.write("Displaying data from the CSV:")
st.dataframe(df)
