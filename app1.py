import pandas as pd
import numpy as np
import plotly.express as px
import plotly.figure_factory as ff
import warnings 
import streamlit as st
warnings.filterwarnings("ignore") 

st.title('Data Science Spotify 2010-2019 EDA')
st.header('Target')
st.write('The target of this EDA is to draw conclusions about the viability of certain positions within the realm of Data Science based on numerous features . This will be done through the use of comprehensive charts, tables, and maps that will paint an overall picture of the given dataset.')
# Data Exploration

df = pd.read_csv('Spotify 2010 - 2019 Top 100.csv')
st.write(df.head(10))

st.header('List of Features')
st.write(df.columns)

colnames = list(df.columns)

st.header('Value Counts For Each Feature')
for i in colnames:
    st.write(df[i].value_counts())

st.header('Data Cleaning')
st.write('Here, upon reviewing the value counts and determining how valuable certain features would be compared to others, it was decided that artist type, and year released would be dropped. Artist type didnt quite matter as compare to artist, and year released is mostly same as top year')

df = df.dropna(axis=0).reset_index(drop=True)


st.header('Exploring Correlation')
numeric_columns = df.select_dtypes(include=np.number).columns
df_corr = df[numeric_columns].corr()
x = list(df_corr.columns)
y = list(df_corr.index)
z = np.array(df_corr)

fig = ff.create_annotated_heatmap(
    z,
    x = x,
    y = y ,
    annotation_text = np.around(z, decimals=2),
    hoverinfo='z',
    colorscale='Brwnyl',
    showscale=True,
    )
fig.update_xaxes(side="bottom")
fig.update_layout(
    # title_text='Heatmap', 
    title_x=0.5, 
    width=500, 
    height=500,
    yaxis_autorange='reversed',
    template='plotly_white'
)
st.write(' ')
st.write('Correlation Heatmap')
st.plotly_chart(fig)


