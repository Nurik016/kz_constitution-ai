import streamlit as st

from ai_chat import ai_chat

st.title('ZanBot')



with st.sidebar:
    gemini_api_key = st.text_input("Gemini API Key", type="password")

    uploaded_files = st.file_uploader("Upload a file", accept_multiple_files=True)

    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)



if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if promt := st.chat_input('What can I do to help?'):
    st.chat_message('user').markdown(promt)
    st.session_state.messages.append({'role':'user', 'content':promt})

    answer = ai_chat(promt, gemini_api_key) #ai

    response = answer
    with st.chat_message('assistant'):
        st.markdown(response)

    st.session_state.messages.append({'role':'assistant', 'content':response})