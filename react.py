import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv()

llm = Ollama(model="mistral")
tools = load_tools(["llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

agent.run("My age is 28, what is my age raised at the power of 2.4")