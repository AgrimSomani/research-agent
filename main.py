from pydantic import BaseModel
import fastapi
from agent import get_agent


app = fastapi.FastAPI()

class Research_Agent_Data(BaseModel):
    query:str

@app.post("/")
def researchAgent(data:Research_Agent_Data):
    query = data.query
    agent = get_agent()
    content = agent(query)
    return content['output']


    


