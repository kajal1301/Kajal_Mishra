import streamlit as st

def main():
    st.set_page_config(page_title="Agents in LLM", layout="wide")
    
    st.title('Agents in LLM')
    st.subheader('Exploring AI Agents, LangGraph, and RAG')

    st.markdown("### AI Agents")
    st.write("""
        An AI agent is a software program designed to interact with its environment, gather data, and perform tasks to achieve set goals. 
        While humans set these goals, the AI agent independently determines the best actions to reach them.
        
        **Example:** In a contact center, an AI agent can resolve customer queries by asking questions, searching internal documents, 
        and providing solutions. If it can't resolve the issue, it will pass it on to a human.
    """)
    st.image('Images/Basic_Agent_architecture.jpeg', caption='Basic Agent Architecture Diagram')


    st.markdown("### Types of Agents")
    st.write("Select the agent types you're interested in to learn more:")

    agent_types = {
        'Cyclic Agents': {
            'description': """
                These agents follow a repetitive cycle of sensing the environment, processing the information, 
                and acting based on their current state and inputs.

                **Example:** A Roomba vacuum cleaner that senses dirt, moves to clean it, and repeats this process until the room is clean.
            """,
            'image': 'Images/cyclic_agents.png'
        },
        'Mixed Agents': {
            'description': """
                These agents combine features from different types of agents to leverage the strengths of each. 
                They might use reactive approaches for immediate responses and model-based approaches for planning.

                **Example:** A smart home assistant like Alexa that responds instantly to voice commands (reactive) while also scheduling 
                and planning tasks like setting reminders or controlling smart devices (model-based).
            """,
            'image': 'Images/mixed_agent.png'
        },
        'Supervisor Agents': {
            'description': """
                These agents oversee and manage other agents or systems, ensuring tasks are performed correctly and intervening when necessary.

                **Example:** In a smart home, a supervisor agent might monitor the security system, checking that all doors are locked and 
                notifying the homeowner if something unusual is detected.
            """,
            'image': 'Images/Supervisor_Agent.png'
        }
    }

    for agent, details in agent_types.items():
        with st.expander(agent):
            st.write(details['description'])
            if 'image' in details and details['image']:
                st.image(details['image'], caption=agent)

    st.markdown("### More about Agents")
    st.write("Explore additional agent types and their functionalities:")

    additional_agents = {
        'Reactive Agents': {
            'description': """
                These agents respond directly to environmental stimuli without using internal states or memory. 
                They focus on immediate decisions based on current inputs.

                **Example:** A simple obstacle-avoiding robot that changes direction when it bumps into something.
            """,
            # 'image': 'Images/Reactive_Agent.png'
        },
        'Planner Agents': {
            'description': """
                These agents use planning techniques to decide on a sequence of actions to achieve their goals. 
                They consider future states and plan accordingly.

                **Example:** A delivery robot that plans the best route to deliver packages, taking into account the layout 
                of the building and avoiding obstacles.
            """,
            # 'image': 'Images/Planner_Agent.png'
        },
        'Utility-Based Agents': {
            'description': """
                These agents use a utility function to measure the desirability of different states and aim to maximize 
                their utility to achieve the most preferred outcomes.

                **Example:** A recommendation system that suggests products to users based on their past preferences and behaviors, 
                aiming to maximize user satisfaction.
            """,
            'image': 'Images/utility_based_agents.png'
        }
    }

    for agent, details in additional_agents.items():
        with st.expander(agent):
            st.write(details['description'])
            if 'image' in details and details['image']:
                st.image(details['image'], caption=agent)

if __name__ == "__main__":
    main()
