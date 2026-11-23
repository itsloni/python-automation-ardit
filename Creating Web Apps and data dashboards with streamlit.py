import streamlit as st
import pandas

data = {
    "series_1" : [1, 2, 3, 4, 90],
    "series_2" : [20, 30, 10, 70, 89]
}
df = pandas.DataFrame(data)

st.title("My First Streamlit App")
st.subheader("Introducing Streamlit in Automate Everything with Python")
st.write("""This is my First Web App.
Enjoy it!
""")
st.write(df)
st.line_chart(df)