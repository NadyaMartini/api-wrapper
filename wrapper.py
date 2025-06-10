from fastapi import FastAPI
import requests
from openai import OpenAI
import os
SECRET_ID = os.environ.get('SECRET_ID')

client = OpenAI(api_key= SECRET_ID)




app = FastAPI()

@app.get("/")
def root():
    return "hello worlds"       

@app.post("/items/")
async def create_item(item):
    if item == "chair":
        return "chair? really?"
    else: 
        response = client.responses.create(
            model="gpt-4.1",
            input=item
)
        return response.output_text
    

#print(response.output_text)