import streamlit as st
from serpapi import GoogleSearch
import random
import time

st.title("Job searching chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize user's job description variable
job_description = ""

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to perform SerpApi job search
def serpapi_search(query):
    search_params = {
        "q": query + " jobs",
        "api_key": "6a7365d23d76833f732d2f4b393f2ef84ac825f754bd7115d1503e32f69a4788"  
    }
    search = GoogleSearch(search_params)
    result = search.get_dict()
    return result.get("organic_results", [])

# Function to display job search results in a collapsible section
def display_serpapi_jobs(serpapi_results):
    for index, result in enumerate(serpapi_results, start=1):
        title = result.get('title', '')
        company = result.get('snippet', '')
        link = result.get('link', '')

        # Create a collapsible section for each job result
        with st.expander(f"Job {index} - {title}"):
            # Add content inside the expander
            st.write(f"Company: {company}")
            st.write(f"Link: {link}")

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
        
        ]

        job_responses = [
            "Enter your job descrpition",
            
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

            # Check if the assistant is asking for a job description
            if "Your job details" in assistant_response:
                # Store user's input in the job_description variable
                job_description = prompt

                # Now you can use the job_description variable for your API call
                # For example, you can pass it as a parameter to your API function
                serpapi_results = serpapi_search(job_description)

                # Simulate an API call by printing the results to the chat
                if serpapi_results:
                    st.write("")
                    display_serpapi_jobs(serpapi_results)
                else:
                    st.write("No job listings found using SerpApi for the given criteria.")
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