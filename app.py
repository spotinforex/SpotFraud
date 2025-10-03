import streamlit as st
import pandas as pd
from src.model_prediction import Prediction

st.set_page_config(page_title = 'Fraud Detection App', layout = 'wide')
st.title( "Spot Fraud Detection App")


st.subheader(" Batch Prediction For CSV")
uploaded_file = st.file_uploader( ' Upload Your CSV File', type = ['csv'])

if uploaded_file is not None:
    raw_df = pd.read_csv(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(" Data Preview")
        st.dataframe(raw_df.head())

    with col2:
        st.markdown(" Number Of Missing Data")
        data_null = raw_df.isnull().sum()
        st.dataframe(data_null)

    if st.button( " Run Prediction"):
        st.subheader(" Prediction Results")
        with st.spinner( "Running Inference"):
            try:
                model_path = 'models\model_V1.pkl'
                pred = Prediction(raw_df, model_path)
                raw_df['Prediction'] = pred

                st.success("Prediction Complete")
                st.dataframe(raw_df.head(10))
                st.download_button(' Download Predictions',
                  raw_df.to_csv(index = False),
                  'Fraud Prediction CSV')
            except Exception as e:
                st.error(f'Error Occurred During Prediction {e}')





