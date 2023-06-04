import streamlit as st
import requests
import pandas as pd

def fetch_astronauts():
    res = requests.get('http://api.open-notify.org/astros.json')
    data = res.json()
    return data

def fetch_iss_location():
    res = requests.get('http://api.open-notify.org/iss-now.json')
    data = res.json()
    return data

def main():
    st.title("People in Space")

    st.markdown("An application to show the current number of people in space and their names.")

    data = fetch_astronauts()
    total_astronauts = data["number"]
    astronauts = data["people"]

    st.write(f"There are currently {total_astronauts} people in space.")

    for i, astronaut in enumerate(astronauts, start=1):
        st.markdown(f"{i}. **{astronaut['name']}** is currently on {astronaut['craft']}.")

    st.markdown("## Current Location of the International Space Station")

    iss_data = fetch_iss_location()
    iss_location = iss_data['iss_position']
    iss_df = pd.DataFrame([iss_location])
    iss_df['latitude'] = pd.to_numeric(iss_df['latitude'])
    iss_df['longitude'] = pd.to_numeric(iss_df['longitude'])

    st.map(iss_df)

    st.markdown("The map above shows the current location of the International Space Station.")

if __name__ == "__main__":
    main()
