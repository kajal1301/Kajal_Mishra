import streamlit as st

def main():
    st.set_page_config(page_title="Document Summarizer - Demo", layout="wide")

    st.title("Document Summarizer - Demo")
    st.markdown("""
        Welcome to the Document Summarizer application demo! This tool leverages advanced language models to process and summarize PDF documents, providing concise overviews of lengthy texts.
    """)

    # Introduction and Tools Used
    with st.expander("Introduction and Tools Used", expanded=True):
        st.write("""
            ### Introduction
            The Document Summarizer is designed to extract and summarize text from PDF files. By leveraging powerful language models and text processing techniques, it enables users to quickly obtain summaries of their documents.
        """)
        st.write("""
            ### Tools Used
            - **Python**: The primary programming language used for development.
            - **LangChain**: A framework for building applications with language models.
            - **PyMuPDF (fitz)**: A library for extracting text from PDF files.
            - **OpenAI API GPT-3**: The language model used for generating summaries.
            - **Streamlit**: The framework used for creating this interactive web application.
        """)

    # System Diagram
    with st.expander("System Architecture", expanded=True):
        st.write("""
            ### System Architecture
            The system architecture provides an overview of how the Document Summarizer processes and summarizes PDF documents. Please refer to the diagram below for a visual representation.
        """)
        st.image('Images/Document_Summarizer.png', caption='System Architecture Diagram')

    # Project Demo
    with st.expander("Project Demo", expanded=True):
        st.write("""
            ### Project Demo
            Watch the video below to see the Document Summarizer in action. The demo highlights the process of uploading a PDF document, generating a summary, and downloading the result.
        """)
        # st.warning("Please upload the demo video link (hosted on YouTube).")
        st.video('videos/Document_Summarizer.mov')

    # Additional Sections
    # st.markdown("""
    # <style>
    # .stApp {
    #     background-color: #f0f2f6;
    # }
    # .css-1v3fvcr {
    #     color: #4a90e5;
    # }
    # </style>
    # """, unsafe_allow_html=True)

    st.markdown("""
        ## Key Features
        - **PDF Text Extraction**: Extracts text content from uploaded PDF files.
        - **Document Chunking**: Splits long documents into manageable chunks for summarization.
        - **Concise Summarization**: Provides a brief overview of the document's content using advanced language models.
        - **Download Summary**: Allows users to download the generated summary as a text file.

        ## Future Enhancements
        - **Improved Summarization Accuracy**: Enhancing summarization techniques for better performance.
        - **User Interface Improvements**: Creating a more intuitive and user-friendly interface.
        - **Support for Additional Formats**: Extending support to other document formats such as DOCX or TXT.

        ## Contact Information
        For more information or to discuss potential collaborations, please contact [Kajal Mishra](https://www.linkedin.com/in/kajalmishra-1301/).
    """)

if __name__ == "__main__":
    main()
