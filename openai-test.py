from openai import OpenAI
import time
import argparse
import os
import re

model_use = "gpt-3.5-turbo"
platform = "OpenAI"
model_choices = ["gpt-3.5-turbo", "3.5", "gpt-4o", "4o", "gpt-4-turbo", "4"]


parser = argparse.ArgumentParser()
parser.parse_args()
parser.add_argument("-m", "--model", help="The OpenAI model", choices = model_choices)
args = parser.parse_args()
if platform == "OpenAI":
  if (args.model == "gpt-4o") or (args.model == "4o"):
    model_use = "gpt-4o"
  elif(args.model == "gpt-4-turbo") or (args.model == "4"):
    model_use = "gpt-4-turbo"
'''
When integration for other platforms like Anthrophic's Claude and Google Gemini
Increase the model choices to account for them as well
And create paramters for platform
'''
    
    



client = OpenAI()
completion = client.chat.completions.create(
  model= model_use,
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)
end_time = int(time.time())
start_time = completion.created
print(completion.choices[0].message)

print("Elapsed time = ", end_time - start_time) 

'''
Count the number of words or tokens produced by the model. Divide the no. of words/tokens by the elapsed time.
This will normalize the
'''