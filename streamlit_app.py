import streamlit as st

st.sidebar.title('Smart Farm Surveillance')
st.sidebar.subheader('Settings')

base_genre = st.sidebar.selectbox("Choose your preference",('About Smart Farm Surveillance','Livestock Monitoring','Object Detection in Farm'))

if base_genre == 'About Smart Farm Surveillance':
  	with st.container():
		st.markdown("<h1 style='text-align:center;color:black;'>Smart Farm Surveillance</h1>")
		#image = Image.open('Search-for-Lost-Cattle.jpeg')
		st.image(image)
		st.markdown('**Smart Farm Surveillance** system is an alternative to the traditional approach of farm monitoring by the use of technology-oriented agricultural techniques.\n')
		st.markdown('The main of this surveillance system is to reduce the manual effort required for security of the farm. \n')
		st.markdown('The current version of this Smart Farm Surveillance system performs the tasks of classifying the cattle & its behavior along with object detection by the use of deep learning models.\n')
