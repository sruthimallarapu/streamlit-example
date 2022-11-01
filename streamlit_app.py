import streamlit as st

st.sidebar.title('Smart Farm Surveillance System')

base_genre = st.sidebar.selectbox("Choose your preference",('About Smart Farm Surveillance System', 'Livestock Detection and Tracking', 'Intruder Detection and Tracking', 'Vehicle Detection and Tracking'))

if base_genre == 'About Smart Farm Surveillance System':
	with st.container():
		st.markdown("<h1 style='text-align: center; color: black;'>Smart Farm Surveillance System</h1>", unsafe_allow_html=True")
		#image = Image.open('Search-for-Lost-Cattle.jpeg')
		#st.image(image)
		st.markdown('**Smart Farm Surveillance** system is an alternative to the traditional approach of farm monitoring by the use of technology-oriented agricultural techniques.\n')
		st.markdown('The main of this surveillance system is to reduce the manual effort required for security of the farm. \n')
		st.markdown('The current version of this Smart Farm Surveillance system performs the tasks of classifying the cattle & its behavior along with object detection by the use of deep learning models.\n')
		
elif base_genre == 'Livestock Detection and Tracking':
	with st.container():
		st.markdown("# Livestock Detection and Tracking")
		st.markdown(''' Here the type of cattle is identified using the drone video of cattle grazing on the farmland. Cattles like cow, sheep and horse are identified.
			            The basic positional behavior of cattles like standing, eating and idle states are  captured.
			            Along with the mentioned classification, the cattles are counted and their movement is also tracked.
			            The output classification video display either all the cattle types or the cattle type given by the user.
                    ''')
		genre = st.sidebar.radio('Choose the livestock classification type',('Species Classification','Behavior Classification'))
		
		if genre == 'Species Classification':
			st.markdown("<h3 style='text-align: center; color: black;'>Species Classification</h3>", unsafe_allow_html=True)
			names = ['All','Cow','Sheep','Horse']
			assigned_class = st.sidebar.radio("Choose the cattle to be identified:", names)
			st.sidebar.markdown('---')
			uploaded_files = st.sidebar.file_uploader("Upload the drone video of farm", type=[ "mp4", "mov",'avi','asf', 'm4v' ], accept_multiple_files=False)
		else:
			st.markdown("<h3 style='text-align: center; color: black;'>Behavior Classification</h3>", unsafe_allow_html=True)
			names = ['All','Sit','Stand','Sleep']
			assigned_class = st.sidebar.radio("Choose the behavior type to be identified:", names)
			st.sidebar.markdown('---')
			uploaded_files = st.sidebar.file_uploader("Upload the drone video of farm", type=[ "mp4", "mov",'avi','asf', 'm4v' ], accept_multiple_files=False)
