import streamlit as st
from streamlit.logger import get_logger
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
import os
from langchain_openai import ChatOpenAI

logger = get_logger(__name__)

import os
if os.getenv('USER', "None") == 'appuser': # streamlit
    hf_token = st.secrets['OI_TOKEN']
    os.environ["openai_api_key"] = hf_token

st.title("my gen AI app")

temp = 1
logger.info(f"{temp=}")

with st.slider("Temperature", 0.0, 1.0, 0.5):
    temp = st.session_state.slider_value
    logger.info(f"{temp=}")

with st.form("sample_app"):
    txt = st.text_area("Enter text:", "what GPT stands for?")
    sub = st.form_submit_button("submit")
    if sub:
        llm1 =ChatOpenAI(model='gpt-4.1-mini', temperature=0.1, openai_api_key=os.environ["openai_api_key"])
        logger.info("invoking")
        ans = llm1.invoke(txt, temperature=temp)
        st.info(ans.content)
        logger.info("Done")
