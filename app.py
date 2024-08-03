import streamlit as st
from langchain import PromptTemplate
from langchain.llms import AzureOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Assign variables from environment
OPENAI_API_TYPE = os.getenv("OPENAI_API_TYPE")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")
OPENAI_MODEL_NAME=os.getenv("OPENAI_MODEL_NAME")

llm = AzureOpenAI(deployment_name=DEPLOYMENT_NAME,
                      model_name=OPENAI_MODEL_NAME,
                      openai_api_base=OPENAI_API_BASE,
                      openai_api_key=OPENAI_API_KEY
                      )

prompts = {
    "Sentiment": None,
    "Review_expressing": None,
    "Translator": None,
    "Tone_converter": None,
    "AI_assistant_email": None
    }


st.title("Langchain prompts demo")
prompt_method = st.sidebar.selectbox("Select a prompt method", list(prompts.keys()))
# display_input_form(prompt_method)
# st.write(prompt_method)

if prompt_method == "Sentiment":
    user_query = st.text_input("Enter the sentence")
    
    template = """
    I need you to find What is the sentiment of the following product review, 
    say the response in simple one word way,positive or negative.
    Review text: {user_query}
    """
    prompt = PromptTemplate(
        input_variables=["user_query"],
        template=template,
        )
    
    response = llm(
            prompt.format(
                user_query=user_query
            )
        )
    st.write(response)
    
if prompt_method == "Review_expressing":
    user_query = st.text_input("Enter the sentence")
    template = """ Identify a list of emotions that the writer of the 
    following review is expressing. Include no more than 
    five items in the list. Format your answer as a list of 
    lower-case words separated by commas.

    Review text: {user_query}

    """
    prompt = PromptTemplate(
        input_variables=["user_query"],
        template=template,
        )
    
    response = llm(
            prompt.format(
                user_query=user_query
            )
        )
    st.write(response)
    
if prompt_method == "Translator":
    user_query = st.text_input("Enter the sentence")
    template= """I need you to act as english translater, 
    analyse the language given by the user and translate that input text to english and display.
    input :{user_query}
    """
    
    prompt = PromptTemplate(
        input_variables=["user_query"],
        template=template,
        )
    
    response = llm(
            prompt.format(
                user_query=user_query
            )
        )
    st.write(response)
    
if prompt_method == "Tone_converter":
    user_query = st.text_input("Enter the sentence")
    template = """
    I need you to be a Translator the following from slang to a business letter
    input: {user_query}
    """
    prompt = PromptTemplate(
        input_variables=["user_query"],
        template=template,
        )
    
    response = llm(
            prompt.format(
                user_query=user_query
            )
        )
    st.write(response)
    
if prompt_method == "AI_assistant_email":
    sentiment = st.text_input("Enter the sentiment")
    customer_review = st.text_input("Enter the customer review")
    
    template = """You are a customer service AI assistant.
    Your task is to send an email reply to a valued customer.
    Given the customer email 
    Generate a reply to thank the customer for their review.
    If the sentiment is positive or neutral, thank them for
    their review.
    If the sentiment is negative, apologize and suggest that 
    they can reach out to customer service. 
    Make sure to use specific details from the review.
    Write in a concise and professional tone.
    Sign the email as `AI customer agent`.
    Customer review: {customer_review}
    Review sentiment: {sentiment}
    """
    
    prompt = PromptTemplate(
        input_variables=["customer_review", "sentiment"],
        template=template,
        )
    
    response = llm(
        prompt.format(
            customer_review=customer_review,
            sentiment = sentiment
            )
        )
    
    st.write(response)

