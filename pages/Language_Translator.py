import streamlit as st

def main():
    st.set_page_config(page_title="Language Translator", layout="wide")

    # Title and Introduction
    st.title("Language Translator")
    st.markdown("""
        ## Welcome to the Language Translator App
        Translate text between different languages using advanced AI language models.
        Below, you can specify the source language, target language, and the text you want to translate.
    """)

    # Introduction and Tools Used
    with st.expander("Language Translator App Overview", expanded=True):
        st.write("""
            ### Introduction
            The Language Translator App uses state-of-the-art AI models to provide accurate translations 
            between various languages. It demonstrates the power of AI in facilitating communication 
            across different linguistic contexts.
        """)
        st.write("""
            ### Tools Used
            - **Python**: The programming language used for development.
            - **OpenAI GPT-3**: Utilized for translating text between languages.
            - **Streamlit**: The framework used for building this interactive web application.
            - **Other Tools**: Add any other relevant tools or libraries used in your project.
        """)

    # System Diagram (Placeholder)
    with st.expander("System Architecture", expanded=True):
        st.write("""
            ### System Diagram
            The system architecture provides an overview of how different components interact within the Language Translator App.
            Please refer to the diagram below for a visual representation.
        """)
        # st.warning("Please upload the system architecture image.")
        st.image('Images/Language Translator.png', caption='System Architecture Diagram')

    # Additional Sections
    st.markdown("""
        ## Key Features
        - **Multilingual Support**: Translate text between a variety of languages.
        - **AI-Powered Translation**: Uses advanced AI models for accurate and context-aware translations.
        - **User-Friendly Interface**: Simple and intuitive design for ease of use.
        
        ## Future Enhancements
        - **Enhanced Language Support**: Adding more languages for translation.
        - **Real-Time Translation**: Implementing real-time translation capabilities.
        - **Integration with APIs**: Connecting with external translation APIs for extended functionality.

       ## Contact Information
        For more information or to discuss potential collaborations, please contact [Kajal Mishra](https://www.linkedin.com/in/kajalmishra-1301/).
    """)

if __name__ == "__main__":
    main()
