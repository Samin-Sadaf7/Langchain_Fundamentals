#Import for deploying LLM
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes

load_dotenv()

#Create the prompts
system_template = "Translate the following into {language}:"

prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# Create the model
model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)

#Create parser
parser = StrOutputParser()

#Create chain
chain = prompt_template | model | parser 

app = FastAPI(
    title="My LLM API",
    description="My first LLM API",
    version="1.0",
)

add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)