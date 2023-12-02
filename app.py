import streamlit as st
from dotenv import load_dotenv




def main():
    load_dotenv
    st.set_page_config(page_title="Chat with multiple PDF's",page_icon=":books:")

    st.header("Chat with multiple PDF's :books:")
    st.text_input("Ask me a question from you document:")


    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader(" Upload yours pdf's and Hit Process")
        st.button("Process")
    


if __name__ == '__main__':
    main()