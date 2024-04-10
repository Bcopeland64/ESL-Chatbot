import chainlit as cl
import openai
from langchain.prompts import PromptTemplate
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool, initialize_agent
from dotenv import load_dotenv
import os
import time  # Import the time module for rate limiting

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI with the API key
model_name = "text-davinci-003"  # Using a GPT-3 model for English language tasks

# Tool for grammar checking
grammar_tool = Tool.from_function(name="Grammar Assistant",
                                   func=lambda text: openai.Completion.create(
                                       model=model_name,
                                       prompt=text,
                                       max_tokens=50),
                                   description="Helps with grammar and sentence structure.")

# Tool for providing synonyms
synonyms_tool = Tool.from_function(name="Synonyms Assistant",
                                    func=lambda word: openai.Completion.create(
                                        model=model_name,
                                        prompt=f"What are synonyms for {word}?",
                                        max_tokens=50),
                                    description="Provides synonyms for a given word.")

# Tool for providing definitions
definition_tool = Tool.from_function(name="Definition Assistant",
                                     func=lambda word: openai.Completion.create(
                                         model=model_name,
                                         prompt=f"What is the definition of {word}?",
                                         max_tokens=50),
                                     description="Provides the definition of a given word.")

def initialize_language_agent(llm):
    return initialize_agent(
        tools=[grammar_tool, synonyms_tool, definition_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        handle_parsing_errors=True
    )

agent = initialize_language_agent(None)

@cl.on_chat_start
def language_chatbot():
    agent = initialize_language_agent(None)
    cl.user_session.set("agent", agent)

@cl.on_message
async def process_user_query(message: cl.Message):
    agent = cl.user_session.get("agent")

    # Rate limiting: delay each request by 1 second
    time.sleep(30)

    response = await agent.acall(message.content,
                                 callbacks=[cl.AsyncLangchainCallbackHandler()])

    await cl.Message(response["output"]).send()
