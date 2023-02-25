import cohere
from cohere.classify import Example

co = cohere.Client('ib4Rc6soXLKKinhSdbE7trjG1Gupc2ZuSLtUODa6')

examples=[
  Example("Help me", "negative"), 
  Example("I am stuck under boulder", "negative"), 
  Example("someone close to me is stuck under a boulder", "negative"), 
  Example("I don't have any water", "negative"), 
  Example("I cannot move", "negative"), 
  Example("I cannot breath", "negative"), 
  Example("Somebody is looting my stuff", "negative"), 
  Example("I need help", "negative"), 
  Example("I am ok", "positive"), 
  Example("We have got enough food", "positive"), 
  Example("I am away from the buildings", "positive"), 
  Example("Get away from the buildings", "neutral"), 
  Example("There is somebody attacking me", "neutral"), 
  Example("I am safe", "positive"), 
  Example("when is rescue team coming", "negative"),
]

inputs=[voice_message]
response = co.classify(
  inputs=inputs,
  examples=examples,
)