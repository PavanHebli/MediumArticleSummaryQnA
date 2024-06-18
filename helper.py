import requests
from bs4 import BeautifulSoup
from groq import Groq
from constants import prompts, inputMessage, ModelParam

def FetchMediumLink(ipURL):
    response=requests.get(ipURL)
    responseBS = BeautifulSoup(response.content, 'html.parser')
    return responseBS

def CheckMediumLink(responseBS):
    CheckPublisher = responseBS.find(class_='af ag ah ai aj ak al am an ao ap aq ar as at ab')
    if CheckPublisher:
        return True
    else: 
        return False
    
def GetSummary(param):
    prompts.summaryVar=param
    ipPromt=prompts.summary.substitute(summaryVar=param)
    output=QueryLLM(ipPromt)
    return output

def GenerateQuizQuestions(param1, param2):
    ipPromt=prompts.quizGenerator.substitute(questions=param1, summaryVar= param2)
    output=QueryLLM(ipPromt)
    return output

def QueryLLM(inputText, temp=ModelParam.temperature):
    client = Groq(
        api_key=ModelParam.api_key
    )
    completion = client.chat.completions.create(
        model=ModelParam.model,
        messages=[
            {
                "role": "user",
                "content": inputText
            }
        ],
        temperature=temp,
        max_tokens=ModelParam.max_tokens,
        top_p=ModelParam.top_p,
        stream=ModelParam.stream,
        stop=ModelParam.stop,
    )
    summaryText = ""    
    for chunk in completion:
        summaryText+= chunk.choices[0].delta.content or "" + " "
    return summaryText