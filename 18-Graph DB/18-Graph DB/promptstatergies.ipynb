{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "NEO4J_URI=\"neo4j+s://427c9a4f.databases.neo4j.io\"\n",
    "NEO4J_USERNAME=\"neo4j\"\n",
    "NEO4J_PASSWORD=\"rQJMGc6onbUh6iWZ27jOg5QeyqBcMq3JWxUJ3_Y\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "os.environ[\"NEO4J_URI\"] = NEO4J_URI\n",
    "os.environ[\"NEO4J_USERNAME\"] = NEO4J_USERNAME\n",
    "os.environ[\"NEO4J_PASSWORD\"] = NEO4J_PASSWORD"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<langchain_community.graphs.neo4j_graph.Neo4jGraph at 0x238d675adb0>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from langchain_community.graphs import Neo4jGraph\n",
    "graph=Neo4jGraph(url=NEO4J_URI,username=NEO4J_USERNAME,password=NEO4J_PASSWORD)\n",
    "graph"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "moview_query=\"\"\"\n",
    "LOAD CSV WITH HEADERS FROM\n",
    "'https://raw.githubusercontent.com/tomasonjo/blog-datasets/main/movies/movies_small.csv' as row\n",
    "\n",
    "MERGE(m:Movie{id:row.movieId})\n",
    "SET m.released = date(row.released),\n",
    "    m.title = row.title,\n",
    "    m.imdbRating = toFloat(row.imdbRating)\n",
    "FOREACH (director in split(row.director, '|') | \n",
    "    MERGE (p:Person {name:trim(director)})\n",
    "    MERGE (p)-[:DIRECTED]->(m))\n",
    "FOREACH (actor in split(row.actors, '|') | \n",
    "    MERGE (p:Person {name:trim(actor)})\n",
    "    MERGE (p)-[:ACTED_IN]->(m))\n",
    "FOREACH (genre in split(row.genres, '|') | \n",
    "    MERGE (g:Genre {name:trim(genre)})\n",
    "    MERGE (m)-[:IN_GENRE]->(g))\n",
    "\n",
    "\n",
    "\"\"\"\n",
    "graph.query(moview_query)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ChatGroq(client=<groq.resources.chat.completions.Completions object at 0x00000238D667EF00>, async_client=<groq.resources.chat.completions.AsyncCompletions object at 0x00000238D667F920>, model_name='Gemma2-9b-It', groq_api_key=SecretStr('**********'))"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "from dotenv import load_dotenv\n",
    "load_dotenv()\n",
    "\n",
    "groq_api_key=os.getenv(\"GROQ_API_KEY\")\n",
    "from langchain_groq import ChatGroq\n",
    "llm=ChatGroq(groq_api_key=groq_api_key,model_name=\"Gemma2-9b-It\")\n",
    "llm"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GraphCypherQAChain(verbose=True, graph=<langchain_community.graphs.neo4j_graph.Neo4jGraph object at 0x00000238D675ADB0>, cypher_generation_chain=LLMChain(prompt=PromptTemplate(input_variables=['question', 'schema'], template='Task:Generate Cypher statement to query a graph database.\\nInstructions:\\nUse only the provided relationship types and properties in the schema.\\nDo not use any other relationship types or properties that are not provided.\\nSchema:\\n{schema}\\nNote: Do not include any explanations or apologies in your responses.\\nDo not respond to any questions that might ask anything else than for you to construct a Cypher statement.\\nDo not include any text except the generated Cypher statement.\\n\\nThe question is:\\n{question}'), llm=ChatGroq(client=<groq.resources.chat.completions.Completions object at 0x00000238D667EF00>, async_client=<groq.resources.chat.completions.AsyncCompletions object at 0x00000238D667F920>, model_name='Gemma2-9b-It', groq_api_key=SecretStr('**********'))), qa_chain=LLMChain(prompt=PromptTemplate(input_variables=['context', 'question'], template=\"You are an assistant that helps to form nice and human understandable answers.\\nThe information part contains the provided information that you must use to construct an answer.\\nThe provided information is authoritative, you must never doubt it or try to use your internal knowledge to correct it.\\nMake the answer sound as a response to the question. Do not mention that you based the result on the given information.\\nHere is an example:\\n\\nQuestion: Which managers own Neo4j stocks?\\nContext:[manager:CTL LLC, manager:JANE STREET GROUP LLC]\\nHelpful Answer: CTL LLC, JANE STREET GROUP LLC owns Neo4j stocks.\\n\\nFollow this example when generating answers.\\nIf the provided information is empty, say that you don't know the answer.\\nInformation:\\n{context}\\n\\nQuestion: {question}\\nHelpful Answer:\"), llm=ChatGroq(client=<groq.resources.chat.completions.Completions object at 0x00000238D667EF00>, async_client=<groq.resources.chat.completions.AsyncCompletions object at 0x00000238D667F920>, model_name='Gemma2-9b-It', groq_api_key=SecretStr('**********'))), graph_schema='Node properties are the following:\\nCEO {POB: STRING, name: STRING, YOB: INTEGER},Company {name: STRING},enterpreneur {POB: STRING, name: STRING, YOB: INTEGER},Country {name: STRING},Person {name: STRING, born: INTEGER},Movie {title: STRING, released: INTEGER, genre: STRING, movieId: INTEGER, id: STRING, imdbRating: FLOAT},User {name: STRING, city: STRING, userId: INTEGER, age: INTEGER},Post {postId: INTEGER, content: STRING, timestamp: DATE_TIME}\\nRelationship properties are the following:\\n\\nThe relationships are the following:\\n(:enterpreneur)-[:LIVES_IN]->(:Country),(:Person)-[:ACTED_IN]->(:Movie),(:Person)-[:DIRECTED]->(:Movie),(:User)-[:POSTED]->(:Post),(:User)-[:FRIEND]->(:User),(:User)-[:LIKES]->(:User)')"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from langchain.chains import GraphCypherQAChain\n",
    "chain=GraphCypherQAChain.from_llm(graph=graph,llm=llm,exclude_types=[\"Genre\"],verbose=True)\n",
    "chain"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Node properties are the following:\\nCEO {POB: STRING, name: STRING, YOB: INTEGER},Company {name: STRING},enterpreneur {POB: STRING, name: STRING, YOB: INTEGER},Country {name: STRING},Person {name: STRING, born: INTEGER},Movie {title: STRING, released: INTEGER, genre: STRING, movieId: INTEGER, id: STRING, imdbRating: FLOAT},User {name: STRING, city: STRING, userId: INTEGER, age: INTEGER},Post {postId: INTEGER, content: STRING, timestamp: DATE_TIME}\\nRelationship properties are the following:\\n\\nThe relationships are the following:\\n(:enterpreneur)-[:LIVES_IN]->(:Country),(:Person)-[:ACTED_IN]->(:Movie),(:Person)-[:DIRECTED]->(:Movie),(:User)-[:POSTED]->(:Post),(:User)-[:FRIEND]->(:User),(:User)-[:LIKES]->(:User)'"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "chain.graph_schema"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "examples = [\n",
    "    {\n",
    "        \"question\": \"How many artists are there?\",\n",
    "        \"query\": \"MATCH (a:Person)-[:ACTED_IN]->(:Movie) RETURN count(DISTINCT a)\",\n",
    "    },\n",
    "    {\n",
    "        \"question\": \"Which actors played in the movie Casino?\",\n",
    "        \"query\": \"MATCH (m:Movie {{title: 'Casino'}})<-[:ACTED_IN]-(a) RETURN a.name\",\n",
    "    },\n",
    "    {\n",
    "        \"question\": \"How many movies has Tom Hanks acted in?\",\n",
    "        \"query\": \"MATCH (a:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie) RETURN count(m)\",\n",
    "    },\n",
    "    {\n",
    "        \"question\": \"List all the genres of the movie Schindler's List\",\n",
    "        \"query\": \"MATCH (m:Movie {{title: 'Schindler\\\\'s List'}})-[:IN_GENRE]->(g:Genre) RETURN g.name\",\n",
    "    },\n",
    "    {\n",
    "        \"question\": \"Which actors have worked in movies from both the comedy and action genres?\",\n",
    "        \"query\": \"MATCH (a:Person)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g1:Genre), (a)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g2:Genre) WHERE g1.name = 'Comedy' AND g2.name = 'Action' RETURN DISTINCT a.name\",\n",
    "    },\n",
    "    {\n",
    "        \"question\": \"Which directors have made movies with at least three different actors named 'John'?\",\n",
    "        \"query\": \"MATCH (d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Person) WHERE a.name STARTS WITH 'John' WITH d, COUNT(DISTINCT a) AS JohnsCount WHERE JohnsCount >= 3 RETURN d.name\",\n",
    "    },\n",
    "    {\n",
    "        \"question\": \"Identify movies where directors also played a role in the film.\",\n",
    "        \"query\": \"MATCH (p:Person)-[:DIRECTED]->(m:Movie), (p)-[:ACTED_IN]->(m) RETURN m.title, p.name\",\n",
    "    },\n",
    "    {\n",
    "        \"question\": \"Find the actor with the highest number of movies in the database.\",\n",
    "        \"query\": \"MATCH (a:Actor)-[:ACTED_IN]->(m:Movie) RETURN a.name, COUNT(m) AS movieCount ORDER BY movieCount DESC LIMIT 1\",\n",
    "    },\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate\n",
    "\n",
    "example_prompt=PromptTemplate.from_template(\n",
    "    \"User input:{question}\\n Cypher query:{query}\"\n",
    ")\n",
    "\n",
    "prompt=FewShotPromptTemplate(\n",
    "    examples=examples[:5],\n",
    "    example_prompt=example_prompt,\n",
    "    prefix=\"You are a Neo4j expert. Given an input question,create a syntactically very accurate Cypher query\",\n",
    "    suffix=\"User input: {question}\\nCypher query: \",\n",
    "    input_variables=[\"question\",\"schema\"]\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "FewShotPromptTemplate(input_variables=['question'], examples=[{'question': 'How many artists are there?', 'query': 'MATCH (a:Person)-[:ACTED_IN]->(:Movie) RETURN count(DISTINCT a)'}, {'question': 'Which actors played in the movie Casino?', 'query': \"MATCH (m:Movie {{title: 'Casino'}})<-[:ACTED_IN]-(a) RETURN a.name\"}, {'question': 'How many movies has Tom Hanks acted in?', 'query': \"MATCH (a:Person {{name: 'Tom Hanks'}})-[:ACTED_IN]->(m:Movie) RETURN count(m)\"}, {'question': \"List all the genres of the movie Schindler's List\", 'query': \"MATCH (m:Movie {{title: 'Schindler\\\\'s List'}})-[:IN_GENRE]->(g:Genre) RETURN g.name\"}, {'question': 'Which actors have worked in movies from both the comedy and action genres?', 'query': \"MATCH (a:Person)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g1:Genre), (a)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g2:Genre) WHERE g1.name = 'Comedy' AND g2.name = 'Action' RETURN DISTINCT a.name\"}], example_prompt=PromptTemplate(input_variables=['query', 'questions'], template='User input:{questions}\\n Cypher query:{query}'), suffix='User input: {question}\\nCypher query: ', prefix='You are a Neo4j expert. Given an input question,create a sytacrically very accurate Cypher query')"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prompt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "You are a Neo4j expert. Given an input question,create a syntactically very accurate Cypher query\n",
      "\n",
      "User input:How many artists are there?\n",
      " Cypher query:MATCH (a:Person)-[:ACTED_IN]->(:Movie) RETURN count(DISTINCT a)\n",
      "\n",
      "User input:Which actors played in the movie Casino?\n",
      " Cypher query:MATCH (m:Movie {title: 'Casino'})<-[:ACTED_IN]-(a) RETURN a.name\n",
      "\n",
      "User input:How many movies has Tom Hanks acted in?\n",
      " Cypher query:MATCH (a:Person {name: 'Tom Hanks'})-[:ACTED_IN]->(m:Movie) RETURN count(m)\n",
      "\n",
      "User input:List all the genres of the movie Schindler's List\n",
      " Cypher query:MATCH (m:Movie {title: 'Schindler\\'s List'})-[:IN_GENRE]->(g:Genre) RETURN g.name\n",
      "\n",
      "User input:Which actors have worked in movies from both the comedy and action genres?\n",
      " Cypher query:MATCH (a:Person)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g1:Genre), (a)-[:ACTED_IN]->(:Movie)-[:IN_GENRE]->(g2:Genre) WHERE g1.name = 'Comedy' AND g2.name = 'Action' RETURN DISTINCT a.name\n",
      "\n",
      "User input: How many artists are there?\n",
      "Cypher query: \n"
     ]
    }
   ],
   "source": [
    "print(prompt.format(question=\"How many artists are there?\", schema=\"foo\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "llm\n",
    "chain=GraphCypherQAChain.from_llm(graph=graph,llm=llm,cypher_prompt=prompt,verbose=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\u001b[1m> Entering new GraphCypherQAChain chain...\u001b[0m\n",
      "Generated Cypher:\n",
      "\u001b[32;1m\u001b[1;3mcypher\n",
      "MATCH (m:Movie {title: 'Casino'})<-[:ACTED_IN]-(a)\n",
      "RETURN a.name\n",
      "\u001b[0m\n",
      "Full Context:\n",
      "\u001b[32;1m\u001b[1;3m[{'a.name': 'Robert De Niro'}, {'a.name': 'Joe Pesci'}, {'a.name': 'Sharon Stone'}, {'a.name': 'James Woods'}]\u001b[0m\n",
      "\n",
      "\u001b[1m> Finished chain.\u001b[0m\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "{'query': 'Which actors played in the movie Casino?',\n",
       " 'result': 'Robert De Niro, Joe Pesci, Sharon Stone, and James Woods.  \\n'}"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "chain.invoke(\"Which actors played in the movie Casino?\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\n",
      "\u001b[1m> Entering new GraphCypherQAChain chain...\u001b[0m\n",
      "Generated Cypher:\n",
      "\u001b[32;1m\u001b[1;3mcypher\n",
      "MATCH (a:Person)<-[:ACTED_IN]-(m:Movie) \n",
      "WHERE size((a)-[:ACTED_IN]->(:Movie)) > 1 \n",
      "RETURN a.name\n",
      "\u001b[0m\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "Generated Cypher Statement is not valid\n{code: Neo.ClientError.Statement.SyntaxError} {message: A pattern expression should only be used in order to test the existence of a pattern. It can no longer be used inside the function size(), an alternative is to replace size() with COUNT {}. (line 3, column 12 (offset: 59))\n\"WHERE size((a)-[:ACTED_IN]->(:Movie)) > 1\"\n            ^}",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mCypherSyntaxError\u001b[0m                         Traceback (most recent call last)",
      "File \u001b[1;32me:\\UDemy Final\\GraphLangchain\\venv\\Lib\\site-packages\\langchain_community\\graphs\\neo4j_graph.py:419\u001b[0m, in \u001b[0;36mNeo4jGraph.query\u001b[1;34m(self, query, params)\u001b[0m\n\u001b[0;32m    418\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 419\u001b[0m     data \u001b[38;5;241m=\u001b[39m \u001b[43msession\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun\u001b[49m\u001b[43m(\u001b[49m\u001b[43mQuery\u001b[49m\u001b[43m(\u001b[49m\u001b[43mtext\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mquery\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mtimeout\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mtimeout\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mparams\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    420\u001b[0m     json_data \u001b[38;5;241m=\u001b[39m [r\u001b[38;5;241m.\u001b[39mdata() \u001b[38;5;28;01mfor\u001b[39;00m r \u001b[38;5;129;01min\u001b[39;00m data]\n",
      "File \u001b[1;32me:\\UDemy Final\\GraphLangchain\\venv\\Lib\\site-packages\\neo4j\\_sync\\work\\session.py:312\u001b[0m, in \u001b[0;36mSession.run\u001b[1;34m(self, query, parameters, **kwargs)\u001b[0m\n\u001b[0;32m    311\u001b[0m parameters \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mdict\u001b[39m(parameters \u001b[38;5;129;01mor\u001b[39;00m {}, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n\u001b[1;32m--> 312\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_auto_result\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_run\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    313\u001b[0m \u001b[43m    \u001b[49m\u001b[43mquery\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mparameters\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_config\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdatabase\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    314\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_config\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mimpersonated_user\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_config\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdefault_access_mode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    315\u001b[0m \u001b[43m    \u001b[49m\u001b[43mbookmarks\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_config\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mnotifications_min_severity\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    316\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_config\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mnotifications_disabled_categories\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    317\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    319\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_auto_result\n",
      "File \u001b[1;32me:\\UDemy Final\\GraphLangchain\\venv\\Lib\\site-packages\\neo4j\\_sync\\work\\result.py:181\u001b[0m, in \u001b[0;36mResult._run\u001b[1;34m(self, query, parameters, db, imp_user, access_mode, bookmarks, notifications_min_severity, notifications_disabled_categories)\u001b[0m\n\u001b[0;32m    180\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_connection\u001b[38;5;241m.\u001b[39msend_all()\n\u001b[1;32m--> 181\u001b[0m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_attach\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32me:\\UDemy Final\\GraphLangchain\\venv\\Lib\\site-packages\\neo4j\\_sync\\work\\result.py:292\u001b[0m, in \u001b[0;36mResult._attach\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    291\u001b[0m \u001b[38;5;28;01mwhile\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_attached \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mFalse\u001b[39;00m:\n\u001b[1;32m--> 292\u001b[0m     \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_connection\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mfetch_message\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32me:\\UDemy Final\\GraphLangchain\\venv\\Lib\\site-packages\\neo4j\\_sync\\io\\_common.py:180\u001b[0m, in \u001b[0;36mConnectionErrorHandler.__getattr__.<locals>.outer.<locals>.inner\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    179\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 180\u001b[0m     \u001b[43mfunc\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    181\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m (Neo4jError, ServiceUnavailable, SessionExpired) \u001b[38;5;28;01mas\u001b[39;00m exc:\n",
      "File \u001b[1;32me:\\UDemy Final\\GraphLangchain\\venv\\Lib\\site-packages\\neo4j\\_sync\\io\\_bolt.py:851\u001b[0m, in \u001b[0;36mBolt.fetch_message\u001b[1;34m(self)\u001b[0m\n\u001b[0;32m    848\u001b[0m tag, fields \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39minbox\u001b[38;5;241m.\u001b[39mpop(\n\u001b[0;32m    849\u001b[0m     hydration_hooks\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mresponses[\u001b[38;5;241m0\u001b[39m]\u001b[38;5;241m.\u001b[39mhydration_hooks\n\u001b[0;32m    850\u001b[0m )\n\u001b[1;32m--> 851\u001b[0m res \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_process_message\u001b[49m\u001b[43m(\u001b[49m\u001b[43mtag\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mfields\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    852\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39midle_since \u001b[38;5;241m=\u001b[39m perf_counter()\n",
      "File \u001b[1;32me:\\UDemy Final\\GraphLangchain\\venv\\Lib\\site-packages\\neo4j\\_sync\\io\\_bolt5.py:376\u001b[0m, in \u001b[0;36mBolt5x0._process_message\u001b[1;34m(self, tag, fields)\u001b[0m\n\u001b[0;32m    375\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 376\u001b[0m     \u001b[43mresponse\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mon_failure\u001b[49m\u001b[43m(\u001b[49m\u001b[43msummary_metadata\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;129;43;01mor\u001b[39;49;00m\u001b[43m \u001b[49m\u001b[43m{\u001b[49m\u001b[43m}\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    377\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m (ServiceUnavailable, DatabaseUnavailable):\n",
      "File \u001b[1;32me:\\UDemy Final\\GraphLangchain\\venv\\Lib\\site-packages\\neo4j\\_sync\\io\\_common.py:247\u001b[0m, in \u001b[0;36mResponse.on_failure\u001b[1;34m(self, metadata)\u001b[0m\n\u001b[0;32m    246\u001b[0m Util\u001b[38;5;241m.\u001b[39mcallback(handler)\n\u001b[1;32m--> 247\u001b[0m \u001b[38;5;28;01mraise\u001b[39;00m Neo4jError\u001b[38;5;241m.\u001b[39mhydrate(\u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mmetadata)\n",
      "\u001b[1;31mCypherSyntaxError\u001b[0m: {code: Neo.ClientError.Statement.SyntaxError} {message: A pattern expression should only be used in order to test the existence of a pattern. It can no longer be used inside the function size(), an alternative is to replace size() with COUNT {}. (line 3, column 12 (offset: 59))\n\"WHERE size((a)-[:ACTED_IN]->(:Movie)) > 1\"\n            ^}",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[33], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[43mchain\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43minvoke\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mactors who acted in multiple movies\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32me:\\UDemy Final\\GraphLangchain\\venv\\Lib\\site-packages\\langchain\\chains\\base.py:166\u001b[0m, in \u001b[0;36mChain.invoke\u001b[1;34m(self, input, config, **kwargs)\u001b[0m\n\u001b[0;32m    164\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mBaseException\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[0;32m    165\u001b[0m     run_manager\u001b[38;5;241m.\u001b[39mon_chain_error(e)\n\u001b[1;32m--> 166\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m e\n\u001b[0;32m    167\u001b[0m run_manager\u001b[38;5;241m.\u001b[39mon_chain_end(outputs)\n\u001b[0;32m    169\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m include_run_info:\n",
      "File \u001b[1;32me:\\UDemy Final\\GraphLangchain\\venv\\Lib\\site-packages\\langchain\\chains\\base.py:156\u001b[0m, in \u001b[0;36mChain.invoke\u001b[1;34m(self, input, config, **kwargs)\u001b[0m\n\u001b[0;32m    153\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m    154\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_validate_inputs(inputs)\n\u001b[0;32m    155\u001b[0m     outputs \u001b[38;5;241m=\u001b[39m (\n\u001b[1;32m--> 156\u001b[0m         \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_call\u001b[49m\u001b[43m(\u001b[49m\u001b[43minputs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mrun_manager\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mrun_manager\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    157\u001b[0m         \u001b[38;5;28;01mif\u001b[39;00m new_arg_supported\n\u001b[0;32m    158\u001b[0m         \u001b[38;5;28;01melse\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_call(inputs)\n\u001b[0;32m    159\u001b[0m     )\n\u001b[0;32m    161\u001b[0m     final_outputs: Dict[\u001b[38;5;28mstr\u001b[39m, Any] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mprep_outputs(\n\u001b[0;32m    162\u001b[0m         inputs, outputs, return_only_outputs\n\u001b[0;32m    163\u001b[0m     )\n\u001b[0;32m    164\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mBaseException\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m e:\n",
      "File \u001b[1;32me:\\UDemy Final\\GraphLangchain\\venv\\Lib\\site-packages\\langchain_community\\chains\\graph_qa\\cypher.py:338\u001b[0m, in \u001b[0;36mGraphCypherQAChain._call\u001b[1;34m(self, inputs, run_manager)\u001b[0m\n\u001b[0;32m    335\u001b[0m \u001b[38;5;66;03m# Retrieve and limit the number of results\u001b[39;00m\n\u001b[0;32m    336\u001b[0m \u001b[38;5;66;03m# Generated Cypher be null if query corrector identifies invalid schema\u001b[39;00m\n\u001b[0;32m    337\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m generated_cypher:\n\u001b[1;32m--> 338\u001b[0m     context \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mgraph\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mquery\u001b[49m\u001b[43m(\u001b[49m\u001b[43mgenerated_cypher\u001b[49m\u001b[43m)\u001b[49m[: \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mtop_k]\n\u001b[0;32m    339\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    340\u001b[0m     context \u001b[38;5;241m=\u001b[39m []\n",
      "File \u001b[1;32me:\\UDemy Final\\GraphLangchain\\venv\\Lib\\site-packages\\langchain_community\\graphs\\neo4j_graph.py:425\u001b[0m, in \u001b[0;36mNeo4jGraph.query\u001b[1;34m(self, query, params)\u001b[0m\n\u001b[0;32m    423\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m json_data\n\u001b[0;32m    424\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m CypherSyntaxError \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[1;32m--> 425\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mGenerated Cypher Statement is not valid\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;132;01m{\u001b[39;00me\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mValueError\u001b[0m: Generated Cypher Statement is not valid\n{code: Neo.ClientError.Statement.SyntaxError} {message: A pattern expression should only be used in order to test the existence of a pattern. It can no longer be used inside the function size(), an alternative is to replace size() with COUNT {}. (line 3, column 12 (offset: 59))\n\"WHERE size((a)-[:ACTED_IN]->(:Movie)) > 1\"\n            ^}"
     ]
    }
   ],
   "source": [
    "chain.invoke(\"actors who acted in multiple movies\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
