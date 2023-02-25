from typing import Union

from fastapi import FastAPI

import cohere
from cohere.classify import Example

co = cohere.Client('ib4Rc6soXLKKinhSdbE7trjG1Gupc2ZuSLtUODa6')

examples=[
  Example("Help me", "negative"), 
  Example("I am stuck", "negative"), 
  Example("someone close to me is stuck", "negative"), 
  Example("I am thirsty", "negative"), 
  Example("I cannot move", "negative"), 
  Example("I cannot breath", "negative"), 
  Example("I need help", "negative"), 
  Example("I am ok", "positive"), 
  Example("We have got food", "positive"), 
  Example("I am away from the buildings", "positive"), 
  Example("Get away from the buildings", "neutral"), 
  Example("I am safe", "positive"), 
  Example("when is rescue team coming", "negative"),
]

app = FastAPI()




@app.get("/")
def read_root():
    voice_message = ""
    inputs=[voice_message]
    response = co.classify(
    inputs=inputs,
    examples=examples,
    )
    if response == "positive":
        return {"status": "safe"}
    elif response == "neutral":
        return {"status": "need help"}
    elif response == "negative":
        return {"status": "need immidiate help"}
    
    return {"": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}