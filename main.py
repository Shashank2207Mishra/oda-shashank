import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import seaborn as sns
dataset=st.container()
Analysis=st.container()
Header=st.container()

with dataset:
    st.title("Welcome to Olympics Analysis Project")
    data_1=pd.read_csv("athlete_events.csv")
    data_2=pd.read_csv("noc_regions.csv")
    data = pd.merge(data_1, data_2, on='NOC')
    data = data[data["Season"] == "Summer"]
    st.subheader("Dataset Used In Analysis is :")
    st.write(data)
    st.subheader("See Your favrouite Country Analysis")
    country_selectbox=st.selectbox("Enter country",data["region"].sort_values().unique())
    A = pd.get_dummies(data["Medal"])
    data = pd.concat([data, A], axis=1)
    data.drop_duplicates(["Team", "NOC", "Games", "Year", "Season", "City", "Sport", "Event", "Medal", "region"],
                         inplace=True)
    database = data.groupby("region").sum(["Gold", "Silver", "Bronze"]).sort_values(by="Gold",
                                                                                    ascending=False).reset_index()
    medal_tally = database[["region", "Bronze", "Gold", "Silver"]]
    medal_tally["total"] = medal_tally["Bronze"] + medal_tally["Gold"] + medal_tally["Silver"]
    medal_tally[medal_tally["region"]==country_selectbox]

    st.subheader("Here You Get Info about Yearwise analysis Of Olyampics ")
    select_year=st.selectbox("select Year to View",data["Year"].sort_values().unique())
    country_selectbox=st.selectbox("select Country",data["region"].sort_values().unique())
    database_year = data.groupby(["Year", "region"]).sum().reset_index()
    database_year.rename(columns={"Year": "year_1"}, inplace=True)
    database_year = database_year[["year_1", "region", "Gold", "Silver", "Bronze"]]
    database_year[(database_year["year_1"]==select_year) & (database_year["region"]==country_selectbox)]



