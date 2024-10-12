# plugin.py
import os
import json
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ideariver_core import BasePlugin  # Assuming BasePlugin is part of ideariver-core

class ChapterDetectionPlugin(BasePlugin):
    """
    Plugin that detects chapters from video transcripts using OpenAI's LLM.
    """

    def __init__(self):
        self.services = None

    def init(self, services):
        """
        Initialize the plugin with required services, such as OpenAI credentials.
        
        Args:
            services (dict): Dictionary of services (e.g., logging, configuration).
        """
        self.services = services

        # Load environment variables from the .env file if present
        load_dotenv()

        # Access OpenAI API key
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

        # Initialize LangChain's OpenAI model
        self.llm = ChatOpenAI(api_key=self.openai_api_key, model="gpt-4o-mini")

        # Define the prompt template
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", """You are an assistant that detects chapters in video transcripts.
            Here is a video transcript. Please divide it into meaningful chapters. Provide the chapters with timestamps in the following format:

            00:00 Introduction
            10:00 Main topic
            20:00 Conclusion
            """),
            ("user", "{input}"),
        ])

        # Output parser to convert the response to a string
        self.output_parser = StrOutputParser()

        # Chain mechanism
        self.chain = self.prompt_template | self.llm | self.output_parser

    def run(self, input_data):
        """
        Run the plugin to detect chapters from the transcript.

        Args:
            input_data (dict): Dictionary with transcript segments.

        Returns:
            str: Detected chapters in YouTube format.
        """
        segments = input_data["segments"]
        full_transcript = " ".join([segment["text"] for segment in segments])

        # Invoke the LangChain model
        chapters_text = self.chain.invoke({"input": full_transcript})
        
        return chapters_text
