import argparse

model_choices = ["gpt-3.5-turbo", "3.5", "gpt-4o", "4o", "gpt-4-turbo", "4"]

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--model", help="The OpenAI model", choices=model_choices)
args = parser.parse_args()

print(f"Selected model: {args.model}")
