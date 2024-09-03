import streamlit as st
import plotly.express as px
import backend

data = []

st.title('Weather Forecast for the Next Days')

location = st.text_input('Location:')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of days to forecast')
if days == 1:
    suffix = ''
else:
    suffix = 's'
option = st.selectbox('Select the data to view', options=('Temperature', 'Sky'))

st.subheader(f'{option} forecast for the next {days} day{suffix} in {location.capitalize()}')

if location:
    lat, lon = backend.get_location(location)
    data = backend.get_data(lat, lon, days)

    dates = []
    temperatures = []
    for item in data['list']:
        dates.append(item['dt_txt'])
        temperatures.append(f'{item['main']['temp']}')

    if option == 'Temperature':
        figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
        st.plotly_chart(figure)
    if option == 'Sky':
        pass

