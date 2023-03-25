import colorama
from colorama import Fore, Style
import openai
import os
import argparse
# Initialize colorama
colorama.init(autoreset=True)
import argparse


import subprocess

# Set the GitHub repository URL and the script file name
github_url = "https://github.com/tytan-codes/chatGPT.git"
script_name = "main.py"

# Get the latest commit hash from the GitHub repository
cmd = "git ls-remote " + github_url + " HEAD"
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode != 0:
    print("Error getting latest commit hash from GitHub.")
    exit()
latest_commit = result.stdout.decode().split()[0]

# Check if the latest commit is already downloaded
cmd = "git rev-parse HEAD"
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode != 0:
    print("Error getting current commit hash.")
    exit()
current_commit = result.stdout.decode().strip()
if current_commit == latest_commit:
    print("You are running the latest version of the script.")
else:
    os.system('clear')
    print(f"{Style.BRIGHT + Fore.RED}You are running an outdated version of the script.")
    print(f"{Style.BRIGHT}A new version of the script is available on GitHub.")
    print(f"{Style.BRIGHT}Latest commit: " + latest_commit)
    print(f"{Style.BRIGHT}Current commit: " + current_commit)
    print(f"{Style.BRIGHT + Fore.RED}Please update by running update.py")
    print(f'{Style.BRIGHT + Fore.RED}You updating will make your experience better')
    exit()



# Set OpenAI API key
openai.api_key = 'API KEY GOES HERE'

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



