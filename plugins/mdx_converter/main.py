import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ideariver_core import BasePlugin  # Assuming BasePlugin is part of ideariver-core

class ConvertToMDXPlugin(BasePlugin):
    """
    Plugin that converts transcript text into MDX format using OpenAI's LLM.
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
        self.llm = ChatOpenAI(api_key=self.openai_api_key, model="gpt-3.5-turbo")

        # Define the prompt template for converting a transcript into MDX
        self.prompt_template = ChatPromptTemplate.from_messages([
            ("system", """You are an assistant that converts transcript text into MDX format. The MDX should have proper headings, bullet points, and JSX components where appropriate."""),
            ("user", "{input}"),
        ])

        # Output parser to convert the response to a string
        self.output_parser = StrOutputParser()

        # Chain mechanism
        self.chain = self.prompt_template | self.llm | self.output_parser

    def run(self, input_data):
        """
        Run the plugin to convert the transcript text into MDX format.

        Args:
            input_data (dict): Dictionary with transcript text.

        Returns:
            str: MDX formatted content.
        """
        transcript_text = input_data.get("transcript_text")
        if not transcript_text:
            raise ValueError("The 'transcript_text' field is required.")

        # Invoke the LangChain model to generate MDX
        mdx_content = self.chain.invoke({"input": transcript_text})
        
        return mdx_content
