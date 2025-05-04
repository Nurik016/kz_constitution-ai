import streamlit as st

from ai_chat import ai_chat
from handler_files import extract_text_from_file
from vector_store import save_to_vectorstore, query_vectorstore, save_query_answer


st.title('⚖️ ZanBot')

with st.sidebar:
    gemini_api_key = st.text_input("Gemini API Key", type="password")
    uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True, type=["txt", "pdf", "docx"])

    all_text = []

    if uploaded_files:
        for uploaded_file in uploaded_files:
            extracted = extract_text_from_file(uploaded_file)
            st.success(f"📄 {uploaded_file.name} loaded")
            all_text.append(extracted)

        save_to_vectorstore(all_text)

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if promt := st.chat_input('What can I do to help?'):
    context = query_vectorstore(promt)
    full_prompt = f"Context:\n{context}\n\nUser question:\n{promt}"

    st.chat_message('user').markdown(promt)
    st.session_state.messages.append({'role': 'user', 'content': promt})

    response = ai_chat(full_prompt, gemini_api_key)

    save_query_answer(promt, response)

    with st.chat_message('assistant'):
        st.markdown(response)

    st.session_state.messages.append({'role': 'assistant', 'content': response})
