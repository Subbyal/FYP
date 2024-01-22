import streamlit as st
import random
import time

st.set_page_config(
    page_title="Job Searching Chatbot",
    page_icon=":briefcase:",
    layout="wide",
)

st.title("Job Searching Chatbot")
st.sidebar.title("Job Searching Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Your other code...

job_questions = [
    "SALAM",
    "SALAMALAIKUM",
    "ASSALAMUALAIKUM",
    "ASSALAMOALAIKUM",
    "ASSALAM U ALAIKUM",
    "ASSALAM O ALAIKOM",
    "ASSALAMOALAIKUM",
    "HELLO",
    "EMPLOYMENT",
    "HOW ARE YOU",
    "I WANT JOB",
    "YES",
    "BY",
]

responses = {
    "SALAM": "WALAIKOM ASSALAM! How can I assist you with your job search?",
    "SALAMALAIKUM": "WALAIKOM ASSALAM! How can I assist you with your job search?",
    "ASSALAMUALAIKUM": "WALAIKOM ASSALAM! How can I assist you with your job search?",
    "ASSALAMOALAIKUM": "WALAIKOM ASSALAM! How can I assist you with your job search?",
    "ASSALAM U ALAIKUM": "WALAIKOM ASSALAM! How can I assist you with your job search?",
    "ASSALAM O ALAIKOM": "WALAIKOM ASSALAM! How can I assist you with your job search?",
    "ASSALAMOALAIKUM": "WALAIKOM ASSALAM! How can I assist you with your job search?",
    "HELLO": "Hello! How can I assist you with your job search?",
    "EMPLOYMENT": "Sure, tell me more about the type of employment you are looking for.",
    "HOW ARE YOU": "I'm just a chatbot, but thanks for asking! How can I help you today?",
    "I WANT JOB": "Enter your job description",
    "YES": "Great! What specific job are you interested in?",
    "BY": "Goodbye! If you have more questions, feel free to ask.",
}

def clear_chat_history():
    st.session_state.messages = []
    st.session_state.job_results = []
    with open("chathistory.txt", "w") as file:
        for item in st.session_state.messages + st.session_state.job_results:
            file.write(f"{item['role']}: {item['content']}\n")

st.sidebar.button('Clear Chat History', on_click=clear_chat_history)
st.sidebar.markdown("<div class='custom button'></div>", unsafe_allow_html=True)

st.sidebar.markdown("## Customer Feedback:")
feedback = st.sidebar.text_area("Provide feedback of chatbot:")
if st.sidebar.button("Submit Feedback"):
    with open("feedback.txt", "a") as feedback_file:
        feedback_file.write(f"{feedback}\n")
    st.sidebar.success("Feedback submitted successfully!")

def save_to_chat_history(role, content):
    st.session_state.messages.append({"role": role, "content": content})
    with open("chathistory.txt", "a") as file:
        file.write(f"{role}: {content}\n")

def display_jobs(results):
    for index, result in enumerate(results, start=1):
        title = result.get('title', '')
        company = result.get('snippet', '')
        link = result.get('link', '')

        with st.expander(f"Job {index} - {title}"):
            st.write(f"Company: {company}")
            st.write(f"Link: {link}")

if prompt := st.chat_input("Enter your desired job (example: Software Engineer)"):
    save_to_chat_history("user", prompt)
    with st.chat_message("user"):
        st.markdown(prompt)

    job_description = prompt.upper()

    # Check if the user's input contains any of the job-related questions
    contains_job_question = any(question in job_description for question in job_questions)

    # Initialize response with a default message
    response = "I'm sorry, I didn't understand that. How can I assist you with your job search? Enter your description."

    if contains_job_question:
        # User input contains a job-related question, process accordingly
        role_response = "assistant"

        # Check if the job_description is in the responses dictionary
        if job_description in responses:
            response = responses[job_description]
        elif "JOB" in job_description:
            # Extract the job title from the user's input
            job_title = job_description.replace("JOB", "").strip()
            # Add your custom job search logic here if needed

        # Save the response to chat history
        save_to_chat_history(role_response, response)

        # Display the response
        with st.chat_message(role_response):
            st.markdown(response)
    else:
        # User input does not contain a job-related question, display a generic response
        with st.chat_message("assistant"):
            st.markdown("Hello! How can I assist you with your job search?")
