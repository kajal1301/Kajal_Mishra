import streamlit as st

def main():
    st.set_page_config(page_title="Chatbot - VIRTUAL ASSISTANT", layout="wide")

    # Title and Introduction
    st.title("Chatbot - VIRTUAL ASSISTANT")
    st.markdown("""
        ## Welcome to the Virtual Assistant Chatbot Showcase
        This virtual assistant leverages advanced language models to provide accurate answers to user queries and assist with various tasks. 
        Below, you'll find detailed information about the tools used, the system architecture, and a demo of the project.
    """)

    # Introduction and Tools Used
    with st.expander("Virtual Assistant Chatbot Intro and Tools Used", expanded=True):
        st.write("""
            ### Introduction
            The Virtual Assistant Chatbot is designed to assist users by processing input text data through a sophisticated language model.
            This project demonstrates the capabilities of modern AI in natural language understanding and generation, making interactions seamless and efficient.
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
            The system architecture provides an overview of how different components interact within the Virtual Assistant Chatbot.
            Please refer to the diagram below for a visual representation.
        """)
        st.image('Images/chatbot.png', caption='System Architecture Diagram')

    # Project Demo
    with st.expander("Project Demo", expanded=True):
        st.write("""
            ### Project Demo
            Watch the following video to see the Virtual Assistant Chatbot in action. The demo highlights the chatbot's ability to understand and respond to user queries effectively.
        """)
        # st.warning("Please upload the demo video link (hosted on YouTube).")
        st.video('videos/chatbot.mov')

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
        - **Natural Language Understanding**: The chatbot comprehends user queries in natural language.
        - **Accurate Responses**: Leverages GPT-3 to provide precise answers based on input data.
        - **Task Assistance**: Helps users with various tasks such as setting reminders, providing information, and more.
        - **Scalable and Flexible**: Built using scalable and modular tools to adapt to various use cases.
        
        
        ## Contact Information
        For more information or to discuss potential collaborations, please contact [Kajal Mishra](https://www.linkedin.com/in/kajalmishra-1301/).
    """)

if __name__ == "__main__":
    main()


## Future Enhancements
        # - **Improved Accuracy**: Incorporating more advanced models and fine-tuning for better performance.
        # - **User Interface Enhancements**: Developing a more intuitive and user-friendly interface.
        # - **Integration with Other Platforms**: Expanding compatibility with different data sources and APIs.
