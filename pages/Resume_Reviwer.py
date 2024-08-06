import streamlit as st

def main():
    st.set_page_config(page_title="Resume Review Analysis", layout="wide")

    # Title and Introduction
    st.title("Resume Review Analysis")
    st.markdown("""
        ## Welcome to the Resume Review Analysis Showcase
        This application analyzes how well a resume matches a given job description and provides recommendations to improve the resume's alignment with the job requirements.
    """)

    # Introduction and Tools Used
    with st.expander("Resume Review Analysis Intro and Tools Used", expanded=True):
        st.write("""
            ### Introduction
            The Resume Review Analysis tool helps job seekers optimize their resumes to better match job descriptions. It leverages advanced language models to analyze and compare the content of resumes and job descriptions.
        """)
        st.write("""
            ### Tools Used
            - **Python**: The primary programming language used for development.
            - **PyPDF2**: A library for reading PDF files.
            - **Streamlit**: The framework used for creating this interactive web application.
        """)

        
    # System Diagram (Placeholder)
    with st.expander("System Architecture", expanded=True):
        st.write("""
            ### System Diagram
            The system architecture provides an overview of how different components interact within the Language Translator App.
            Please refer to the diagram below for a visual representation.
        """)
        # st.warning("Please upload the system architecture image.")
        st.image('Images/Resume_review.png', caption='System Architecture Diagram')

    # Project Demo
    with st.expander("Project Demo", expanded=True):
        st.write("""
            ### Project Demo
            Watch the following video to see the Resume Analyser in action. The demo highlights how the Resume Analyser analyses the Job Description and Matches the Resume with it.This tells about the strengths and weakness of Resume and the Recommendations to add in the Resume to make it a perfect match with JD Provided.
        """)
        # st.warning("Please upload the demo video link (hosted on YouTube).")
        st.video('videos/Resume_Review.mov')



    # Additional Sections
    st.markdown("""
        ## Key Features
        - **Resume Analysis**: Compares resume content with job descriptions to determine match percentage.
        - **Recommendations**: Provides actionable suggestions to improve resume alignment with job requirements.
        
        ## Future Enhancements
        - **Improved Analysis**: Integrating more sophisticated models for deeper analysis.
        - **Expanded File Support**: Supporting additional file formats and larger documents.
        - **User Interface Enhancements**: Developing a more intuitive and user-friendly interface.

        ## Contact Information
        For more information or to discuss potential collaborations, please contact [Kajal Mishra](https://www.linkedin.com/in/kajalmishra-1301/).
    """)

if __name__ == "__main__":
    main()