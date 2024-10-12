import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ideariver_core import BasePlugin  # Assuming ideariver_core is part of your system

class YouTubeDescriptionPlugin(BasePlugin):
    """
    Plugin that generates YouTube video descriptions based on transcript data using LangChain.
    """

    def __init__(self):
        self.llm = None
        self.chain = None

    def init(self, services):
        """
        Initialize the plugin with required services like OpenAI API credentials.
        
        Args:
            services (dict): Dictionary of services (e.g., logging, configuration).
        """
        # Load environment variables from the .env file to access sensitive data like API keys
        load_dotenv()

        # Retrieve OpenAI API key from environment variables
        openai_api_key = os.getenv('OPENAI_API_KEY')

        # Initialize the LangChain model with the provided OpenAI API key
        self.llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4o-mini")

        # Define the prompt template for generating YouTube descriptions based on the video transcript
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """You are a YouTuber specializing in writing descriptions.
            Here is a video transcript. Please write a detailed and engaging YouTube description based on the transcript.
            """),
            ("user", "{input}"),  # Placeholder for the actual transcript input
        ])

        # Output parser to process and return the response as a string
        output_parser = StrOutputParser()

        # Chain the prompt template, language model, and output parser into a sequence
        self.chain = prompt_template | self.llm | output_parser

    def run(self, input_data):
        """
        Generate a YouTube video description based on transcript data.

        Args:
            input_data (dict): Dictionary containing the video transcript.

        Returns:
            str: A well-structured YouTube video description.
        """
        transcript = input_data.get('transcript')
        if not transcript:
            raise ValueError("The 'transcript' field is required.")
        
        # Generate the description using the LangChain model
        return self.chain.invoke({"input": transcript})
