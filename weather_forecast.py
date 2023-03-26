import streamlit as st
import plotly.express as px
from load_data import data


st.title("5-DAY WEATHER FORECAST 🌥 🌦")
city = st.text_input("ENTER THE CITY NAME: ","London", placeholder="City Name")
days = st.select_slider(
    "Forecast Days",
    options=[1, 2, 3, 4, 5] )
kind = st.selectbox("Select Data to view", ("Temperature", "Sky"))
submit_button = st.button("Submit")
st.header(f"Temperature for the next {days} days in {city}")
try:
    filtered_data = data(city, days)

    if submit_button:
        print("clicked")
        if kind == "Temperature":
            temperature = [ round(dict["main"]["temp"] / 10 ) for dict in filtered_data]
            dates = [ date["dt_txt"] for date in filtered_data]
            figure = px.line(x = dates, y=temperature,
                             labels=({"x": "Dates", "y": "Temperature (C)"}))
            st.plotly_chart(figure)
        if kind == "Sky":
            images = {
                "Clouds" : "images/cloud.png",
                "Rain" : "images/rain.png",
                "Clear" : "images/clear.png",
                "Snow" : "images/snow.png",
            }
            weather = [ dict["weather"][0]["main"] for dict in filtered_data]
            img = [ images[sky] for sky in weather]
            st.image(img, width=110)
except KeyError:
    st.warning("Invalid City. Please Try again")
