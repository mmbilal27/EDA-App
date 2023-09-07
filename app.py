import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# Create a Streamlit sidebar for navigation
st.sidebar.title("EDA App")

# Upload a file
uploaded_file = st.sidebar.file_uploader("Upload a file", type=["csv", "xlsx", "txt"])

if uploaded_file is not None:
    # Load the data
    df = pd.read_csv(uploaded_file)  # You can handle other file types similarly

    # Display the first 5 rows
    st.subheader("Data Preview")
    st.write(df.head())

    # Summary statistics
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Visualizations
    st.subheader("Visualizations")

    # Histogram
    selected_column_hist = st.selectbox("Select a column for Histogram", df.columns)
    plt.figure(figsize=(8, 6))
    sns.histplot(df[selected_column_hist], bins=20, kde=True)
    st.pyplot()

    # Box plot
    selected_column_boxplot = st.selectbox("Select a column for Box Plot", df.columns)
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, y=selected_column_boxplot)
    st.pyplot()

    # Correlation heatmap
    st.subheader("Correlation Heatmap")
    corr_matrix = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=.5)
    st.pyplot()

    # Missing data
    st.subheader("Missing Data")
    st.write(df.isnull().sum())

    # Feature engineering (example: extracting year from date)
    if "date_column" in df.columns:
        df['year'] = pd.to_datetime(df['date_column']).dt.year
        st.subheader("Feature Engineering")
        st.write(df.head())

    # Download modified dataset
    st.subheader("Download Modified Dataset")
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="modified_data.csv">Download CSV</a>'
    st.markdown(href, unsafe_allow_html=True)
