import streamlit as st
import pandas as pd
import sqlite3

st.title('Clinical Trails Dashboard')

conn = sqlite3.connect('clinicaltrials.db')
df = pd.read_sql('SELECT * FROM trials', conn)
conn.close()

st.write('Total trials in database:', len(df))
status_filter = st.selectbox('Filter by status', ['All'] + list(df['status'].unique()))

if status_filter != 'All':
    df = df[df['status'] == status_filter]

num_results = st.slider('Number of trials to show', 5, len(df), 10)
df = df.head(num_results)
st.write('Showing', len(df), 'trials')
status_counts = df['status'].value_counts()
st.bar_chart(status_counts)
st.dataframe(df)
