# ESL - Chatbot

# Language Assistant Chatbot

## Introduction

Language Assistant Chatbot is a Python-based project that leverages the OpenAI API to create a chatbot with enhanced language processing capabilities. The project integrates several tools for grammar checking, synonym finding, and definition providing, all within an easy-to-use chat interface.

## Features

- **Grammar Assistance**: Helps users with grammar and sentence structure in their queries.
- **Synonyms Finder**: Provides synonyms for any given word.
- **Definition Provider**: Offers definitions for words to enhance understanding and vocabulary.

## Getting Started

### Prerequisites

To run this project, you will need:
- Python 3.6 or higher.
- `chainlit`, `openai`, `langchain`, and `dotenv` Python packages.
- An OpenAI API key.

### Installation

1. Clone the repository to your local machine.
2. Install the required Python packages:
   ```bash
   pip install chainlit openai langchain python-dotenv
3. Create a .env file in the root directory of the project and add your OpenAI API key:
   OPENAI_API_KEY='your_api_key_here'

### Usage
- Run the chatbot:
   python [filename].py
- The chatbot will start, and you can interact with it by sending messages. The chatbot will utilize its tools to assist with grammar, synonyms, and definitions.

### How It Works
- The application initializes language tools for grammar checking, synonym finding, and word definitions.
- An agent is created to handle user queries, using the initialize_language_agent function.
- For each user query, the agent processes the input and provides an appropriate response based on the integrated tools.
- The chatbot ensures a user-friendly experience and maintains a rate limit for queries to manage server load and API usage effectively.

### Additonal Chatbots

- I have included two additional experimental chatbots using different LLMs (Feel free to modify them as desired)

