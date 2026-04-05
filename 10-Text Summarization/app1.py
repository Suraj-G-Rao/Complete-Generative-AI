import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader

# Streamlit App Configuration
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader('Summarize URL')

# Sidebar for API Key
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

# URL input for the user
generic_url = st.text_input("URL", label_visibility="collapsed")

# Groq API for LLM
llm = ChatGroq(model="Gemma-7b-It", groq_api_key=groq_api_key)

# Prompt template for summarization
prompt_template = """
Provide a summary of the following content in 300 words:
Content: {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# On Button Click: Summarize the Content
if st.button("Summarize the Content from YT or Website"):
    # Validate the inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the required information to get started.")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be a YouTube video or website URL.")
    else:
        try:
            with st.spinner("Fetching and summarizing the content..."):
                # Load data from the given URL
                if "youtube.com" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(generic_url, add_video_info=True)
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=True,  # Enable SSL verification
                        headers={
                            "User-Agent": (
                                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                            )
                        },
                    )

                # Load documents
                docs = loader.load()

                # Check if content was loaded successfully
                if not docs:
                    st.error("No content could be retrieved from the provided URL.")
                else:
                    # Summarize the content
                    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                    output_summary = chain.invoke({"input_documents": docs})
                    st.success(output_summary)

        except Exception as e:
            st.error(f"An error occurred: {e}")
