from typing import Union
from fastapi import FastAPI, Request

import cohere
from cohere.classify import Example

import geocoder

import smtplib, ssl

port = 465  # For SSL
password = "" #will be written in deployment server
co = cohere.Client('')




examples=[
  Example("Help me", "negative"), 
  Example("I am stuck", "negative"), 
  Example("someone close to me is stuck", "negative"), 
  Example("I am thirsty", "negative"), 
  Example("I cannot move", "negative"), 
  Example("I cannot breath", "negative"), 
  Example("I need help", "negative"), 
  Example("I am ok", "positive"),
  Example("There is somebody following me", "negative"),  
  Example("We have got food", "positive"), 
  Example("I am away from the buildings", "positive"), 
  Example("Get away from the buildings", "neutral"), 
  Example("I am safe", "positive"), 
  Example("when is rescue team coming", "negative"),
]



app = FastAPI()



# Path: /{email_of_friend}/{status} example: www.distresscall.com/johndoe@gmail.com/i%20am%20stuck
@app.get("/{email_of_friend}}/{status}")
def read_root(request: Request, email_of_friend: str, status: str):
    voice_message = ""
    inputs=[voice_message]
    response = co.classify(
    inputs=inputs,
    examples=examples,
    )
    

    g = geocoder.ip(client_host = request.client.host)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("distresscallapp12314124@gmail.com", password)
        
    if response == "positive":
        return {"status": "safe"}
    elif response == "neutral":
        message = "need help, please come to my location: " + g.latlng
        server.sendmail("distresscallapp12314124@gmail.com", email_of_friend, message)
        return {"status": "need help"}
    else:
        message = "need immidiate help, please come to my location: " + g.latlng
        server.sendmail("distresscallapp12314124@gmail.com", email_of_friend, message)
        return {"status": "need immidiate help"}
    
