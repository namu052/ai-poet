from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from dotenv import load_dotenv
import os
import streamlit as st

# load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY, temperature=0.5)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user","{input}")
    ]

)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# content = "코딩"
# result = chain.invoke({"input": content + "에 대한 시를 써 줘"})
# print(result)


st.title("인공지능 시인")
content = st.text_input("시의 주제를 제시해주세요.")
st.write("시의 주제는", content)

if st.button("시 작성 요청하기"):
    with st.spinner("Wait for it..."):
        result = chain.invoke({"input": content + "에 대한 시를 써 줘"})
        st.write(result)
