from langchain import OpenAI
from langchain.prompts import PromptTemplate

# Initialize OpenAI model via LangChain
llm = OpenAI(model="gpt-3.5-turbo", temperature=0.7)

def convert_to_mdx_with_langchain(transcript_text):
    """Converts the provided transcript text into an MDX formatted file using ChatGPT via LangChain."""
    
    # Define a prompt template for MDX conversion
    template = """
    Convert the following transcript text into MDX format with proper headings, bullet points, and any appropriate JSX:
    
    Transcript: {transcript_text}
    
    MDX:
    """
    
    # Create the LangChain prompt
    prompt = PromptTemplate(template=template, input_variables=["transcript_text"])
    
    # Generate MDX using the LangChain LLM interface
    formatted_prompt = prompt.format(transcript_text=transcript_text)
    mdx_content = llm(formatted_prompt)

    # Save the MDX content to a file
    with open("transcript.mdx", "w") as mdx_file:
        mdx_file.write(mdx_content)

    return "transcript.mdx"
