import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from the .env file
load_dotenv()

# Access the OpenAI API key and other environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize LangChain's OpenAI model
llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4o-mini")

# Define the prompt template
prompt_template = ChatPromptTemplate.from_messages([
    ("system", """You are an assistant that detects chapters in video transcripts.
    Here is a video transcript. Please divide it into meaningful chapters. Provide the chapters with timestamps in the following format:

    00:00 Introduction
    10:00 Main topic
    20:00 Conclusion

    
    """),
    ("user", "{input}"),
])

# Output parser to convert the response to a string
output_parser = StrOutputParser()

# Use the chaining mechanism (RunnableSequence)
# chain = prompt_template | llm | output_parser
chain = prompt_template | llm | output_parser

def detect_chapters_nlp(transcript_data):
    """
    Detects chapters using an LLM (e.g., GPT) to analyze semantic transitions in the transcript.

    Args:
    transcript_data (dict): Transcript data passed as JSON.

    Returns:
    str: Detected chapters in YouTube format.
    """
    segments = transcript_data["segments"]
    full_transcript = " ".join([segment["text"] for segment in segments])

    # Invoke the LangChain model
    chapters_text = chain.invoke({"input": full_transcript})
    
    return chapters_text
