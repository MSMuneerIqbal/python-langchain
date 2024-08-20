#type:ignore
from langchain import OpenAI 

# Set up your API key for OpenAI
import openai
openai.api_key = 'your-openai-api-key'

# Create an instance of the OpenAI LLM
llm = OpenAI(model_name="text-davinci-003", temperature=0.0)

# Generate a simple message
response = llm("Say 'Hello, World!'")

# Print the result
print(response)

