import json
import requests
import os
from bs4 import BeautifulSoup
from langchain.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains.summarize import load_summarize_chain
from dotenv import load_dotenv



load_dotenv()

SERPER_API_KEY = os.getenv('SERPER_API_KEY')
BROWSERLESS_API_KEY = os.getenv('BROWSERLESS_API_KEY')

# tool for searching links on internet
def search(query:str):

    url = 'https://google.serper.dev/search'

    payload = json.dumps({
        "q":query
    })

    headers = {
        'X-API-KEY':SERPER_API_KEY,
        'Content-type': 'application/json'
    }

    response = requests.request('POST',url,headers=headers,data=payload)

    print(response.text)

    return response.text

# tool for scraping websites

def summary(objective:str,content:str):

    llm = ChatOpenAI(temperature=0,model='gpt-3.5-turbo-16k-0613')

    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=10000, chunk_overlap = 500)

    docs = text_splitter.create_documents([content])
    map_prompt = """
    Write a summary of the following text for {objective}:
    "{text}"
    SUMMARY:
    """
    map_prompt_template = PromptTemplate(template=map_prompt,input_variables=["text","objective"])

    summary_chain = load_summarize_chain(llm,chain_type="map_reduce",map_prompt=map_prompt_template,
    combine_prompt = map_prompt_template,
    verbose=True                                    
    )

    output = summary_chain.run(input_documents=docs,objective=objective)

    return output

def scrape_website(url:str,objective:str):

    print('Scraping website...')

    headers = {
        'Cache-Control':'no-cache',
        'Content-type':'application/json'
    }

    data ={
        'url':url
    }
    data_json = json.dumps(data)

    post_url = f'https://chrome.browserless.io/content?token={BROWSERLESS_API_KEY}'
    response = requests.post(post_url,headers=headers,data=data_json)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content,'html.parser')
        text = soup.get_text()
        print(f'Content: {text}')
        if len(text) > 10000:
            return summary(objective,text)
        return text
    else:
        print(response)
        print(f'HTTP request failed with status code {response.status_code}')
