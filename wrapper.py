from fastapi import FastAPI
import requests
from openai import OpenAI
client = OpenAI(api_key="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"
)


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