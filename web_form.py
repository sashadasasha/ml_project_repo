import streamlit as st
import speech_syntese as ss

def main():
    st.title('Добро пожаловать в наш чат. Спросите меня что-нибудь')
    prompt = st.chat_input(placeholder="Начните разговор")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ss.generate_answer(prompt)
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role": "assistant", "content": full_response})

       
if __name__ == "__main__":
    main()