import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from ideariver_core import BasePlugin  # Assuming BasePlugin is part of ideariver-core

class ConvertToMDXPlugin(BasePlugin):
    """
    Plugin to convert transcript text into MDX format using LangChain's GPT models.
    """

    def __init__(self):
        self.llm = None

    def init(self, services):
        """
        Initialize the plugin with the OpenAI LLM via LangChain.
        
        Args:
            services (dict): Dictionary of services (e.g., logging, API keys).
        """
        # Load environment variables from the .env file to access sensitive data like API keys
        load_dotenv()

        # Retrieve OpenAI API key from environment variables
        openai_api_key = os.getenv('OPENAI_API_KEY')

        # Initialize OpenAI model via LangChain
        self.llm = ChatOpenAI(api_key=openai_api_key, model="gpt-3.5-turbo", temperature=0.7)

    def run(self, input_data):
        """
        Convert the provided transcript text into MDX format.

        Args:
            input_data (dict): Dictionary containing 'transcript_text'.

        Returns:
            str: Path to the saved MDX file.
        """
        transcript_text = input_data.get('transcript_text')
        if not transcript_text:
            raise ValueError("The 'transcript_text' field is required.")
        
        return self.convert_to_mdx(transcript_text)

    def convert_to_mdx(self, transcript_text):
        """Converts the provided transcript text into MDX format and saves it to a file."""

        # Define the message for MDX conversion
        system_message = {
            "role": "system",
            "content": "You are an assistant that converts transcript text into MDX format with headings, bullet points, and JSX where appropriate."
        }
        user_message = {
            "role": "user",
            "content": f"Transcript: {transcript_text}\n\nConvert this into MDX format."
        }

        # Create the LangChain prompt with system and user messages
        prompt = ChatPromptTemplate.from_messages([system_message, user_message])

        # Generate MDX using the LangChain LLM interface
        mdx_content = self.llm(prompt)

        # Save the MDX content to a file
        output_file = "transcript.mdx"
        with open(output_file, "w") as mdx_file:
            mdx_file.write(mdx_content)

        return output_file
