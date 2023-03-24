import colorama
from colorama import Fore, Style
import openai
import os
import argparse
# Initialize colorama
colorama.init(autoreset=True)
import argparse


# Set OpenAI API key
openai.api_key = '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'

def make_request(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    return response['choices'][0]['text']

# Define function for generating an essay
def essay():
    print("Generating essay...")
    ess = str(input('Write me an essay about... '))
    response = make_request(ess)
    print('Reply: ' + response)

# Define function for generating a story
def story():
    print("Generating story...")
    abt = str(input('Write me a story about... '))
    response = make_request(abt)
    print('Reply: ' + response)

# Define function for generating a resume
def resume():
    print("Generating resume...")
    good = str(input('What are you good at? '))
    get = str(input('What job are you trying to get? '))
    jobs = str(input('What are your previous jobs? '))
    fit = str(input('Why are you a good fit? '))

    prompt = f'I would like you to make me a resume. I am good at {good}. The job I am trying to get is called {get}. My previous jobs are {jobs}. I am a good fit because {fit}.'
    response = make_request(prompt)
    print('Reply: ' + response)

# Define function for chatting with GPT-3
def chat():
    print("Generating response...")
    ask = str(input(f'{Fore.RED + Style.BRIGHT}What would you like to ask? '))
    response = make_request(ask)
    print('Reply: ' + response)

# Define function for displaying the main menu
def main_menu():
    print(f'{Fore.RED + Style.BRIGHT}(1) Make {Fore.CYAN + Style.BRIGHT}GPT-3{Fore.RED + Style.BRIGHT} generate an essay.')
    print(f'{Fore.RED + Style.BRIGHT}(2) Make {Fore.CYAN + Style.BRIGHT}GPT-3{Fore.RED + Style.BRIGHT} generate a story.')
    print(f'{Fore.RED + Style.BRIGHT}(3) Make {Fore.CYAN + Style.BRIGHT}GPT-3{Fore.RED + Style.BRIGHT} generate a resume.')
    print(f'{Fore.RED + Style.BRIGHT}(4) Chat with {Fore.CYAN + Style.BRIGHT}GPT-3{Fore.RED + Style.BRIGHT}.')
    print(f'{Fore.RED + Style.BRIGHT}(5) Exit.')

# Define function for handling user input
def handle_input(input_str):
    if input_str == '1':
        essay()
    elif input_str == '2':
        story()
    elif input_str == '3':
        resume()
    elif input_str == '4':
        chat()

# Define function for running the program
def run():
    while True:
        main_menu()
        user_input = input(f'{Fore.RED + Style.BRIGHT}What do you want to do? ')
        if user_input == '5':
            break
        else:
            handle_input(user_input)




parser = argparse.ArgumentParser(description='It\'s chatGPT in python. As this script is not finished please make sure to look at the github for the latest updates.')
parser.add_argument('--essay', action='store_true', help='Generate\'s an essay about what ever you want.')
parser.add_argument('--chat', action='store_true', help='Chat with chatGPT')
parser.add_argument('--resume', action='store_true', help='Generate\'s an resume about what ever you want.')
parser.add_argument('--story', action='store_true', help='Generate\'s an story about what ever you want.')
args = parser.parse_args()

if args.essay:
    essay()
if args.chat:
    chat()
if args.resume:
    resume()
if args.story:
    story()

run()



