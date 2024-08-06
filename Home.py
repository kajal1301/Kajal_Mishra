import streamlit as st
import fitz  

from pages import (
    RAG as RAG,
    Agents as Agents,
    Chatbot as ChatBot,
    Document_Summarizer as Document_Summarizer,
    Language_Translator as Language_Translator,
    QnA_App as QnA_APP,
    Resume_Reviwer as Resume_Reviewer
)

# Create a dictionary to hold page names and corresponding module imports
pages = {
    "Page 1": Agents,
    "Page 2": RAG,
    "Page 3": ChatBot,
    "Page 4": Resume_Reviewer,
    "Page 5": Document_Summarizer,
    "Page 6": Language_Translator,
    "Page 7": QnA_APP,
}


def display_pdf_as_images(pdf_path):
    document = fitz.open(pdf_path)
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        pix = page.get_pixmap()
        img = pix.tobytes("png")
        st.image(img, caption=f"Page {page_num + 1}", use_column_width=True)


def main():
    st.title('Hi! I am Kajal Mishra')

    st.header('Welcome to the my Portfolio')
    # Adding personal details
    st.subheader('About Me')
    st.write('''I am a passionate Data Scientist and AI enthusiast with a strong background in developing and deploying AI solutions.
             I have 3 years experience in various Generative AI projects, including language translation, QnA applications, chatbots, 
             resume reviewing, and marketing summarization. My goal is to leverage AI to solve real-world problems and drive 
             innovation in various domains.''')
    
    st.subheader('Contact Information')
    st.write('''
        - **Email:** kajal123m@gmail.com
        - **LinkedIn:** [linkedin.com/in/kajalmishra](https://www.linkedin.com/in/kajalmishra-1301/)
        - **GitHub:** [github.com/kajalmishra](https://github.com/kajal1301)
    ''')

    # Adding resume section
    st.subheader('Resume')
    resume_path = "PDF Docs/KajalMishra_Resume.pdf"
    display_pdf_as_images(resume_path)

 
  

if __name__ == "__main__":
    main()
