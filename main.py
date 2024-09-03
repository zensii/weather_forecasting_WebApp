import streamlit as st

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
