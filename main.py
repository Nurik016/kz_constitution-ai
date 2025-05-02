import streamlit as st

st.title('Echo Bot')

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if promt := st.chat_input('What is up?'):
    st.chat_message('user').markdown(promt)
    st.session_state.messages.append({'role':'user', 'content':promt})

    response = f'Echo: {promt}'
    with st.chat_message('assistant'):
        st.markdown(response)

    st.session_state.messages.append({'role':'assistant', 'content':response})