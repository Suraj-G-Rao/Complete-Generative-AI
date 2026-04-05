import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import YouTubeTranscriptApiException

# Streamlit App Config
st.set_page_config(page_title="LangChain: Summarize Text From YT or Website", page_icon="🦜")
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader("Summarize URL")

# Sidebar for API Key and URL Input
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", value="", type="password")

generic_url = st.text_input("Enter the URL (YouTube or Website):", label_visibility="collapsed")

# Gemma Model Using Groq API
llm = ChatGroq(model="Gemma-7b-It", groq_api_key=groq_api_key)

prompt_template = """
Provide a summary of the following content in 300 words:
Content: {text}
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["text"])

# Function to extract video ID from YouTube URL
def extract_video_id(url):
    if "youtube.com" in url or "youtu.be" in url:
        if "v=" in url:
            return url.split("v=")[-1].split("&")[0]
        elif "youtu.be/" in url:
            return url.split("youtu.be/")[-1]
    return None

# Function to fetch YouTube transcript
def fetch_youtube_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([item['text'] for item in transcript])
    except YouTubeTranscriptApiException as e:
        st.error(f"Error fetching transcript: {e}")
        return None

if st.button("Summarize the Content from YT or Website"):
    # Validate inputs
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started.")
    elif not validators.url(generic_url):
        st.error("Please enter a valid URL. It can be a YouTube video URL or website URL.")
    else:
        try:
            with st.spinner("Processing..."):
                docs = None
                # Loading content from the URL
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    video_id = extract_video_id(generic_url)
                    if video_id:
                        transcript = fetch_youtube_transcript(video_id)
                        if transcript:
                            docs = [{"page_content": transcript}]
                        else:
                            st.error("No transcript found for this YouTube video.")
                    else:
                        st.error("Invalid YouTube URL.")
                else:
                    try:
                        loader = UnstructuredURLLoader(
                            urls=[generic_url],
                            ssl_verify=False,
                            headers={
                                "User-Agent": (
                                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1)"
                                    " AppleWebKit/537.36 (KHTML, like Gecko)"
                                    " Chrome/116.0.0.0 Safari/537.36"
                                )
                            },
                        )
                        docs = loader.load()
                    except Exception as url_error:
                        st.error(f"Error loading website data: {url_error}")

                # Summarization process
                if docs:
                    chain = load_summarize_chain(llm, chain_type="stuff", prompt=prompt)
                    output_summary = chain.run(docs)
                    st.success("Summary:")
                    st.write(output_summary)
                else:
                    st.error("Failed to load content from the provided URL.")

        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
