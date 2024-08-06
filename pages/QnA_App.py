import streamlit as st

def main():
    st.set_page_config(page_title="QnA Chatbot", layout="wide")

    # Title and Introduction
    st.title("QnA Chatbot")
    st.markdown("""
        ## Welcome to the QnA Chatbot Showcase
        This chatbot leverages advanced language models to provide accurate answers to user queries based on provided text data. 
        Below, you'll find detailed information about the tools used, the system architecture, and a demo of the project.
    """)

    # Introduction and Tools Used
    with st.expander("QnA Chatbot Intro and Tools Used", expanded=True):
        st.write("""
            ### Introduction
            The QnA Chatbot is designed to answer user queries by processing input text data through a sophisticated language model.
            This project demonstrates the capabilities of modern AI in natural language understanding and generation.
        """)
        st.write("""
            ### Tools Used
            - **Python**: The primary programming language used for development.
            - **LangChain**: A framework for building applications with language models.
            - **OpenAI GPT-3**: The language model powering the chatbot's responses.
            - **Streamlit**: The framework used for creating this interactive web application.
        """)

    # System Diagram
    with st.expander("System Architecture", expanded=True):
        st.write("""
            ### System Diagram
            The system architecture provides an overview of how different components interact within the QnA Chatbot.
            Please refer to the diagram below for a visual representation.
        """)
        # st.warning("Please upload the system architecture image.")
        st.image('Images/QnA_Application.png', caption='System Architecture Diagram')

    # Project Demo
    # with st.expander("Project Demo", expanded=True):
    #     st.write("""
    #         ### Project Demo
    #         Watch the following video to see the QnA Chatbot in action. The demo highlights the chatbot's ability to understand and respond to user queries effectively.
    #     """)
    #     st.warning("Please upload the demo video link (hosted on YouTube).")
        # st.video('youtube_demo_link')

    # Additional Sections
    st.markdown("""
        ## Key Features
        - **Natural Language Understanding**: The chatbot comprehends user queries in natural language.
        - **Accurate Responses**: Leverages GPT-3 to provide precise answers based on input data.
        - **Scalable and Flexible**: Built using scalable and modular tools to adapt to various use cases.
        
        ## Future Enhancements
        - **Improved Accuracy**: Incorporating more advanced models and fine-tuning for better performance.
        - **User Interface Enhancements**: Developing a more intuitive and user-friendly interface.
        - **Integration with Other Platforms**: Expanding compatibility with different data sources and APIs.

        ## Contact Information
        For more information or to discuss potential collaborations, please contact [Your Name](https://www.linkedin.com/in/kajalmishra-1301/).
    """)

if __name__ == "__main__":
    main()
