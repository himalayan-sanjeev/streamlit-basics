import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title('Getting Started with streamlit')

# Sidebar
st.sidebar.header('Navigation')
option = st.sidebar.selectbox('Select a page:', ['Home', 'Upload Data', 'Plot Data'])


# Home Page
if option == 'Home':
    st.write('### Welcome to the Home Page')
    st.write('This is a simple web app built using Streamlit.')
    st.write('You can navigate to other pages using the sidebar.')
    st.write('To get started, select "Upload Data" from the sidebar.')
    
# Upload Data Page
if option == 'Upload Data':
    st.write('### Upload Data')
    uploaded_file = st.file_uploader('Choose a CSV file', type='csv')
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        st.write('Data uploaded successfully!')
        st.write('Navigate to "Plot Data" to visualize the data.')
        
# Plot Data Page
elif option == 'Plot Data':
    st.write('### Plot Data')
    st.code('''
    # Generate random data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)''')
    
    st.write("### Random Data Visualization")
    
    # Generate random data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)
    
    