import streamlit as st
import pandas as pd
import PyPDF2
import io

# Set page config
st.set_page_config(page_title="Data Sweeper App", layout="wide")

# Add custom CSS
st.markdown("""
    <style>
        .stButton>button {
            width: 100%;
        }
        .main {
            padding: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("📊 Data Sweeper App")
st.markdown("---")

# File type selection
file_type = st.radio("Select file type:", ["CSV", "PDF"])

if file_type == "CSV":
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        try:
            # Read the CSV file
            df = pd.read_csv(uploaded_file)
            
            # Display the original data
            st.subheader("📋 Original Data")
            st.dataframe(df, use_container_width=True)

            # Sidebar for cleaning options
            with st.sidebar:
                st.subheader("🛠️ Cleaning Options")
                
                # Option to remove duplicates
                if st.checkbox("Remove Duplicates"):
                    df = df.drop_duplicates()
                    st.success("✅ Duplicates removed!")

                # Option to handle missing values
                if st.checkbox("Handle Missing Values"):
                    missing_option = st.selectbox(
                        "Select an option", 
                        ["Drop Rows", "Fill with Mean", "Fill with Median"]
                    )
                    if missing_option == "Drop Rows":
                        df = df.dropna()
                        st.success("✅ Rows with missing values dropped!")
                    elif missing_option == "Fill with Mean":
                        df.fillna(df.mean(numeric_only=True), inplace=True)
                        st.success("✅ Missing values filled with mean!")
                    elif missing_option == "Fill with Median":
                        df.fillna(df.median(numeric_only=True), inplace=True)
                        st.success("✅ Missing values filled with median!")

            # Display the cleaned data
            st.subheader("✨ Cleaned Data")
            st.dataframe(df, use_container_width=True)

            # Option to download the cleaned data
            csv = df.to_csv(index=False)
            st.download_button(
                "📥 Download Cleaned Data",
                csv,
                "cleaned_data.csv",
                "text/csv",
                key='download-csv'
            )
            
        except Exception as e:
            st.error(f"Error processing CSV file: {str(e)}")

else:  # PDF handling
    uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        try:
            # Read PDF file
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            
            # Extract text from all pages
            text_content = ""
            for page in pdf_reader.pages:
                text_content += page.extract_text()

            # Display the extracted text
            st.subheader("📄 Extracted Text from PDF")
            st.text_area("Content", text_content, height=300)

            # Option to download the extracted text
            st.download_button(
                "📥 Download Extracted Text",
                text_content,
                "extracted_text.txt",
                "text/plain",
                key='download-text'
            )

        except Exception as e:
            st.error(f"Error processing PDF file: {str(e)}")

# Add footer
st.markdown("---")
st.markdown("### 📌 Instructions")
st.markdown("""
- For CSV files: Upload your data and use the sidebar options to clean it
- For PDF files: Upload your PDF to extract and download the text content
""")