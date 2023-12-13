import streamlit as st
import random
import time

st.title("Job searching chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Job-related questions and answers
        job_questions = [
            "i want job",
            "Tell me about your skills and experience.",
            "What kind of job are you looking for?",
            "Have you prepared a resume?",
            "Are you open to relocation?",
            "How do you handle job interviews?",
            "Do you have any specific industries in mind?",
        ]
        
        job_responses = [
            "Enter your job description"
            "It's important to highlight your skills and experience on your resume.",
            "Consider specifying the type of job you are interested in to narrow down your search.",
            "Having a well-prepared resume is crucial for job applications.",
            "Being open to relocation can broaden your job opportunities.",
            "Prepare for job interviews by practicing common questions and researching the company.",
            "Certain industries may have specific requirements; make sure to tailor your applications accordingly.",
        ]

        # Check if the user's input matches a job-related question
        matched_question = None
        for question in job_questions:
            if question.lower() in prompt.lower():
                matched_question = question
                break

        # If a match is found, respond with the corresponding answer
        if matched_question:
            index = job_questions.index(matched_question)
            assistant_response = job_responses[index]
        else:
            # If no match, provide a generic response
            assistant_response = random.choice(
                [
                    "Hello there! How can I assist you today?",
                    "Hi, human! Is there anything I can help you with?",
                    "Do you need help?",
                ]
            )

        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
