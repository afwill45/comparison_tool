from openai import OpenAI
import time
import argparse
import os
import re

parser = argparse.ArgumentParser()
parser.parse_args()
parser.add_argument("-m", "--model", help ==)



client = OpenAI(organization='org-dNPZULtlZEweJKpXsK80byiq')


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
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