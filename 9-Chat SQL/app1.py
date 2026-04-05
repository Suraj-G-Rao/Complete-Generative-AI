import streamlit as st
from pathlib import Path
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.utilities import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from sqlalchemy import create_engine
import sqlite3
from langchain_groq import ChatGroq

# Streamlit app configuration
st.set_page_config(page_title="LangChain: Chat with SQL DB", page_icon="🦜")
st.title("🦜 LangChain: Chat with SQL DB")

# Database connection options
LOCALDB = "USE_LOCALDB"
MYSQL = "USE_MYSQL"
radio_opt = ["Use SQLite 3 Database - student.db", "Connect to MySQL Database"]

selected_opt = st.sidebar.radio(label="Choose the DB to chat with", options=radio_opt)

# MySQL configuration inputs
if radio_opt.index(selected_opt) == 1:
    db_uri = MYSQL
    mysql_host = st.sidebar.text_input("MySQL Host")
    mysql_user = st.sidebar.text_input("MySQL User")
    mysql_password = st.sidebar.text_input("MySQL Password", type="password")
    mysql_db = st.sidebar.text_input("MySQL Database Name")
else:
    db_uri = LOCALDB

# Groq API key input
api_key = st.sidebar.text_input(label="Groq API Key", type="password")

# Error handling for missing configurations
if not api_key:
    st.error("Please provide the Groq API Key.")
    st.stop()

if db_uri == MYSQL and not (mysql_host and mysql_user and mysql_password and mysql_db):
    st.error("Please provide all MySQL connection details.")
    st.stop()

# Initialize LLM model
try:
    llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
except Exception as e:
    st.error(f"Failed to initialize ChatGroq: {e}")
    st.stop()

# Database configuration function
@st.cache_resource(ttl="2h")
def configure_db(db_uri, mysql_host=None, mysql_user=None, mysql_password=None, mysql_db=None):
    if db_uri == LOCALDB:
        dbfilepath = (Path(__file__).parent / "student.db").absolute()
        creator = lambda: sqlite3.connect(f"file:{dbfilepath}?mode=ro", uri=True)
        return SQLDatabase(create_engine("sqlite:///", creator=creator))
    elif db_uri == MYSQL:
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}"))

# Connect to the selected database
try:
    if db_uri == MYSQL:
        db = configure_db(db_uri, mysql_host, mysql_user, mysql_password, mysql_db)
    else:
        db = configure_db(db_uri)
except Exception as e:
    st.error(f"Failed to connect to the database: {e}")
    st.stop()

# Create the toolkit and agent
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# Chat interface
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# User query input
user_query = st.chat_input(placeholder="Ask anything from the database")
if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        try:
            streamlit_callback = StreamlitCallbackHandler(st.container())
            response = agent.run(user_query, callbacks=[streamlit_callback])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)
        except Exception as e:
            st.error(f"Error during query execution: {e}")
