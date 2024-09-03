import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the Next Days')
location = st.text_input('Location: ')

days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of days to forecast')
if days == 1:
    suffix = ''
else:
    suffix = 's'
option = st.selectbox('Select the data to view', options=('Temperature', 'Sky'))

st.subheader(f'{option} forecast for the next {days} day{suffix} in {location.capitalize()}')

dates = ['2004-11-02', '2005-01-02', '2006-01-02']
temperatures = [10, 15, 22]
temperatures = [i * days for i in temperatures]
figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)
