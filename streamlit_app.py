#https://github.com/streamlit/app-starter-kit
import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

with st.sidebar:
    st.header("About Data")
    st.write("This data contains 3 tables: movies, rating, and tags")

st.title("IMDB Data Analysis")

# Slider for selecting number of records
x = st.slider("Choose the number of records to be displayed: ", min_value=1, max_value=20)

#movies table
st.header("Movies table data")
df_movies = pd.read_csv("movie.csv")
st.table(df_movies.head(x))

#tags table
st.header("Tags table data")
df_tags = pd.read_csv("tag.csv")

# Convert timestamp column to datetime format and extract components
df_tags['timestamp'] = pd.to_datetime(df_tags['timestamp'])
df_tags['Year'] = df_tags['timestamp'].dt.year
df_tags['Month'] = df_tags['timestamp'].dt.month
df_tags['Day'] = df_tags['timestamp'].dt.day
df_tags['Hour'] = df_tags['timestamp'].dt.hour
df_tags['Minute'] = df_tags['timestamp'].dt.minute
df_tags['Second'] = df_tags['timestamp'].dt.second
st.table(df_tags.head(x))

# #rating table
# st.header("Ratings table data")
# df_rating = pd.read_csv(r"C:\Users\91837\Downloads\archive\rating.csv")
# st.table(df_rating.head(x))

# # Plot Histogram for Ratings
# st.subheader("Histogram of Ratings")
# fig, ax = plt.subplots()
# ax.hist(df_rating['rating'])
# ax.set_xlabel("Ratings")
# ax.set_ylabel("Frequency")
# ax.set_title("Distribution of Ratings")
# st.pyplot(fig)

