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
df_corr = df.corr() # Generate correlation matrix
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


def topgenre_year(data):
    year_genre = pd.DataFrame()
    for i in range(2010,2020):
        column = df[df["top year"] == i]
        column = column.groupby('top genre')['top genre'].count().sort_values(ascending=False)
        column = column[:2]
        year_genre = year_genre.append(column)
    return year_genre
topgenre_year = topgenre_year(df)
l = [*range(2010,2020)]
topgenre_year["year"] = l
st.write('This are top Genre ')
fig = px.bar(topgenre_year, x = "year", y = ['dance pop', 'atl hip hop', 'contemporary country',
                                             'art pop', 'pop','edm', 'alt z'])
st.plotly_chart(fig)


def artist_year(data):
    year_genre = pd.DataFrame()
    for i in range(2010,2020):
        column = df[df["top year"] == i]
        column = column.groupby('artist')['artist'].count().sort_values(ascending=False)
        column = column[:2]
        year_genre = year_genre.append(column)
    return year_genre
artist_year = artist_year(df)
l = [*range(2010,2020)]
artist_year["year"] = l
st.write('This are top Artist ')
fig = px.bar(artist_year, x = "year", y = ['Rihanna', 'Kesha', 'Katy Perry', 'Calvin Harris', 'Lana Del Rey',
       'Macklemore & Ryan Lewis', 'Ariana Grande', 'Maroon 5', 'Taylor Swift',
       'The Weeknd', 'Adele', 'Kendrick Lamar', 'Lorde', 'Drake', 'Marshmello',
       'Post Malone'])
st.plotly_chart(fig)


def year_speach(data):
    speach = {}
    for i in range(2010,2020):
        dance = data[data["top year"] == i]
        value = dance["spch"].mean()
        speach[i] = value
    return speach
year_speach = year_speach(df)
st.write("Let's look at how speach as evolved in this past years")
fig = px.line( x = year_speach.keys(), y = year_speach.values())
st.plotly_chart(fig)


def year_energy(data):
    speach = {}
    for i in range(2010,2020):
        dance = data[data["top year"] == i]
        value = dance["nrgy"].mean()
        speach[i] = value
    return speach
year_energy = year_energy(df)
st.write("Let's look at how Energy of songs as evolved in this past years")
fig = px.line( x = year_energy.keys(), y = year_energy.values())
st.plotly_chart(fig)




st.header('Drawing Conclusions')
st.write("We found out that Dance Pop has been top genre in all this years")
st.write ("We found out that Taylor Swift had many songs in top year.")
st.write ("Also, among this past years, many artist had been top years.") 
st.write ("We found out that speach has been getting improved in this past years.")
st.write ("We found out that energy in the songs has been gradually decreasing")