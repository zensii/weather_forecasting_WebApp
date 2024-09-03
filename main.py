import streamlit as st
import plotly.express as px
from backend import get_data, get_location

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
    try:
        lat, lon = get_location(location)
        data = get_data(lat, lon, days)

        if option == 'Temperature':
            dates = []
            temperatures = []
            for item in data['list']:
                dates.append(item['dt_txt'])
                temperatures.append(f'{item['main']['temp']}')

            figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
            st.plotly_chart(figure)

        if option == 'Sky':
            dates = []
            conds = []
            img_paths_list = []

            for item in data['list']:
                dates.append(item['dt_txt'])
                conds.append(f'{item['weather'][0]['main']}')

                img_paths_list = [f'images\\{cond.lower()}.png' for cond in conds]
            st.image(img_paths_list, width=115, caption=dates)

    except IndexError:
        st.warning('The selected location is not found')
