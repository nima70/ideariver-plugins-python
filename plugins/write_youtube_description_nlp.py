import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from the .env file to access sensitive data like API keys
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize the LangChain model with the provided OpenAI API key and model settings
llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4o-mini")

# Define the prompt template for generating YouTube descriptions based on a video transcript
prompt_template = ChatPromptTemplate.from_messages([
    ("system", """You are a YouTuber specializing in writing descriptions.
    Here is a video transcript. Please write a detailed and engaging YouTube description based on the transcript.
    """),
    ("user", "{input}"),  # Placeholder for the actual transcript input
])

# Output parser to process and return the response as a string
output_parser = StrOutputParser()

# Chain the prompt template, language model, and output parser into a sequence
chain = prompt_template | llm | output_parser

def write_youtube_description_nlp(transcript_data):
    """
    Generate a YouTube video description based on transcript data.

    Args:
        transcript_data (dict): A dictionary containing the video transcript.

    Returns:
        str: A well-structured YouTube video description.
    """
    # Extract the transcript and generate the description using the LangChain model
    description = chain.invoke({"input": transcript_data["transcript"]})
    
    return description
