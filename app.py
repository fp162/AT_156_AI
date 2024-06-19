import streamlit as st
import pandas as pd
import plotly.express as px

st.title('AT-AI')
st.write('Welcome to the AT-AI Streamlit app!')

# File upload
uploaded_file = st.file_uploader("Upload a CSV or XLSX file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Read file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    
    # Show preview of data
    st.write("Preview of the data:")
    st.write(df.head())
    
    # Ensure the first column is datetime
    df[df.columns[0]] = pd.to_datetime(df[df.columns[0]])
    df.set_index(df.columns[0], inplace=True)
    
    # Select features to plot
    features = st.multiselect("Select features to plot", df.columns.tolist(), default=df.columns.tolist())
    
    # Select date range
    min_date = df.index.min().date()
    max_date = df.index.max().date()
    start_date = st.date_input("From date", min_date)
    end_date = st.date_input("To date", max_date)
    
    # Filter data based on date range
    mask = (df.index.date >= start_date) & (df.index.date <= end_date)
    filtered_data = df.loc[mask]
    
    # Plot data
    if features:
        st.write("Line plot of selected features:")
        fig = px.line(filtered_data, y=features, title='Selected Features Over Time')
        st.plotly_chart(fig)
