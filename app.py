import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Page Title
st.set_page_config(page_title="Streamlit CSV Visualizer", layout="wide")

# Sidebar Navigation
st.sidebar.header("Navigation")
option = st.sidebar.radio("Go to:", ["Home", "About", "Upload Data", "Visualization"])

# Global Variable for Uploaded Data
if "data" not in st.session_state:
    st.session_state.data = None

# Home Page
if option == "Home":
    st.title("Getting Started with Streamlit")
    st.write("""
    ### Welcome to the CSV Visualizer App!
    
    This is a simple web application on getting started with Streamlit that allows you to:
    - **Upload CSV files** 
    - **Preview data** in tabular format 
    - **Generate various visualizations** based on uploaded data
    
    #### How to Use?
    1. Navigate to **Upload Data** to add a CSV file.
    2. Go to **Visualization** to generate different plots dynamically.
    3. Use the sidebar to switch between pages.
    """)

# About Page
elif option == "About":
    st.title("About")
    st.write("""
    ### About This App
    This is a sample streamlit web application for uploading CSV files and visualizing data interactively.  
    Features:
    - Upload CSV files
    - Preview uploaded data
    - Generate custom **line charts, bar plots, scatter plots, and histograms**
    - Select **any numeric column** for plotting
    """)

# Upload Data Page
elif option == "Upload Data":
    st.title("Upload CSV File")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the uploaded CSV
        df = pd.read_csv(uploaded_file)
        st.session_state.data = df  # Store in session state
        
        # Show preview of uploaded data
        st.write("### Data Preview")
        st.dataframe(df.head())  # Show first 5 rows
        st.success("Data uploaded successfully! Navigate to 'Visualization' to explore.")

# Visualization Page
elif option == "Visualization":
    st.title("Data Visualization")
    
    # Check if data is available
    if st.session_state.data is None:
        st.warning("No data available. Please upload a CSV file first.")
    else:
        df = st.session_state.data
        
        # Get numeric columns
        numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
        
        if len(numeric_columns) < 2:
            st.warning("The dataset must contain at least two numeric columns to generate meaningful plots.")
        else:
            # Choose plot type
            plot_type = st.selectbox("Choose Plot Type:", ["Line Chart", "Bar Chart", "Scatter Plot", "Histogram"])
            
            # Select X and Y axis
            x_axis = st.selectbox("Select X-axis:", numeric_columns)
            y_axis = st.selectbox("Select Y-axis:", numeric_columns)
            
            # Generate plots
            fig, ax = plt.subplots()
            
            if plot_type == "Line Chart":
                ax.plot(df[x_axis], df[y_axis], marker='o', linestyle='-')
                ax.set_title(f"Line Chart: {y_axis} vs {x_axis}")
            
            elif plot_type == "Bar Chart":
                ax.bar(df[x_axis], df[y_axis], color='skyblue')
                ax.set_title(f"Bar Chart: {y_axis} vs {x_axis}")
            
            elif plot_type == "Scatter Plot":
                ax.scatter(df[x_axis], df[y_axis], color='red')
                ax.set_title(f"Scatter Plot: {y_axis} vs {x_axis}")
            
            elif plot_type == "Histogram":
                ax.hist(df[y_axis], bins=20, color='purple', alpha=0.7)
                ax.set_title(f"Histogram: {y_axis}")
            
            # Labels
            ax.set_xlabel(x_axis)
            ax.set_ylabel(y_axis)
            
            # Display the plot
            st.pyplot(fig)
