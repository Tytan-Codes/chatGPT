import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)
import openai
import os
openai.api_key = 'API KEY GOES HERE!'


def essay():
    os.system('cls')
    ess = str(input('Write me an essay about... '))
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ess,
        temperature=0.9,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )

    text = response['choices'][0]['text']
    print ('Reply: '+text)

def story():
    os.system('cls')
    abt = print('Write me a story about... ')
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=abt,
        temperature=0.9,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )

    text = response['choices'][0]['text']
    print ('Reply: '+text)

def resume():
    os.system('cls')
    good = str(input('What are you good at? '))
    get = str(input('What job are you trying to get? '))
    jobs = str(input('What are your previous jobs? '))
    fit = str(input('Why are you a good fit? '))
    
    
    
    
        
        
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'I would like you to make me an resume. I am good at {good}. The job i am trying to get is called {get}. My previous jobs are {jobs}. I am a good fit because {fit}. ',
        temperature=0.9,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )

    text = response['choices'][0]['text']
    print ('Reply: '+text)
def chatGPT():
    os.system('cls')

    
        
    ask = str(input(f'{Fore.RED + Style.BRIGHT}What would you like to generate? '))
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=ask,
        temperature=0.9,
        max_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )

    text = response['choices'][0]['text']
    print ('Reply: '+text)
        
        
def pre():
    os.system('cls')
    print(f'{Fore.RED + Style.BRIGHT}(1) Make {Fore.CYAN + Style.BRIGHT}GPT-3{Fore.RED + Style.BRIGHT} make a resume.')
    print(f'{Fore.RED + Style.BRIGHT}(2) Make {Fore.CYAN + Style.BRIGHT}GPT-3{Fore.RED + Style.BRIGHT} write you a story.')
    print(f'{Fore.RED + Style.BRIGHT}(3) Make {Fore.CYAN + Style.BRIGHT}GPT-3{Fore.RED + Style.BRIGHT} write you an essay.')

    prey = int(input(f'{Fore.RED + Style.BRIGHT}What do you want to do? '))
    if prey == 1:
        resume()
    if prey == 2:
        story()
    if prey == 3:
        essay()

def ready():
    os.system('cls')
    print(f'{Fore.RED + Style.BRIGHT}Go to line 6 of the script and put your openAI API key.\nYou can get it from https://platform.openai.com/account/api-keys.\nTo put the API key in the script, type {Fore.CYAN + Style.BRIGHT}nano +6 main.py')
    print(f'{Fore.RED + Style.BRIGHT}(1) Ask {Fore.CYAN + Style.BRIGHT}GPT-3{Fore.RED + Style.BRIGHT} anything.')
    print(f'{Fore.RED + Style.BRIGHT}(2) Ask {Fore.CYAN + Style.BRIGHT}GPT-3{Fore.RED + Style.BRIGHT} pre-made things (ie. resume maker.).')
    
    readyy = int(input(f'{Fore.RED + Style.BRIGHT}What do you want to do?' ))
    if readyy == 1:
        chatGPT()
    elif readyy == 2:
        pre()

ready()