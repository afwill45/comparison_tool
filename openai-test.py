from openai import OpenAI
import time
import argparse
import os
import re

#Declare default model, AI provider and OpenAI model options
model_use = "gpt-3.5-turbo"
platform = "OpenAI"
model_choices = ["gpt-3.5-turbo", "3.5", "gpt-4o", "4o", "gpt-4-turbo", "4"]

#Initialize the command line input parser
parser = argparse.ArgumentParser()

#Add the optional argument for a model. If one is not specified the default value will be used
parser.add_argument("-m", "--model", help="The OpenAI model", choices=model_choices)

#Parse the inputs
args = parser.parse_args()

#Change the value for the model depending on the command line input. If a value is not recognized, defaults to default value"
if platform == "OpenAI":
    if (args.model == "gpt-4o") or (args.model == "4o"):
        model_use = "gpt-4o"
    elif (args.model == "gpt-4-turbo") or (args.model == "4"):
        model_use = "gpt-4-turbo"


'''
When integration for other platforms like Anthropic's Claude and Google Gemini
Increase the model choices to account for them as well
And create parameters for platform
'''

#Initializes OpenAI API
client = OpenAI()
completion = client.chat.completions.create(
  #Selects OPENAI model based on command line inputs
  model= model_use,
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

end_time = int(time.time())
start_time = completion.created
response_length = len(completion.choices[0].message.content)
elapsed_time =  end_time - start_time
print(completion.choices[0].message.content)

print("")
print("Elapsed time = ", elapsed_time) 
print("Normalized score = ", response_length/elapsed_time)
print("Response length = ", response_length)
print("Model = ", model_use)
'''
Count the number of words or tokens produced by the model. Divide the no. of words/tokens by the elapsed time.
This will normalize the results. We want speed of delivery.
'''