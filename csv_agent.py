import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your csv")
    st.header("Ask your CSV")

    user_csv = st.file_uploader("Upload you CSV file", type="csv")

    if user_csv is not None:
        user_question = st.text_input("Ask your question about CSV file:")
        llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo-instruct")

        agent = create_csv_agent(llm, user_csv)
        if user_question is not None and user_question !="":
            response = agent.run(user_question)
            st.write(response)


if __name__ == "__main__":
        main()