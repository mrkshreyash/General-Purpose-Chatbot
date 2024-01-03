import streamlit as st
import random
import time
import wikipedia
import webbrowser

def AssistantResponse(assistant_response:str) -> str:
    message_placeholder = st.empty()
    full_response = ""

    # Simulate stream of response with milliseconds delay
    
    for chunk in assistant_response.split():
        full_response += chunk + " "
        time.sleep(0.05)
        # Add a blinking cursor to simulate typing
        message_placeholder.markdown(full_response + "▌")
    message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

def ChatBot():
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
            # """ 
            # Greeting Module :
            #     USER greet the system and system also greet back to user
            # """
            
            greetings_prompt = ['hi', 'hey', 'hello']
            open_command = ['google', 'youtube']
            creator = ['tell me about your creator', 'who made you', 'who is your creator', 'who designed you', 'who created you']

            if any(greet in prompt.lower() for greet in greetings_prompt):
                assistant_response = random.choice(
                    [
                        "Hello there! How can I assist you today?",
                        "Hi, human! Is there anything I can help you with?",
                        "Do you need help?",
                    ]
                )
                AssistantResponse(assistant_response=assistant_response)

            elif any(command in prompt.lower() for command in open_command):
                if 'google' in prompt.lower():
                    webbrowser.open("https://www.google.com")
                    AssistantResponse(assistant_response="Google Opened in new tab !")
                
                if 'youtube' in prompt.lower():
                    webbrowser.open("https://www.youtube.com/")
                    AssistantResponse(assistant_response="Youtube Opened in new tab !")                

            elif any(create_prompt in prompt.lower() for create_prompt in creator):
                AssistantResponse("The programmer who created me is the student pursuing B.Tech in Artificial Intelligence and Data Science.")
                AssistantResponse("His name is Mr. Shreyash Avinash Kamble. He created this bot on date 03-01-2024 (3rd January 2024) in time period of 12:00 PM to 4:00 PM.")
                AssistantResponse("It is initially developed for a Pure Technology IT Solutions, as its task for selection as an Intern. You can check out his profiles from below links:")
                AssistantResponse("GitHub : https://github.com/mrkshreyash")
                AssistantResponse("LinkedIn : https://www.linkedin.com/in/shreyash-avinash-kamble-5a880021a/")
                
                
            else:
                try:
                    wiki_response = wikipedia.summary(prompt, sentences=3)
                    AssistantResponse(assistant_response=wiki_response)
                except Exception as e:
                    error_prompt = f"The above query/question is not understandable. Or the data regarding above query/question is not present. Please ask another query/question."
                    AssistantResponse(assistant_response=error_prompt)


    # st.write(st.session_state)
                    
if __name__ == '__main__':
    st.set_page_config(
        page_title="General Purpose Chatbot",
        layout="wide",
        page_icon=":tada:"
    )

   
    with st.container():
        left, mid, right = st.columns(3)
        with mid:
            st.title("General Purpose ChatBot".upper())

    ChatBot()
