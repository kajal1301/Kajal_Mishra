import streamlit as st

def main():
    st.set_page_config(page_title="Retrieval-Augmented Generation (RAG)", layout="wide")
    
    st.title('Retrieval-Augmented Generation (RAG)')
    st.subheader('Combining Retrieval and Generation in AI')

    st.markdown("### What is RAG?")
    st.write("""
        Retrieval-Augmented Generation (RAG) is an approach that combines the strengths of retrieval-based systems and 
        generation-based systems. It leverages large external datasets to retrieve relevant information and then generates 
        responses or content based on that retrieved information.
        
        This approach enhances the capabilities of AI models, making them more accurate and contextually aware.
    """)

    st.markdown("### Key Components of RAG")

    rag_components = {
        'Retrieval Component': {
            'description': """
                The retrieval component is responsible for searching and retrieving relevant documents or pieces of information from a large corpus. 
                It ensures that the AI model has access to the most pertinent data.

                **Example:** In a question-answering system, the retrieval component finds relevant paragraphs from a vast database 
                to help answer the user's question.
            """,
            'image': 'Images/RAG_indexing.png'
        },
        'Generation Component': {
            'description': """
                The generation component takes the retrieved information and uses it to generate a coherent and contextually appropriate response. 
                This is typically handled by a neural network, such as a transformer model.

                **Example:** After retrieving relevant information about a historical event, the generation component composes a detailed 
                and accurate answer to a user's query about that event.
            """,
            'image': 'Images/RAG_generation.png'
        },
        'Combining Retrieval and Generation': {
            'description': """
                RAG effectively combines the retrieval and generation components, allowing the AI to generate responses based on real-time 
                retrieved data. This synergy improves both the relevance and accuracy of the responses.

                **Example:** A customer service chatbot uses RAG to retrieve the latest policy documents and generate answers to customer questions, 
                ensuring that the information provided is both up-to-date and accurate.
            """,
            'image': 'Images/RAG_Combined.png'
            
        }
    }

    for component, details in rag_components.items():
        with st.expander(component):
            st.write(details['description'])
            if 'image' in details and details['image']:
                st.image(details['image'], caption=component)

    st.markdown("### Benefits of RAG")
    st.write("Explore the advantages of using RAG in AI applications:")

    rag_benefits = {
        'Improved Accuracy': {
            'description': """
                By leveraging up-to-date and relevant information from large datasets, RAG can provide more accurate and reliable responses.

                **Example:** A medical diagnosis system using RAG can retrieve the latest research papers and clinical guidelines to assist doctors in making accurate diagnoses.
            """,
            # 'image': 'Images/RAG_accuracy.png'
        },
        'Enhanced Contextual Awareness': {
            'description': """
                RAG models have a better understanding of context due to the combination of retrieval and generation, resulting in more contextually appropriate responses.

                **Example:** A legal advice chatbot can understand and generate responses based on specific legal contexts, providing more precise advice.
            """,
            # 'image': 'Images/RAG_contextual.png'
        },
        'Scalability': {
            'description': """
                RAG systems can scale effectively by expanding the retrieval corpus, making it possible to handle a wide range of topics and queries.

                **Example:** An educational platform can use RAG to provide detailed answers across various subjects by continuously expanding its knowledge base.
            """,
            # 'image': 'Images/RAG_scalability.png'
        }
    }

    for benefit, details in rag_benefits.items():
        with st.expander(benefit):
            st.write(details['description'])
            # st.image(details['image'], caption=benefit)

if __name__ == "__main__":
    main()
